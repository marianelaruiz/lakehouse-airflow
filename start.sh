#!/bin/bash

DIR="$(pwd)"

export AIRFLOW_HOME="$DIR"

airflow webserver --port 8080
airflow standalone ?