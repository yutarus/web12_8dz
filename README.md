<h1 align="center">Homework #8</h1>

Running docker container with Redis
- docker run --name cache -d -p 6379:6379 redis

Running docker container with RabbitMQ

- docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management

<h3>First part of homework</h3>

Filling the database

- python3 seeds.py

Running main.py script

 - python3 main.py

<h3>Second part of homework</h3>

Starting Consumer

-  python3 src/consumer.py 

Starting Producer

- python3 src/producer.py 