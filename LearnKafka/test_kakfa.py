from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers = ['172.18.191.185:9094'],
    security_protocol = 'SASL_PLAINTEXT',
    sasl_mechanism = 'PLAIN',
    sasl_plain_username = 'erp13user',  
    sasl_plain_password ='Fr0nt!!rerp13'
)

headers_list = [('Event-type', b'Test')]
try:
    producer.send('erp.outbox', key=b'key', value=b'value')
except AttributeError as e:
    print("The value assigned to the object is Nonetype")