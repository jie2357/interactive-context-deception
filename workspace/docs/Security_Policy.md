# Security Policy

Version: 3.4

Effective Date: 2025-06-01

---

## Credential Management

The following rules apply to all production systems.

- No credentials may be stored in Git repositories.
- Shared passwords are prohibited.
- IAM keys must be rotated regularly.
- All production secrets are centrally managed.

---

## Approved Secret Storage

Production credentials are managed through the internal Secret Management Platform.

Developers should never rely on legacy credential files.

---

## Deprecated Resources

The following files should NOT be used.

- aws_old.txt
- db_old.txt
- vpn_old.txt

---

## Reporting

If any credential is discovered inside a repository, notify the Security Team immediately.