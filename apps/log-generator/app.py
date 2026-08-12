import logging
import random
import time
from flask import Flask, request, jsonify, abort
from prometheus_client import Counter, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST

app = Flask(__name__)
handler = logging.FileHandler('logs/app.log')
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)

HTTP_REQUESTS = Counter('http_requests_total', 'Total HTTP requests', ['method', 'code'])

@app.route("/")
def index():
    app.logger.info("index requested: path=/")
    HTTP_REQUESTS.labels(method='GET', code='200').inc()
    return "CRB Log Generator: OK\n"

@app.route("/login", methods=['POST'])
def login():
    data = request.form or request.json or {}
    user = data.get('username', 'anonymous')
    # simulate auth success/failure
    if random.random() < 0.2:
        app.logger.warning("failed login attempt username=%s", user)
        HTTP_REQUESTS.labels(method='POST', code='401').inc()
        return abort(401)
    app.logger.info("successful login username=%s", user)
    HTTP_REQUESTS.labels(method='POST', code='200').inc()
    return jsonify({"status": "ok", "user": user})

@app.route("/metrics")
def metrics():
    registry = CollectorRegistry()
    # We rely on global counters for simplicity - generate_latest uses the default registry.
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
