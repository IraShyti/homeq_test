import pika, os, time
import json
from utilities.utilities import *
from workers.apartments_worker import *


class RabbitMq(object):
  @background
  def __init__(self):
    # Access the CLODUAMQP_URL
    self.queue_name = 'apartments'
    self.exchange_name = ' integration.exchange'

    # Access the CLODUAMQP_URL
    url = os.environ.get('CLOUDAMQP_URL',
                         'amqp://pujsxkjn:V2xiYe4PJN1O2AsPBQ26KuPy5iwfY4eM@bee.rmq.cloudamqp.co m/pujsxkjn')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)

    channel = connection.channel()

    channel.queue_declare(self.queue_name)

    channel.queue_bind(exchange=self.exchange_name,
                       queue=self.queue_name,
                       routing_key='integration.exchange')
    # Subscribe queue
    channel.basic_consume(self.callback,
                          queue=self.queue_name,
                          no_ack=True)

    # Start Consuming from the queue
    channel.start_consuming()
    connection.close()

    # Function called on incoming messages

  def callback(self, ch, method, properties, body):
    self.apartment_process_function(body)

  def apartment_process_function(self, msg):
    print(" Apartments processing")
    print(" Received %r" % msg)

    my_json = msg.decode('ISO-8859-1').replace("'", '"')
    my_json = my_json.replace(": True", ": true")
    my_json = my_json.replace(": False", ": false")
    data = json.loads(my_json)

    for element in data:
      print(str(element) + " " + str(data[element]) + " " + str(type(data[element])))
    # PROCESS APARTMENT
    ApartmentsWorker().proceed_apartments(data)

    print(" Apartments processing finished")
    return
