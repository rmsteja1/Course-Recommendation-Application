from kafka import KafkaProducer,KafkaConsumer
from json import dumps , loads
from flask import Flask
from time import sleep 
# import sys
# sys.path.append('../consumer')
# from consumerDB import consumerDbData


def send_message():

    my_producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer = lambda x:dumps(x).encode('utf-8') )
    print("test")
    my_producer.send('user_authentication',"message from producer")
    

    
def receive_message():
    try:
        my_consumer = KafkaConsumer(  
        'user_authentication_db_data',  
        bootstrap_servers = ['localhost : 9092'],  
        auto_offset_reset = 'latest',  
        enable_auto_commit = True,  
        group_id = 'my-group',  
        value_deserializer = lambda x : loads(x.decode('utf-8'))  
        )
        print("1")
        for message in my_consumer:
            print("producer side check")
            print(message.value)
            return message.value
        return "no value"
	
    except Exception as e:
        print(e)


app = Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
    print("testing")
    send_message()
    res = receive_message()
    return res
    #return 'Hello, World!'




if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    print("app is running")
    app.run(debug=True)


