# app.py
import random
import time
from flask import Flask, Response
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

# DEFINE METRICS
# These are the variables Prometheus will track.
# Gauges are typically used for measured values like temperatures or current memory usage, but also "counts" that can go up and down, like the number of concurrent requests.
# tldr: Gauge is a number that can go up and down (like a price).
EGG_PRICE = Gauge('grocery_price_eggs', 'Current price of a dozen eggs in USD')
WATERLOO_PRICE = Gauge('grocery_price_waterloo', 'Current price of Waterloo Sparkling Water')
BED_ROT_LEVEL = Gauge('personal_bed_rot_index', 'Subjective energy level (0-100)')

# THE "SCRAPER" LOGIC
def update_metrics():
    """
    In a real app, one would use requests.get() and BeautifulSoup here.
    For this MVP, just simulate market volatility.
    """
    # Simulate Eggs fluctuating between $3.00 and $5.00
    current_egg_price = round(random.uniform(3.0, 5.0), 2)
    EGG_PRICE.set(current_egg_price)
    
    # Simulate Waterloo finding a deal (sometimes it drops to $0.49!)
    current_waterloo = 0.49 if random.random() < 0.1 else 3.99
    WATERLOO_PRICE.set(current_waterloo)

    # Simulate energy levels (Bed Rot)
    BED_ROT_LEVEL.set(random.randint(20, 90))

#  THE ENDPOINT
@app.route('/metrics')
def metrics():
    # Update the data right before Prometheus scrapes
    update_metrics()
    # Return the data in the format Prometheus understands
    return Response(generate_latest(), mimetype='text/plain')

@app.route('/')
def home():
    return "<h1>The Inflation Dashboard is Running. Go to /metrics to see the raw data.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)