import os
from google.cloud import pubsub_v1

credentials_path = r'C:\Users\josuv\OneDrive\Documentos\ASR-Latencia\requests-messages_privatekey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

time_out = 5.0


subscriber =  pubsub_v1.SubscriberClient()
subscription_path = 'projects/pub-sub-messages/subscriptions/requests-messages-sub'

def callback (message):
    print(f"Received message")
    print(f"data: {message.data}")
    message.ack()

    if message.attributes:
        print('Messsage: ')
        for key in message.attributes:
            value = message.attributes.get(key)
            print(f"{key}: {value}")


streaming  =  subscriber.subscribe(subscription_path , callback=callback)
print( "Listening for messages on {subscription_path}")



with subscriber:
    try:
        streaming.result()
    except TimeoutError:
        streaming.cancel()
        streaming.result()

