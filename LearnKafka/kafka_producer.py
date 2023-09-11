from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
producer = KafkaProducer(
                bootstrap_servers = ['172.18.191.185:9092'],
                security_protocol = 'SASL_PLAINTEXT',
                sasl_mechanism = 'PLAIN',
                sasl_plain_username = 'erp13user',  
                sasl_plain_password ='Fr0nt!!rerp13'
            )

# Asynchronous by default
# headers_to_send = [('key1', b'value1'), ('key2', b'value2'), ('key1', b'repeated_key')]
future = producer.send('erp.outbox', key=b'foo', value=b'bar')

# future = producer.send('erp.outbox', {'event-type': 'create'})

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError as err:
    # Decide what to do if produce request failed...
    print(err.exception())
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

# produce keyed messages to enable hashed partitioning
# producer.send('my-topic', key=b'foo', value=b'bar')

# encode objects via msgpack
# producer = KafkaProducer(value_serializer=msgpack.dumps)
# producer.send('msgpack-topic', {'key': 'value'})

# produce json messages
# producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
# future = producer.send('erp.outbox', {'event-type': 'create'})

# produce asynchronously
# for _ in range(100):
#     producer.send('my-topic', b'msg')

# def on_send_success(record_metadata):
#     print(record_metadata.topic)
#     print(record_metadata.partition)
#     print(record_metadata.offset)

# def on_send_error(excp):
#     log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
# producer.send('my-topic', b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
# producer.flush()

# configure multiple retries
# producer = KafkaProducer(retries=5)