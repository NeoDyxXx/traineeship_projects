from kafka import KafkaProducer
import time

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        print("Try create producer")
        # _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
        _producer = KafkaProducer(bootstrap_servers=['broker:29092'], api_version=(0, 10))
        print("Create producer")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':
    time.sleep(10)
    with open('file.txt', 'w') as file:
        producer = connect_kafka_producer()

        for i in range(20):
            publish_message(producer, 'test', '123', i.__str__())
            file.write("push message")
            time.sleep(3)