RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'




import pika
from os import environ ###

#local RABBITMQ
hostname = environ.get('rabbit_host') or 'localhost'
port = environ.get('rabbit_port') or 5672
# connect to the broker and set up a communication channel in the connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))


                            # # Declare exchange and queue
                            # channel.exchange_declare(exchange=RABBITMQ_SELL_EXCHANGE, exchange_type='fanout')
                            # channel.queue_declare(queue=RABBITMQ_SELL_QUEUE)
                            # channel.queue_bind(exchange=RABBITMQ_SELL_EXCHANGE, queue=RABBITMQ_SELL_QUEUE)
                            # # Publish order to exchange
                            # order = {'sell_price': current_coin_pricing, 'sell_quantity': sell['sell_quantity'], 'ordercoin': sell['ordercoin'], 'total_amount_earned': total_amount_gain}
                            # channel.basic_publish(exchange=RABBITMQ_BUY_EXCHANGE, routing_key='', body=json.dumps(order))
                            # # Close RabbitMQ connection
                            # connection.close()
#################
channel = connection.channel()
#==================================================== Buy Order ========================================================================================================

# Set up the exchange if the exchange doesn't exist
# - use a 'fanout' exchange to enable interaction
exchangetype="fanout"
RABBITMQ_BUY_EXCHANGE_NAME = 'buyorders'
RABBITMQ_BUY_QUEUE = 'buyordersqueue'
channel.exchange_declare(exchangename=RABBITMQ_BUY_EXCHANGE_NAME, exchange_type=exchangetype, durable=True)
channel.queue_bind(exchange = RABBITMQ_BUY_EXCHANGE_NAME, queue=RABBITMQ_BUY_QUEUE) 

    
#====================================================End Buy Order ========================================================================================================
#==================================================== Sell Order ========================================================================================================

############   tele queue    #############
#delcare tele queue
exchangetype="fanout"
RABBITMQ_SELL_EXCHANGE_NAME = 'sellorders'
RABBITMQ_SELL_QUEUE = 'sellordersqueue'
channel.exchange_declare(exchange= RABBITMQ_SELL_EXCHANGE_NAME, exchange_type=exchangetype, durable=True)
    # 'durable' makes the queue survive broker restarts

#bind twilio_Log queue
channel.queue_bind(exchange = RABBITMQ_SELL_EXCHANGE_NAME, queue=RABBITMQ_SELL_QUEUE) 
    # bind the queue to the exchange via the key
    # 'routing_key=#' => any routing_key would be matched
    
#==================================================== End Sell Order ========================================================================================================

"""
This function in this module sets up a connection and a channel to a cloud AMQP broker,
and declares a 'topic' exchange to be used by the microservices in the solution.
"""


def check_setup():
    # The shared connection and channel created when the module is imported may be expired, 
    # timed out, disconnected by the broker or a client;
    # - re-establish the connection/channel is they have been closed
    global connection, channel, hostname, port, exchangename, exchangetype

    if not is_connection_open(connection):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port, heartbeat=3600, blocked_connection_timeout=3600))
    if channel.is_closed:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)


def is_connection_open(connection):
    # For a BlockingConnection in AMQP clients,
    # when an exception happens when an action is performed,
    # it likely indicates a broken connection.
    # So, the code below actively calls a method in the 'connection' to check if an exception happens
    try:
        connection.process_data_events()
        return True
    except pika.exceptions.AMQPError as e:
        print("AMQP Error:", e)
        print("...creating a new connection.")
        return False