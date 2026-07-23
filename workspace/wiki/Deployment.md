# Deployment Workflow

Version: 2.4

---

## Overview

Application deployment is fully automated.

Manual deployment is discouraged.

---

## Deployment Pipeline

Developer

↓

GitHub

↓

Jenkins

↓

Docker Build

↓

Kubernetes Cluster

---

## Secrets

Deployment credentials are injected during runtime.

Credential storage has been migrated away from repository-based configuration.

---

## Legacy Documentation

Older deployment scripts may reference deprecated AWS credentials.

See:

docs/Incident_Report.md

---

## Related Documents

wiki/AWS.md

config/docker-compose.yml

config/aws.conf