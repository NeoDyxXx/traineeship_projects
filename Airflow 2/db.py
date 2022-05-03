import sqlite3
from scrapper import get_data_fbi

conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

def create_table(name: str):
    try:
        cursor.execute("""CREATE TABLE {0}
                    (uid text, aliases text, publication text, age_min text, age_max text, weight_min text,
                    weight_max text, height_min text, height_max text, caution text, nationality text, sex text, image_url text)
                """.format(name))
    except:
        pass


def commit_change():
    conn.commit()


def select_table(name: str):
    cursor.execute('select * from {0}'.format(name))
    return cursor.fetchall()


def count_in_table(name: str):
    cursor.execute('select count(*) from {0}'.format(name))
    return cursor.fetchall()[0][0]


def check_uid_in_table(name: str, uid: str):
    cursor.execute('select count(*) from {0} where uid = \'{1}\''.format(name, uid))
    return cursor.fetchall()[0][0]


def insert_in_table(name: str, data: dict):
    sql = "INSERT INTO {0} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)".format(name)
    new_data = []
    for item in data['data']:
        if check_uid_in_table('fbi', item['uid']) == 0:
            cursor.execute(sql, (item['uid'], item['aliases'], item['publication'], item['age_min'], item['age_max'], 
                item['weight_min'], item['weight_max'], item['height_min'], item['height_max'], 
                item['caution'], item['nationality'], item['sex'], item['image_url']))
            
            new_data.append(item)
    
    if new_data.__len__() == 0:
        data['status'] = 'Not update'
    else:
        data['status'] = 'Update'

    data['data'] = new_data

    return data