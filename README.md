# Multilanguage README Pattern
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/LeonardoBasilio/ambienteCDC/blob/main/README.pt-br.md)

Change Data Capture (CDC) With Docker, Apache Kafka, Debezium and MYSQL.

Introdution

Change Data Capture (CDC) is the process of identifying and capturing changes made to data in a database and delivering those changes in real-time to downstream systems or processes. CDC plays a crucial role in data engineering by enabling real-time data integration and analysis, ensuring that the most current data is available for decision-making and operational processes.

This articles presents a comprehensive guilde to understaing CDC and setting up a CDC pipeline using Docker.

Docker Compose Setup 

The provided Docker Compose file orchestrates the deployment of all essential services, including MySQL, Debezium, Kafka, and Kafka UI.

Architecture
The CDC pipeline follows the flow: MYSQL -> CDC -> Debezium -> Kafka.

MYSQL: The Source database where changes are tracked.
Debezium: Captures changes from MYSQL and publishes them to Kafka Topics.
Apache Kafka: A distributed messaging system that handles CDC events.
Kafka UI: A visual interface for monitoring data flows within Kafka.


Implementation and Testing
Run docker compose by using the following commands:

docker-compose up -d 

Access MySQL to set up the database.
Create a Debezium connector to monitor MySQL and publish to Kafka topics.

Configure Debezium and Kafka to monitor changes and publish them.

Kafka UI 

Configure Kafka UI for visual monitoring of Kafka Data Flows

Access Kafka UI at: http://localhost:10000/



Conclusion
Integrating Apache Spark Streaming into the CDC pipeline empowers organizations to extract valuable insights from streaming data in real-time. With Docker Compose facilitating deployment and management, this architecture offers a scalable and efficient solution for real-time data integration and analysis.

Happy Learning! ✌️

Useful commands


# Start Docker Compose
docker-compose   up -d

# Access MySQL as root user
docker-compose  exec mysql bash -c 'mysql -u debezium -pdbz'

# After authentication, execute SQL commands
SELECT user,host FROM mysql.user;

CREATE DATABASE cdc;

GRANT ALL ON cdc.* TO 'debezium'@'%';

FLUSH PRIVILEGES;

SHOW databases;

# Access MySQL as debezium user
docker-compose  exec mysql bash -c 'mysql -u debezium -pdbz'

# Create table in the cdc database
CREATE TABLE cdc.cliente(
    clienteId int,
    nome varchar(255),
    sobrenome varchar(255),
    cidade varchar(255)
);

USE cdc;
SHOW tables;



INSERT INTO cliente VALUES (1,"Joao","Fernandes","São Paulo"),
INSERT INTO cliente VALUES (2, "Maria", "Silva", "Rio de Janeiro");
INSERT INTO cliente VALUES (3, "Carlos", "Santos", "Belo Horizonte");
INSERT INTO cliente VALUES (4, "Ana", "Oliveira", "Curitiba");
INSERT INTO cliente VALUES (5, "Pedro", "Almeida", "Porto Alegre");
INSERT INTO cliente VALUES (6, "Juliana", "Souza", "Fortaleza");
INSERT INTO cliente VALUES (7, "Rafael", "Costa", "Salvador");

Kafka Connector Debezium
# Register Debezium connector
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @./conf/register-mysql.json
# List Kafka topics
docker-compose  exec kafka /kafka/bin/kafka-topics.sh \
--bootstrap-server kafka:9092 \
--list
# Consume data from Kafka topic
docker-compose exec kafka /kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server kafka:9092 \
    --from-beginning \
    --property print.key=true \
    --topic dbserver1.cdc.demo 