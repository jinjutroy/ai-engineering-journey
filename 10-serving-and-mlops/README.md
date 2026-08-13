# Phase 10 — Serving and MLOps

## Seven-dimension map

**WHAT:** serving and MLOps make model behavior reproducible, deployable, observable, and maintainable. **WHY:** an offline artifact is not a reliable product. **WHEN:** apply lifecycle discipline from the first baseline; scale infrastructure only when measurements require it. **WHERE:** across data/version pipelines, registries, deployment, inference, and monitoring. **WHO:** training jobs produce artifacts; registries and deployment systems promote them; services consume them; SRE/ML teams operate them. **HOW:** version data/code/config/artifacts, test contracts, package immutably, load test, canary, monitor SLOs and quality, and retain rollback. **FAILURE:** skew, incompatible artifacts, cold starts, overload, retry storms, silent drift, missing lineage, alert fatigue, privacy-unsafe logs, and rollback that does not restore dependent assets.

## Exit gate

Ship a versioned service with reproducible build, schema validation, health/readiness, batch policy, load-test results, SLOs, metrics/traces, canary plan, and tested rollback.

