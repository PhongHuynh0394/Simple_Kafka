import datetime
from kafka import KafkaProducer
from time import sleep, time, ctime

producer = KafkaProducer(bootstrap_servers='localhost:9093')

TOPIC = 'toll'
try:
    for _ in range(100):
        the_dt = str(datetime.datetime.utcnow())
        val = f"Count: {_} at {the_dt}".encode(encoding='utf8')
        producer.send(TOPIC, value=val)
        sleep(2)

    producer.close()
except Exception as e:
    print(e)