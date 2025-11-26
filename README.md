# The Inflation Dashboard
A containerized microservices observability stack designed to ingest, monitor, and visualize real-time economic volatility and personal health metrics.
Tools: **Python (Flask)**, **Docker**, **Prometheus**, and **Grafana**.

## How to install and run:
### **Local**
```
cd app/
python3 -m venv venv
pip install -r requirements.txt
python src/app.py
```

### **Docker**

Build docker image using the DockerFile: `docker build -t inflation-dashboard-app .`

The flask app uses port 5050: `docker run -p 5050:5050 inflation-dashboard-app`

## Disclaimer:
All the data are fake. 