from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('test', group_id='my_favorite_group', bootstrap_servers=['localhost:9092'])

for msg in consumer:
    print (msg)