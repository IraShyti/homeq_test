import pika, os, time
import json
from utilities.utilities import *
from workers.apartments_worker import *


class RabbitMq(object):
  @background
  def __init__(self):
    # Access the CLODUAMQP_URL
    url = os.environ.get('CLOUDAMQP_URL',
                         '')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='apartments')


    # Subscribe queue
    channel.basic_consume(self.callback,
                          queue='apartments',
                          no_ack=True)

    # Start Consuming from the queue
    channel.start_consuming()
    connection.close()

  # Function called on incoming messages
  def callback(self, ch, method, properties, body):
    self.apartment_process_function(body)

  def apartment_process_function(self,msg):
    print(" Apartments processing")
    print(" Received %r" % msg)

    my_json = msg.decode('ISO-8859-1').replace("'", '"')
    my_json = my_json.replace(": True", ": true")
    my_json = my_json.replace(": False", ": false")
    data = json.loads(my_json)

    # PROCESS APARTMENT
    ApartmentsWorker().proceed_apartments(data)

    print(" Apartments processing finished")
    return












