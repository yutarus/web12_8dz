import pika
from faker import Faker

from pprint import pprint
from models import Contacts
import connect


fake = Faker()


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue', durable=True)


def create_contacts() -> list[str]:
    """
    Create contacts and add them to the email queue.
    :return: list of messages
    """
    result = []
    for _ in range(10):
        contact = Contacts(fullname=fake.name(), email=fake.email(), address=fake.address())
        contact.save()

        channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id).encode())
        result.append(f'Contact {contact.id} added to the queue')

    return result


if __name__ == '__main__':
    pprint(create_contacts())



