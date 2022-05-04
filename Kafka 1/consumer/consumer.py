from kafka import KafkaConsumer
import time

# consumer = KafkaConsumer('test', group_id='new_group', bootstrap_servers=['localhost:9092'])
consumer = KafkaConsumer('test', group_id='new_group', bootstrap_servers=['broker:29092'])

with open('message.log', 'w', encoding='utf-8') as file:
    for msg in consumer:
        file.write(msg)