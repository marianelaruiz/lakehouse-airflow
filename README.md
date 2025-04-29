# Apache Airflow & Spark

This repository is intended for orchestrating Spark applications using the Apache Airflow tool

## Table of Contents

1. [Technologies](#technologies)
2. [Install and Run](#install-and-run)
3. [Apache Airflow Webserver](#apache-airflow-webserver)
4. [Databricks Lakehouse Architecture](#databricks-lakehouse-architecture)

## 1. Technologies

A list of technologies used within the project:

* [Python](https://www.python.org): Version 3.12
* [Pyspark](https://spark.apache.org/docs/latest/api/python/index.html): Version 3.5.3
* [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html): Version 2.10.2

## 2. Install and Run

```bash
# Clone this repo
$ git clone https://github.com/marianelaruiz/lakehouse-airflow
# Enter the project folder
$ cd lakehouse-airflow
```

### Windows

```bash
# Create a virtual environment
$ python -m venv airflow_venv 

# Activate your virtual environment
$ airflow_venv\Scripts\activate


```

### MacOS & Linux

```bash
# Create a virtual environment
python3 -m venv airflow_venv # or virtualenv venv

# Activate your virtual environment
source airflow_venv/bin/activate

```
### Initial Setup and Initialize Airflow
   ```bash
  bash setup_airflow.sh
   ```

### Config and Run Apache Airflow
*Ensure that Apache Airflow is installed on your machine.*
Yo have two options:

1. **Create an Airflow User** *(optional)*:
   If you prefer to create a custom user:
   ```bash
   airflow users create \
       --username admin \
       --firstname Admin \
       --lastname User \
       --role Admin \
       --email admin@example.com
   ```

   ``` 
   cd airflow
   export AIRFLOW_HOME=$(pwd)   
   ```
   
   In a terminal:
   ```    
   airflow webserver --port 8080
    airflow scheduler
   ```
   In another terminal:
   ```    
   airflow scheduler
   ```

2. **Start Airflow** :
   For a quicker setup without creating a user, you can use the standalone mode:
   ```bash
   cd airflow
   export AIRFLOW_HOME=$(pwd)
   airflow standalone
   ```
   > This command starts both the Airflow webserver and scheduler, and automatically creates an admin user. The username and password will be displayed in the terminal.

**Access the Airflow UI**:
   Open the browser and navigate to `http://localhost:8080` to access the Airflow UI.

### 3. Apache Airflow Webserver

Webserver will start at: `http://127.0.0.1:8080`

From here, you can access the address above in your browser and log in. 

The first configuration of the web server should be to change the host in Airflow. To do this, go to Admin > Connections > Search for "spark_default" > Change the "Host" field from "yarn" to "local" and save.

Then, you can go to the "Search Dags" field and search for "nome_da_sua_dag". Click on the search result, and you will have access to the interface related to the created Airflow instance. You can execute it by clicking the "Trigger DAG" button in the upper right corner of the screen, where you can observe the execution order and whether the Spark applications were successful or not. You can verify this by looking in the repository for each of the bronze, silver, and gold folders, where a subfolder called `parquet` will be created.

## 4. Databricks Lakehouse Architecture

The Medallion Architecture is a data design pattern used to logically organize data in a lakehouse, aimed at progressively enhancing the structure and quality of data as it flows through each layer of the architecture. The layers include Bronze (raw data), Silver (cleaned and transformed data), and Gold (data ready for analysis).
