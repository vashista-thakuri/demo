# demo-scan-repo

A tiny Python app used as a real (non-sandboxed) test target for the
remediation-agent's GitHub PR flow. It looks up a product by SKU against a
local SQLite database.

This app is **intentionally vulnerable** (SQL injection in `src/products.py`)
so the remediation pipeline has a real finding to analyze and fix. It is not
meant to be run outside this demo.

## Layout

- `src/database.py` — SQLite connection + schema/seed data
- `src/products.py` — product lookup (contains the vulnerability)
- `src/app.py` — thin CLI entry point
- `tests/test_products.py` — existing happy-path tests

## Run

```
python -m src.app SKU-100
python -m pytest
```
