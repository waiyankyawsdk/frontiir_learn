# importing the required libraries  
from time import sleep  
from json import dumps  
from kafka import KafkaProducer  

# initializing the Kafka producer  
my_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:9092'],  
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )  

# generating the numbers ranging from 1 to 500  
for num in range(500):  
    my_data = {'number' : num}  
    my_producer.send('numbers', value = my_data)
    sleep(5)  