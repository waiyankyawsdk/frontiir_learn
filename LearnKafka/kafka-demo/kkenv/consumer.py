# importing the required modules  
from json import loads  
from kafka import KafkaConsumer  
from pymongo import MongoClient  

# generating the Kafka Consumer  
my_consumer = KafkaConsumer(  
    'numbers',  
     bootstrap_servers = ['localhost : 9092'],  
     auto_offset_reset = 'earliest',  
     enable_auto_commit = True,  
     group_id = 'num-group',  
     value_deserializer = lambda x : loads(x.decode('utf-8'))  
     )  
my_client = MongoClient('localhost : 27017')  
my_collection = my_client.numbers.numbers

for message in my_consumer:  
    message = message.value  
    collection.insert_one(message)  
    print(message + " added to " + my_collection)  