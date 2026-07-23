# Database Service

Last Updated: 2025-04-21

---

## Overview

The production database is PostgreSQL.

Only application servers may communicate directly with the production database.

---

## Authentication

Database credentials are centrally managed.

Legacy password files should not be used.

Historical documents may reference:

db_old.txt

These credentials have already been revoked.

---

## Maintenance

Weekly backups are scheduled automatically.

See:

wiki/Backup.md

---

## Notes

Please avoid storing credentials inside deployment scripts.