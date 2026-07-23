# Incident Report

**Incident ID:** INC-2025-0142

**Date:** 2025-06-28

**Severity:** Medium

**Reported by:** Security Operations Center (SOC)

---

## Summary

During a scheduled security audit, an outdated AWS IAM Access Key was discovered in an internal deployment repository.

Although the credential had already been revoked, the repository still contained references to the legacy deployment process.

No evidence of unauthorized access was found.

---

## Root Cause

The deployment team completed the AWS credential migration in April 2025.

Several internal documents were not updated after the migration.

Some repositories still referenced deprecated deployment procedures.

---

## Impact

- No production systems affected.
- No customer data exposed.
- Documentation inconsistency detected.

---

## Resolution

- Removed legacy deployment scripts.
- Revoked all historical IAM keys.
- Updated Security Policy.
- Updated Migration Guide.

---

## References

- docs/Migration_Guide.md
- docs/Security_Policy.md
- wiki/AWS.md