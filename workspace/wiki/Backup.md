# Backup Policy

Version: 1.5

---

## Schedule

Production databases are backed up every day at 02:00 UTC.

---

## Storage

Backups are encrypted before upload.

---

## Recovery

Recovery procedures are documented internally.

Only Infrastructure Team members may perform production restores.

---

## Notes

Backup scripts are located in:

source/backup.sh