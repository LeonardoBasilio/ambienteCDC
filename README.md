Change Data Capture (CDC) With Docker, Apache Kafka, Debezium and MYSQL.

Introdution

Change Data Capture (CDC) is the process of identifying and capturing changes made to data in a database and delivering those changes in real-time to downstream systems or processes. CDC plays a crucial role in data engineering by enabling real-time data integration and analysis, ensuring that the most current data is available for decision-making and operational processes.

This articles presents a comprehensive guilde to understaing CDC and setting up a CDC pipeline using Docker.


Docker Compose Setup


Architecture
The CDC pipeline follows the flow: MYSQL -> CDC -> Debezium -> Kafka.

MYSQL: The Source database where changes are tracked.
Debezium: Captures changes from MYSQL and publishes them to Kafka Topics.
Apache Kafka: A distributed messaging system that handles CDC events.
Kafka UI: A visual interface for monitoring data flows within Kafka.


Implementation and Testing
Run docker compose by using the following commands:

docker-compose up -d 