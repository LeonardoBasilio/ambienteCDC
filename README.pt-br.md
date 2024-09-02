# Captura de Dados de Mudança (CDC) Com Docker, Apache Kafka, Debezium e MySQL
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/LeonardoBasilio/ambienteCDC/blob/main/README.md)

Introdução

A Captura de Dados de Mudança (Change Data Capture, CDC) é o processo de identificar e capturar mudanças feitas em dados em um banco de dados e entregar essas mudanças em tempo real para sistemas ou processos downstream. O CDC desempenha um papel crucial na engenharia de dados ao permitir a integração e análise de dados em tempo real, garantindo que os dados mais atualizados estejam disponíveis para a tomada de decisões e processos operacionais.

Este artigo apresenta um guia abrangente para entender o CDC e configurar um pipeline de CDC usando Docker.

## Configuração do Docker Compose

O arquivo Docker Compose fornecido orquestra a implantação de todos os serviços essenciais, incluindo MySQL, Debezium, Kafka e Kafka UI.

## Arquitetura

O pipeline de CDC segue o fluxo: 
### MySQL -> CDC -> Debezium -> Kafka.

- [MySQL]: O banco de dados de origem onde as mudanças são rastreadas.
- [Debezium]: Captura as mudanças do MySQL e as publica em tópicos do Kafka.
- [Apache Kafka]: Um sistema de mensagens distribuído que gerencia eventos de CDC.
- [Kafka UI]: Uma interface visual para monitoramento dos fluxos de dados dentro do Kafka.


## Implementação e Testes

- Execute o Docker Compose usando os seguintes comandos:
```
docker-compose up -d
```
- Acesse o MySQL para configurar o banco de dados.
```
docker-compose exec mysql bash -c 'mysql -u root -pdebezium'
```

# Após a autenticação, execute os comandos SQL
SELECT user, host FROM mysql.user;

CREATE DATABASE cdc;

GRANT ALL ON cdc.* TO 'debezium'@'%';

FLUSH PRIVILEGES;

SHOW databases;

# Acessar o MySQL como usuário debezium
docker-compose exec mysql bash -c 'mysql -u debezium -pdbz'
```
```
# Criar tabela no banco de dados cdc
CREATE TABLE cdc.cliente(
    clienteId int,
    nome varchar(255),
    sobrenome varchar(255),
    cidade varchar(255)
);

USE cdc;
SHOW tables;

# Inserir dados na tabela cliente
INSERT INTO cliente VALUES (1, "Joao", "Fernandes", "São Paulo");
INSERT INTO cliente VALUES (2, "Maria", "Silva", "Rio de Janeiro");
INSERT INTO cliente VALUES (3, "Carlos", "Santos", "Belo Horizonte");
INSERT INTO cliente VALUES (4, "Ana", "Oliveira", "Curitiba");
INSERT INTO cliente VALUES (5, "Pedro", "Almeida", "Porto Alegre");
INSERT INTO cliente VALUES (6, "Juliana", "Souza", "Fortaleza");
INSERT INTO cliente VALUES (7, "Rafael", "Costa", "Salvador");
```

- Crie um conector Debezium para monitorar o MySQL e publicar nos tópicos do Kafka.

- Configure o Debezium e o Kafka para monitorar mudanças e publicá-las.

## Kafka UI

Configure o Kafka UI para monitoramento visual dos fluxos de dados do Kafka.

Acesse o Kafka UI em:![(http://localhost:10000/)]

## Conclusão

Integrar o Apache Spark Streaming no pipeline de CDC permite que as organizações extraiam insights valiosos dos dados em streaming em tempo real. Com o Docker Compose facilitando a implantação e o gerenciamento, essa arquitetura oferece uma solução escalável e eficiente para a integração e análise de dados em tempo real.

Feliz Aprendizado! ✌️

## Comandos úteis
```
# Iniciar o Docker Compose
docker-compose up -d
```

```


```
# Registrar o conector Debezium
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" http://localhost:8083/connectors/ -d @./conf/register-mysql.json

# Listar tópicos do Kafka
docker-compose exec kafka /kafka/bin/kafka-topics.sh \
--bootstrap-server kafka:9092 \
--list

# Consumir dados de um tópico do Kafka
docker-compose exec kafka /kafka/bin/kafka-console-consumer.sh \
    --bootstrap-server kafka:9092 \
    --from-beginning \
    --property print.key=true \
    --topic dbserver1.cdc.cliente
```
