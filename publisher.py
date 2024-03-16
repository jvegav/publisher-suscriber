import os
from google.cloud import pubsub_v1

credentials_path = r'C:\Users\josuv\OneDrive\Documentos\ASR-Latencia\requests-messages_privatekey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/pub-sub-messages/topics/requests-messages'

data = 'Datos Del Cliente '
data = data.encode('utf-8')
attributes = {
    'client': 'Josue Vega',
    'email': 'josuevega2004@uniandes',
    'phone': '3101234567'

}

future = publisher.publish(topic_path, data,**attributes)
print(f'published message id {future.result()}')