# Smartphone Price Prediction Using Big Data 

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Technologies Used](#2-technologies-used)
3. [Architecture](#3-architecture)
4. [Software Requirements for Running the Project](#5-software-requirements-for-running-the-project)
6. [How to Run](#6-how-to-run)
## 1. Project Overview
This project aims to predict smartphone prices using a combination of batch and stream processing techniques in a Big Data environment. The architecture follows the Lambda Architecture pattern, providing both real-time and batch processing capabilities to users.

## 2. Technologies Used
* **Ingestion Layer:** Apache Kafka (message broker)
* **Stream Layer:** XGBoost (machine learning model), Apache HBase (real-time View)
* **Batch Layer:** Apache Spark (data processing framework), Apache Airflow (workflow orchestration), PostgreSQL (data warehouse (Batch View))



## 3. Architecture

- Here is the architecture :
 ![architecture](images/architecture.png)


The project architecture consists of five main layers: the ingestion layer, the batch layer, the stream layer, the serving layer and the visualization layer.

### Ingestion Layer
- **Apache Kafka**: Utilized for real-time data ingestion from an API providing smartphone data.
   - **Consumer**: Collects data from the API and feeds it into the stream and batch layer.

### Stream Layer
- **Producer**: A machine learning model developed using XGBoost to estimate smartphone prices. This model runs in real-time and stores predictions in a realtime view. (details about the model <a href="https://github.com/aymane-maghouti/Sentiment-Analysis-for-Jumia-Reviews-and-Smartphone-Price-Prediction-System" target="_blank">here</a> )

### Batch Layer
- **HDFS**: Data from the API is stored in HDFS as part of the data lake solution.
 - **PySpark**: Performs data transformation on stored data using PySpark.
 - **Apache Airflow**: Orchestrates the batch processing workflow.


## 4. Software Requirements for Running the Project

This project requires the following software to be installed and configured on your system:

**Big Data Stack:**

* **Apache Kafka (version 2.6.0)**
* **Apache HBase (version 1.2.6)** 
* **Apache Hadoop (version 2.7.0)** 
* **Apache Spark (version 3.3.4)** 
* **PostgreSQL database**

**Programming Languages and Frameworks:**

* **Python (version 3.10.x or later)** 
* **Java 17 (or compatible version)** 

**Machine Learning Library:**

* **XGBoost** 




By installing and configuring these tools, you will have the necessary environment to run this project and leverage its real-time and batch processing capabilities for smartphone price prediction and analysis.

## 5. How to Run
To set up and run the project locally, follow these steps:

  - Clone the repository:
   ```bash
   git clone https://github.com/aymane-maghouti/Big-Data-Project
   ```


#### **1. Stream Layer**
   - Start Apache zookeeper

   ```batch 
zookeeper-server-start.bat C:/kafka_2.13_2.6.0/config/zookeeper.properties
```
   - Start Kafka server

   ```batch 
kafka-server-start.bat C:/kafka_2.13_2.6.0/config/server.properties
```
   - Create Kafka topic

   ```batch 
kafka-topics.bat --create --topic smartphoneTopic --bootstrap-server localhost:9092
```

  - Run the kafka producer

   ```batch 
kafka-console-producer.bat --topic smartphoneTopic --bootstrap-server localhost:9092
```

  - Run the kafka consumer

   ```batch 
kafka-console-consumer.bat --topic smartphoneTopic --from-beginning --bootstrap-server localhost:9092
```

  - Start HDFS and yarn (start-all or start-dfs and start-yarn)

   ```batch 



#### **2. Batch Layer**
   - Start the Apache Airflow instance: 

   ```batch 
docker-compose up -d
```
   Access the Apache Airflow web UI (localhost:8080) and run the DAG
   - Start Apache Spark

   ```batch 
spark-shell
```

   - Start Apache zookeeper

   ```batch 
zookeeper-server-start.bat C:/kafka_2.13_2.6.0/config/zookeeper.properties
```
   - Start Kafka server

   ```batch 
kafka-server-start.bat C:/kafka_2.13_2.6.0/config/server.properties
```

  - Run the kafka producer

   ```batch 
kafka-console-producer.bat --topic smartphoneTopic --bootstrap-server localhost:9092
```



