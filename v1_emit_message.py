# Add imports at the beginning of the file
import pika

# Create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Use the connection to create a communication channel
ch = conn.channel()

# Use the channel to declare a queue
ch.queue_declare(queue="hello")

# Define the message to be sent
message = "This is a different message7!"

# Use the channel to publish the message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)

# Print the message sent to the console for the user
print(f" [x] Sent '{message}'")

# Close the connection to the server
conn.close()