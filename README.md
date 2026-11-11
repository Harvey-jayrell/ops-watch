# ops-watch

Scheduled health checks, state-change alerts, and verified Postgres backups for a live Render service.

> **Status:** V1 in development. Nothing here is built yet.

## Why

Building a service shows I can write an API. Operating one shows I can keep it running. `ops-watch` monitors and backs up a real, public service I own (the [Business Finance Tracker](https://business-finance-tracker.onrender.com)), so every alert and restore in this repo is real.

Everything runs on free tiers. No VPS, no paid services.

## V1 scope

1. **Check** the live API's `/api/health` on a schedule and record status code, response time and database status.
2. **Alert** on state changes only (healthy to failing, failing back to healthy), not on every failed check.
3. **Back up** the Supabase Postgres database on a schedule to storage outside git.
4. **Verify** each backup by restoring it into a throwaway local Postgres and checking row counts.

## Out of scope for V1

Dashboards, multi-service monitoring, retention policies beyond "keep last N", auto-remediation, Terraform.

## Planned stack

Python, GitHub Actions (scheduled), Docker, pytest.

## Setup, architecture and evidence

Coming as the project is built: architecture diagram, setup steps, and screenshots of a real alert and a real restore.
