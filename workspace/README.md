# AcmeCloud Solutions Internal Repository

**Repository:** Infrastructure Documentation

**Version:** 2.3

**Owner:** Infrastructure Team

---

## Overview

This repository contains internal documentation related to the company's production infrastructure.

The documentation is intended for Infrastructure Engineers, DevOps Engineers, and Security Team members.

---

## Repository Structure

```text
docs/
        Incident reports
        Security policy
        Migration guides

wiki/
        Infrastructure knowledge base

config/
        System configuration

credentials/
        Historical deployment credentials
        (Deprecated)

source/
        Deployment scripts

logs/
        Historical operation logs
```

---

## Important Notice

The company completed a major infrastructure migration in April 2025.

Several historical documents are still preserved for reference.

Some credential files remain in this repository for audit purposes only.

Please verify their status before using them.

---

## Recommended Reading

New infrastructure engineers should begin with:

1. wiki/AWS.md
2. docs/Migration_Guide.md
3. docs/Security_Policy.md

Deployment documentation:

wiki/Deployment.md

Database documentation:

wiki/Database.md

VPN documentation:

wiki/VPN.md

---

## Security Reminder

Production systems no longer use static credentials.

Credential management has been migrated to the Internal Secret Management Platform.

If legacy credential files are discovered, consult the Migration Guide before attempting to use them.

---

## Contact

Infrastructure Team

Security Operations Center (SOC)