# Phase 11 — Production AI Systems

## Seven-dimension map

**WHAT:** a production AI system is a sociotechnical distributed system with probabilistic components. **WHY:** usefulness depends on quality, reliability, security, privacy, latency, cost, and recovery together. **WHEN:** apply system design whenever model output affects users or operations. **WHERE:** end to end, including feedback and governance. **WHO:** users, operators, domain owners, engineers, auditors, attackers, and upstream providers. **HOW:** define SLOs and threat models, make boundaries/versioning explicit, design degradation and rollback, evaluate offline and online, capacity plan, and run incidents. **FAILURE:** correlated provider failure, cascading timeouts, feedback corruption, cross-tenant leaks, data residency violations, unsafe automation, metric gaming, undetected quality regression, and unowned incidents.

## Exit gate

Write and defend a design doc under concrete traffic, risk, and budget constraints; execute load, dependency, security, and quality-regression drills; publish postmortems.

