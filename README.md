# CRB is an observability / security telemetry MVP combining:
- Prometheus (metrics)
- Grafana (dashboards & alerting)
- Loki + Promtail (log aggregation)
- Suricata (network IDS) — optional in CI/local since it requires host-level packet capture privileges
- Demo web app that emits logs and Prometheus metrics
- GitHub Actions CI to run linting and a smoke test

Goals
- Fast local developer onboarding via `docker-compose up`
- Real metrics + logs + basic IDS telemetry for alerts and dashboards
- CI smoke tests to validate end-to-end flow

Quickstart (locally)
1. Clone repo and enter directory
   git clone <your-repo-url> && cd CRB

2. Build the demo app and bring up services
   docker-compose build
   docker-compose up -d

3. Open services
   - Grafana: http://localhost:3000 (admin/admin)
   - Prometheus: http://localhost:9090
   - Loki: http://localhost:3100
   - Demo app: http://localhost:8000

4. Generate traffic to see logs & metrics:
   ./scripts/generate-traffic.sh

5. View the provisioned Grafana dashboard (CRB Overview).

Notes & design decisions
- Logs: Loki + Promtail were chosen for a simpler, lower-ops log pipeline than a full ELK stack for an MVP.
- Metrics: Prometheus scrapes the demo application directly.
- Suricata is included for network IDS telemetry; running Suricata in Docker with host network and privileges is platform dependent — see the Suricata section in docs/.
- Wazuh and ELK are powerful but heavier to operate. The README includes instructions to add them as a second stage. If you want, I will add a complete docker-compose + configuration for Wazuh + Elasticsearch + Kibana in a follow-up.

CI
- .github/workflows/ci.yml lints Python code, runs docker-compose up in GitHub Actions (no secrets required), and runs a pytest smoke test that verifies /metrics and log ingestion.

License
- MIT (see LICENSE)

Next improvements (phase 2)
- Wazuh + Elasticsearch + Kibana integration
- Hardened production configs (TLS, auth, resource limits)
- Helm charts / k8s manifests
- Long-term storage for Prometheus (Thanos / Cortex) and Loki retention policy

If you want, I can now:
- Provide a zip of these files
- Generate Helm manifests + k8s production manifests
- Add Wazuh/ELK full integration in the same repo (requires more resources & testing)

