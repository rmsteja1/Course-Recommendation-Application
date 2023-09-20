from kafka import KafkaConsumer,KafkaProducer
import os
from flask import Flask
from json import loads ,dumps 

try:
    
    
    my_consumer = KafkaConsumer(  
    'user_authentication',  
    bootstrap_servers = ['localhost : 9092'],  
    auto_offset_reset = 'latest',  
    enable_auto_commit = True,  
    group_id = 'my-group',  
    value_deserializer = lambda x : loads(x.decode('utf-8'))  
    )
    my_producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer = lambda x:dumps(x).encode('utf-8') )

    for message in my_consumer:  
        print("consumer side check")
        print(message.value)
        #break
    my_producer.send('user_authentication_db_data',"message from consumer data sent")
        

except Exception as e:
    raise e


