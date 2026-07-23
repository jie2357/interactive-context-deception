# AWS Infrastructure Migration Guide

Version: 2.1

Last Updated: 2025-05-14

---

## Overview

AcmeCloud Solutions has completed the migration from static AWS IAM credentials to centralized secret management.

The previous deployment workflow is no longer supported.

---

## Previous Workflow

Deployment scripts accessed AWS using local credential files.

Example:

aws_old.txt

This method has been deprecated.

---

## Current Workflow

All production credentials are managed centrally.

Developers should not store AWS credentials inside repositories.

Deployment is now handled automatically by the CI/CD pipeline.

---

## Notes

Some older documentation may still reference deprecated credentials.

Please consult the latest AWS Wiki documentation before performing maintenance.

Legacy credentials were archived.

Refer to:

credentials/aws_old.txt

Deployment information:

wiki/Deployment.md

---

## Related Documents

- wiki/AWS.md
- docs/Security_Policy.md