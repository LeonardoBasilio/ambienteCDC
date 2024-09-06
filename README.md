# Change Data Capture (CDC) With Docker, Apache Kafka, Debezium and MYSQL.
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/LeonardoBasilio/ambienteCDC/blob/main/README.pt-br.md)


## Introduction

Change Data Capture (CDC) is the process of identifying and capturing changes made to data in a database and delivering those changes in real-time to downstream systems or processes. CDC plays a crucial role in data engineering by enabling real-time data integration and analysis, ensuring that the most up-to-date data is available for decision-making and operational processes.

This article provides a comprehensive guide to understanding CDC and setting up a CDC pipeline using Docker.

## Docker Compose Setup

The provided Docker Compose file orchestrates the deployment of all essential services, including MySQL, Debezium, Kafka, and Kafka UI.

## Architecture

The CDC pipeline follows this flow:
### MySQL -> CDC -> Debezium -> Kafka.

- **[MySQL]:** The source database where changes are tracked.
- **[Debezium]:** Captures changes from MySQL and publishes them to Kafka topics.
- **[Apache Kafka]:** A distributed messaging system that manages CDC events.
- **[Kafka UI]:** A visual interface for monitoring data flows within Kafka.

## Implementation and Testing

- Run Docker Compose using the following commands:
```bash
docker-compose up -d
```

- Access MySQL to configure the database:
```bash
docker-compose exec mysql bash -c 'mysql -u root -pdebezium'
```

# After authentication, run the following SQL commands:
```sql
SELECT user, host FROM mysql.user;
CREATE DATABASE cdc;
GRANT ALL ON cdc.* TO 'debezium'@'%';
FLUSH PRIVILEGES;
SHOW databases;
```

# Access MySQL as the 'debezium' user:
```bash
docker-compose exec mysql bash -c 'mysql -u debezium -pdbz'
```

# Create a table in the 'cdc' database:
```sql
CREATE TABLE cdc.client(
    clientId int,
    firstName varchar(255),
    lastName varchar(255),
    city varchar(255)
);
USE cdc;
SHOW tables;
```

# Insert data into the 'client' table:
```sql
INSERT INTO client VALUES (1, "Joao", "Fernandes", "São Paulo");
INSERT INTO client VALUES (2, "Maria", "Silva", "Rio de Janeiro");
INSERT INTO client VALUES (3, "Carlos", "Santos", "Belo Horizonte");
INSERT INTO client VALUES (4, "Ana", "Oliveira", "Curitiba");
INSERT INTO client VALUES (5, "Pedro", "Almeida", "Porto Alegre");
INSERT INTO client VALUES (6, "Juliana", "Souza", "Fortaleza");
INSERT INTO client VALUES (7, "Rafael", "Costa", "Salvador");
```

- Create a Debezium connector to monitor MySQL and publish to Kafka topics.

- Configure Debezium and Kafka to monitor changes and publish them.

# Update data in the 'client' table:
```sql
UPDATE client SET city = "Uberlândia" WHERE clientId = 1;
```

## Kafka UI

Set up Kafka UI for visual monitoring of Kafka data flows.

Access Kafka UI at: [http://localhost:10000/](http://localhost:10000/)

## Conclusion

Integrating Apache Spark Streaming into the CDC pipeline allows organizations to extract valuable insights from streaming data in real-time. With Docker Compose simplifying deployment and management, this architecture offers a scalable and efficient solution for real-time data integration and analysis.

Happy Learning! ✌️

## Useful Commands
```bash
# Start Docker Compose
docker-compose up -d
```

# Register the Debezium connector
```bash
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" http://localhost:8083/connectors/ -d @./conf/register-mysql.json
```

# List Kafka topics
```bash
docker-compose exec kafka /kafka/bin/kafka-topics.sh --bootstrap-server kafka:9092 --list
```

# Consume data from a Kafka topic
```bash
docker-compose exec kafka /kafka/bin/kafka-console-consumer.sh     --bootstrap-server kafka:9092     --from-beginning     --property print.key=true     --topic dbserver1.cdc.client
```

