import requests
import time

def test_metrics_endpoint():
    r = requests.get("http://localhost:8000/metrics", timeout=5)
    assert r.status_code == 200
    assert "http_requests_total" in r.text

def test_grafana_up():
    # wait for services to settle a bit
    time.sleep(5)
    r = requests.get("http://localhost:3000/api/health", timeout=5)
    assert r.status_code == 200
    assert r.json().get("database") == "ok"
