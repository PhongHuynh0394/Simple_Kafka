from kafka import KafkaConsumer


TOPIC = 'KafkaExplored'
TOPIC = 'toll'
consumer = KafkaConsumer(TOPIC, bootstrap_servers='localhost:9093')
for msg in consumer:
    topic = msg[0]
    value = msg[6]
    print(msg)
    print(f"{topic}:{value.decode()}")