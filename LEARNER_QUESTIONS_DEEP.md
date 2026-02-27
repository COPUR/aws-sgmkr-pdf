# Learner Questions (Deep Understanding Edition)

## How To Use This Set

1. Answer each question with a concrete architecture or operational decision.
2. Include assumptions, risks, and measurable acceptance criteria.
3. When possible, reference relevant files in `output/` (`document.md`, `manifest.json`, `images/`).

## Deep Repo and Data-Orchestration Questions

1. If `manifest.json` and markdown image references diverge, what are the top three root causes and how would you detect each automatically?
2. Design a schema for `text_chunks.jsonl` that preserves source traceability, page lineage, and multimodal linkage for future model training.
3. What is the minimum metadata needed to make the dataset reproducible across machines and months later?
4. How would you version chunking logic so downstream embeddings can be re-indexed safely without silent corruption?
5. Propose a data contract for `output/<source>/` so ingestion fails fast on malformed packages.
6. How would you compute and monitor quality metrics for extracted diagrams (usefulness, uniqueness, clarity)?
7. If storage doubles every month, what retention policy would you implement without losing auditability?
8. How would you prove end-to-end provenance from a learner answer back to the original page and diagram?

## Deep SageMaker Platform Questions (1000/2000 Themes)

1. In what situations should you choose Studio spaces over isolated user profiles, and what are the operational tradeoffs?
2. How do you map team roles (DS, MLE, platform, security) to IAM boundaries with least privilege and minimal friction?
3. Propose an onboarding architecture that supports experimentation speed while enforcing network isolation controls.
4. When should a team move from ad hoc notebooks to managed pipelines, and what objective signals trigger that transition?
5. How would you design guardrails for Canvas users so they can experiment safely without creating governance gaps?
6. Define a cost-governance model for mixed notebook + managed job usage across multiple teams.
7. How do you prevent environment drift across Studio users while preserving flexibility for research?
8. What incident classes are unique to Studio-centric workflows versus CI/CD-centric workflows?

## Deep Labeling and Data Questions (3000 Theme)

1. How would you design a labeling QA process that catches annotation bias before training starts?
2. What metrics would indicate that label quality, not model architecture, is the current bottleneck?
3. How do you run safe taxonomy evolution when historical labels must remain usable?
4. When should you relabel data versus apply post-processing calibration on model outputs?
5. How would you detect silent label distribution shifts across data collection periods?
6. Design a reviewer assignment strategy that reduces confirmation bias in annotation pipelines.
7. What is your rollback strategy if a labeling guideline change degrades model performance?
8. How do you quantify business impact of improved labeling quality in a measurable way?

## Deep Feature Store and Data Engineering Questions (4000 Theme)

1. How would you enforce point-in-time correctness checks before feature materialization is approved?
2. What feature-lineage model best supports cross-team reuse and regulatory audits?
3. How do you decide which transformations belong in feature pipelines vs model code?
4. What stale-feature detection policy would you use for online inference with strict latency SLOs?
5. How would you design compatibility rules for feature schema evolution without breaking old models?
6. What backfill strategy minimizes cost while preserving training-serving consistency?
7. How do you benchmark feature store value versus maintaining feature logic in application code?
8. What failure domains should be isolated between feature ingestion, storage, and serving planes?

## Deep Training and Optimization Questions (5000/6000 Themes)

1. How would you build a training strategy that balances convergence speed, cost, and reproducibility?
2. Which training telemetry would you prioritize for early failure detection in long-running jobs?
3. How do you decide between built-in algorithms, framework containers, and custom containers for a new use case?
4. In distributed training, how do you identify whether scaling inefficiency is compute-bound, memory-bound, or network-bound?
5. What checkpointing design minimizes recovery time while controlling storage overhead?
6. How would you validate that gradient synchronization settings are not degrading final model quality?
7. What anti-patterns cause hidden cost blowups in hyperparameter tuning workflows?
8. How do you formalize promotion criteria from experiment to production-ready model artifact?

## Deep Deployment, Inference, and Pipeline Questions (7000/8000 Themes)

1. How would you design a pipeline gate that blocks deployment when data drift is likely but not yet severe?
2. What decision framework do you use to choose real-time inference, async inference, or batch transform?
3. How do you architect canary rollout with automated rollback based on both technical and business KPIs?
4. What controls ensure model package approval is not a manual bottleneck but still audit-compliant?
5. How do you separate model failure from feature failure during production incidents?
6. What observability model links pipeline events, endpoint behavior, and customer-facing impact?
7. How do you safely test infrastructure changes (instance class, autoscaling, networking) without confounding model evaluation?
8. What long-term maintenance strategy prevents pipeline sprawl and duplicated logic across teams?

## Deep Security, IAM, and Network Questions (8318 Theme)

1. Design an IAM strategy that supports least privilege while keeping emergency operations practical.
2. How would you validate that private-subnet endpoint architecture truly blocks unintended egress?
3. What key management and encryption boundaries are required for cross-account model sharing?
4. How should access review cadence differ for human users, CI roles, and service roles?
5. What threat model is most relevant for model artifacts, training data, and inference payloads?
6. How do you design detective controls for accidental policy over-permissioning?
7. What is your incident playbook for compromised credentials tied to training or endpoint roles?
8. How do you prove security posture to auditors using artifacts from this repo and SageMaker logs?

## Synthesis and Architecture Review Questions

1. Draw an end-to-end architecture for this repo’s extracted dataset powering a multimodal RAG assistant.
2. Identify the three highest-risk single points of failure in the current flow and propose mitigations.
3. What changes are required to make this pipeline production-grade for daily ingestion at scale?
4. How would you design objective acceptance tests for data quality, retrieval quality, and answer faithfulness?
5. Which components should be stateless vs stateful, and why?
6. What are the strongest arguments against your own proposed architecture, and how would you respond?
7. If budget is cut by 40%, what do you optimize first without destroying reliability?
8. If audit requirements double, what architectural improvements become mandatory immediately?
