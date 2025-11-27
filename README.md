# The Inflation Dashboard
A containerized microservices observability stack designed to ingest, monitor, and visualize real-time economic volatility and personal health metrics.
Tools: **Python (Flask)**, **Docker**, **Prometheus**, and **Grafana**.

## Overview
This system treats economic data (e.g., egg prices) and personal biometrics ("Bed Rot" Index) as a distributed systems monitoring problem.

It deploys a self-contained microservices ecosystem that:
1. simulates the economic data and personal biometrics via a Python application, 
2. exposes metrics via a Prometheus compatible endpoint, 
3. aggregates data into Prometheus,
3. and provides a Grafana dashboard

## Architecture

The system is composed of three decoupled services orchestrated via Docker Compose:

 Technology | Port | Role |
 --- | --- | --- |
 Python | `5050` | Simulates price fluctuations for staples (Eggs, Waterloo Water) and exposes metrics |
Prometheus | `9010` | Scrapes the simulator every 5 seconds to build a time-series history |
 Grafana | `3000` | Queries Prometheus and renders real-time dashboards |

## How to install and run:
`docker-compose up --build`

### **To run the Flask app locally**
```
cd app/
python3 -m venv venv
pip install -r requirements.txt
python src/app.py
```

### **Docker**

Build docker image using the DockerFile: `docker build -t inflation-dashboard-app .`

The flask app uses port 5050: `docker run -p 5050:5050 inflation-dashboard-app`


## The Prometheus interface
To query all metrics: `{__name__=~".+"}`

## Disclaimer:
All the data are fake.

Web scrapers are left for future work :D