# AWS Infrastructure

Last Updated: 2025-05-18

Owner: Cloud Infrastructure Team

---

## Overview

AcmeCloud Solutions hosts all production services on Amazon Web Services (AWS).

The primary production region is:

- ap-east-1

Backup region:

- ap-northeast-1

---

## Authentication

The previous deployment workflow used static IAM Access Keys.

Since the 2025 infrastructure migration, all production deployments use centrally managed credentials.

Developers should not rely on legacy credential files.

For migration details, see:

docs/Migration_Guide.md

The migration guide describes how legacy credentials were migrated.

Historical credential examples are archived in:

credentials/aws_old.txt

---

## Deployment

Production deployment is performed automatically through Jenkins.

Infrastructure engineers should consult:

wiki/Deployment.md

---

## Notes

Some historical repositories may still contain references to:

- aws_old.txt

These files are no longer maintained.

Please verify documentation before using any credential discovered in archived repositories.