import requests
import smtplib
import json
import db

class MyOperator():
    def __init__(
            self,
            user,
            pwd,
            recipient,
            **kwargs) -> None:
        self.user = user
        self.pwd = pwd
        self.recipient = recipient

    def get_data_fbi(self, count: int):
        data = requests.get('https://api.fbi.gov/@wanted?pageSize={0}&page=1&sort_on=modified&sort_order=desc'.format(count.__str__())).json()

        result_data = {
            'name': 'Kirill Kraynov',
            'status': None,
            'data': []
        }

        for item in data['items']:
            new_data = {
                'uid': item['uid'],
                'aliases': "None",
                'publication': item['publication'],
                'age_min': item['age_min'],
                'age_max': item['age_max'],
                'weight_min': item['weight_min'],
                'weight_max': item['weight_max'],
                'height_min': item['height_min'],
                'height_max': item['height_max'],
                'caution': item['caution'],
                'nationality': item['nationality'],
                'sex': item['sex'],
                'image_url': item['images'][0]['original']
            }

            if item['aliases'] is not None:
                new_data['aliases'] = ", ".join(item['aliases'])

            result_data['data'].append(new_data)

        return result_data

    def send_email(self, user, pwd, recipient, subject, body):
        FROM = user
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()

    def execute(self, context):
        print("start")
        db.create_table('fbi')

        count = 20
        while True:
            data = db.insert_in_table('fbi', self.get_data_fbi(count))
            if data['status'] != 'Not update':
                break
            else:
                count += 20

        print("1")
        db.commit_change()
        print("Commit")
        self.send_email(self.user, self.pwd, self.recipient, "Automatic send message. Kirill Kraynov", json.dumps(data))
        
        print(db.select_table('fbi'))
        print(count)


app = MyOperator('yakirik3@gmail.com', 'coqilwvblkcjdwza', 'kraynov.kirill2015@yandex.ru')
app.execute(None)