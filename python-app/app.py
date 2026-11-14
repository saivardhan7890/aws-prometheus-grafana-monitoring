from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest
import time

app = Flask(__name__)

REQUESTS = Counter(
    'flask_requests_total',
    'Total Flask requests'
)

LATENCY = Histogram(
    'flask_request_duration_seconds',
    'Request duration'
)

@app.route('/')
def home():
    REQUESTS.inc()
    return "AWS Prometheus Grafana Monitoring Project Running!"

@app.route('/health')
def health():
    return {"status": "healthy"}

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)