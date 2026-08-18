# Resilience Tabletop — Fictional Service Disruption

## Scenario

A fictional organization discovers that its primary customer portal is unavailable during a peak business period. Monitoring shows degraded service health, but the cause is intentionally unspecified. The exercise focuses on governance, recovery, communication, and evidence—not on intrusion techniques.

## Objectives

- confirm incident-command roles;
- identify critical business dependencies;
- practice recovery-priority decisions;
- test internal/external communication ownership;
- document decision assumptions;
- verify recovery evidence before declaring restoration complete.

## Starting information

Use `datasets/sample_resilience_exercises.csv` as fictional supporting data.

## Discussion injects

1. The primary service remains unavailable after the first recovery attempt.
2. A dependent billing service reports partial degradation.
3. Executive leadership asks for an estimated business-impact range.
4. A communications draft is ready, but the facts are still incomplete.
5. A backup is available, but its most recent recovery test is older than policy expectations.
6. Service appears restored, but monitoring coverage is incomplete.

## Questions

- Who has authority to set recovery priorities?
- Which dependencies must be validated before restoration is announced?
- What evidence is required to support a recovery decision?
- What information should be withheld until verified?
- How should unresolved monitoring gaps affect the recovery declaration?
- What follow-up actions belong in the post-incident improvement plan?

## Outputs

Produce a fictional decision log, recovery checklist, communication timeline, evidence list, and improvement backlog.

## Safety boundary

This is a tabletop exercise. Do not attempt to reproduce outages, interfere with systems, disable controls, or access infrastructure without explicit authorization.
