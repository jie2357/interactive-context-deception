# Network Architecture

Version: 1.8

---

## Production Environment

The production environment consists of:

- Public Load Balancer
- Reverse Proxy (Nginx)
- Kubernetes Cluster
- PostgreSQL Database
- Internal Monitoring

---

## AWS Region

Primary Region

ap-east-1

Backup Region

ap-northeast-1

---

## Notes

Database servers are not directly accessible from the Internet.

Administrative access requires VPN authentication.

Infrastructure deployment is documented in:

wiki/Deployment.md