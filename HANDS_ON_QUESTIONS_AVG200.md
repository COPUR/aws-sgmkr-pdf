# Hands-On Questions (Average 200-Page Bands)

This set is derived from in-depth analysis of all core markdown files plus the three learner-question sets.

## Inputs Analyzed

- `README.md`
- `output/orchastrator.md`
- `output/sagemaker-dg-*/document.md` (all generated chunks)
- `ml-output/sagemaker-dg-8318/document.md`
- `LEARNER_QUESTIONS.md`
- `LEARNER_QUESTIONS_DEEP.md`
- `LEARNER_QUESTIONS_EXPERT.md`

## Analysis Method

1. Parsed page-level markdown sections using `## Page N` boundaries.
2. Grouped pages into average 200-page bands (last band may be smaller).
3. Scored each band across theme dictionaries aligned with learner/deep/expert question families.
4. Assigned a primary and secondary theme, then generated a practical hands-on challenge with concrete outputs.

## Dominant Themes by Source

| Source | Top Themes (Primary -> Secondary) |
|---|---|
| `sagemaker-dg-1000` | `studio_platform` (9512) -> `security_network` (2126) -> `training_optimization` (1018) |
| `sagemaker-dg-2000` | `distributed_hyperpod` (3888) -> `studio_platform` (3503) -> `security_network` (2815) |
| `sagemaker-dg-3000` | `data_labeling` (5027) -> `distributed_hyperpod` (3075) -> `security_network` (2851) |
| `sagemaker-dg-4000` | `feature_data_engineering` (4097) -> `security_network` (2856) -> `studio_platform` (1854) |
| `sagemaker-dg-5000` | `training_optimization` (7655) -> `studio_platform` (1065) -> `data_labeling` (909) |
| `sagemaker-dg-6000` | `training_optimization` (4268) -> `distributed_hyperpod` (3011) -> `deployment_inference` (1047) |
| `sagemaker-dg-7000` | `deployment_inference` (5468) -> `pipeline_registry` (4222) -> `security_network` (2466) |
| `sagemaker-dg-8000` | `security_network` (3427) -> `data_labeling` (2635) -> `monitoring_reliability` (2042) |
| `sagemaker-dg-8318` | `security_network` (2218) -> `deployment_inference` (1028) -> `training_optimization` (929) |

## Hands-On Questions by ~200-Page Segment

| Segment | Theme | Diagrams In Band | Hands-On Question | Required Deliverable |
|---|---|---:|---|---|
| `sagemaker-dg-1000:0001-0200` | `studio_platform` + `security_network` | 18 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit iam tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-1000:0201-0400` | `studio_platform` + `deployment_inference` | 19 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit endpoint tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-1000:0401-0600` | `studio_platform` + `security_network` | 14 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit iam tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-1000:0601-0800` | `studio_platform` + `security_network` | 7 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit iam tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-1000:0801-1000` | `studio_platform` + `security_network` | 15 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit iam tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-2000:0001-0200` | `studio_platform` + `security_network` | 21 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit iam tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-2000:0201-0400` | `studio_platform` + `data_labeling` | 45 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit ground truth tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-2000:0401-0600` | `studio_platform` + `security_network` | 14 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit iam tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-2000:0601-0800` | `distributed_hyperpod` + `training_optimization` | 10 | Design a distributed training strategy for this segment. How will you choose parallelism mode, validate scaling efficiency, and harden recovery for cluster failures? Include an explicit training tradeoff analysis. | Parallelism decision tree + scaling KPI targets + checkpoint/recovery runbook. |
| `sagemaker-dg-2000:0801-1000` | `distributed_hyperpod` + `training_optimization` | 6 | Design a distributed training strategy for this segment. How will you choose parallelism mode, validate scaling efficiency, and harden recovery for cluster failures? Include an explicit training tradeoff analysis. | Parallelism decision tree + scaling KPI targets + checkpoint/recovery runbook. |
| `sagemaker-dg-2000:1001-1001` | `deployment_inference` + `studio_platform` | 0 | Design an inference deployment plan using this range. How will you choose endpoint mode, rollout safely, and enforce latency/SLO targets? Include an explicit studio tradeoff analysis. | Deployment strategy doc + canary/shadow rollout plan + SLO/rollback thresholds. |
| `sagemaker-dg-3000:0001-0200` | `distributed_hyperpod` + `studio_platform` | 8 | Design a distributed training strategy for this segment. How will you choose parallelism mode, validate scaling efficiency, and harden recovery for cluster failures? Include an explicit studio tradeoff analysis. | Parallelism decision tree + scaling KPI targets + checkpoint/recovery runbook. |
| `sagemaker-dg-3000:0201-0400` | `distributed_hyperpod` + `security_network` | 0 | Design a distributed training strategy for this segment. How will you choose parallelism mode, validate scaling efficiency, and harden recovery for cluster failures? Include an explicit iam tradeoff analysis. | Parallelism decision tree + scaling KPI targets + checkpoint/recovery runbook. |
| `sagemaker-dg-3000:0401-0600` | `data_labeling` + `security_network` | 10 | Design and run a labeling/data-quality workflow for this range. How will you define labeling policy, quality gates, and relabel triggers tied to measurable model impact? Include an explicit iam tradeoff analysis. | Labeling SOP + QA metrics spec + relabel decision playbook. |
| `sagemaker-dg-3000:0601-0800` | `data_labeling` + `security_network` | 34 | Design and run a labeling/data-quality workflow for this range. How will you define labeling policy, quality gates, and relabel triggers tied to measurable model impact? Include an explicit iam tradeoff analysis. | Labeling SOP + QA metrics spec + relabel decision playbook. |
| `sagemaker-dg-3000:0801-1000` | `data_labeling` + `security_network` | 5 | Design and run a labeling/data-quality workflow for this range. How will you define labeling policy, quality gates, and relabel triggers tied to measurable model impact? Include an explicit iam tradeoff analysis. | Labeling SOP + QA metrics spec + relabel decision playbook. |
| `sagemaker-dg-3000:1001-1001` | `security_network` + `data_labeling` | 0 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit ground truth tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |
| `sagemaker-dg-4000:0001-0200` | `data_labeling` + `security_network` | 14 | Design and run a labeling/data-quality workflow for this range. How will you define labeling policy, quality gates, and relabel triggers tied to measurable model impact? Include an explicit iam tradeoff analysis. | Labeling SOP + QA metrics spec + relabel decision playbook. |
| `sagemaker-dg-4000:0201-0400` | `security_network` + `studio_platform` | 9 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit studio tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |
| `sagemaker-dg-4000:0401-0600` | `security_network` + `studio_platform` | 44 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit studio tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |
| `sagemaker-dg-4000:0601-0800` | `feature_data_engineering` + `security_network` | 34 | Implement a feature engineering plan for this range. How will you guarantee point-in-time correctness, schema evolution safety, and feature lineage for audits? Include an explicit iam tradeoff analysis. | Feature contract + transformation DAG + lineage and backfill policy. |
| `sagemaker-dg-4000:0801-1000` | `feature_data_engineering` + `training_optimization` | 17 | Implement a feature engineering plan for this range. How will you guarantee point-in-time correctness, schema evolution safety, and feature lineage for audits? Include an explicit training tradeoff analysis. | Feature contract + transformation DAG + lineage and backfill policy. |
| `sagemaker-dg-4000:1001-1001` | `training_optimization` + `studio_platform` | 0 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit studio tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-5000:0001-0200` | `training_optimization` + `data_labeling` | 3 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit ground truth tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-5000:0201-0400` | `training_optimization` + `data_labeling` | 7 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit ground truth tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-5000:0401-0600` | `training_optimization` + `security_network` | 19 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit iam tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-5000:0601-0800` | `training_optimization` + `studio_platform` | 39 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit studio tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-5000:0801-1000` | `training_optimization` + `distributed_hyperpod` | 33 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit hyperpod tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-5000:1001-1001` | `distributed_hyperpod` + `pipeline_registry` | 0 | Design a distributed training strategy for this segment. How will you choose parallelism mode, validate scaling efficiency, and harden recovery for cluster failures? Include an explicit pipeline tradeoff analysis. | Parallelism decision tree + scaling KPI targets + checkpoint/recovery runbook. |
| `sagemaker-dg-6000:0001-0200` | `distributed_hyperpod` + `training_optimization` | 9 | Design a distributed training strategy for this segment. How will you choose parallelism mode, validate scaling efficiency, and harden recovery for cluster failures? Include an explicit training tradeoff analysis. | Parallelism decision tree + scaling KPI targets + checkpoint/recovery runbook. |
| `sagemaker-dg-6000:0201-0400` | `training_optimization` + `distributed_hyperpod` | 9 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit hyperpod tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-6000:0401-0600` | `training_optimization` + `security_network` | 3 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit iam tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-6000:0601-0800` | `training_optimization` + `distributed_hyperpod` | 2 | Create a training optimization experiment from this range. How will you choose baselines, tune hyperparameters, detect failure early, and enforce reproducibility? Include an explicit hyperpod tradeoff analysis. | Experiment matrix + failure gates + reproducibility checklist. |
| `sagemaker-dg-6000:0801-1000` | `deployment_inference` + `security_network` | 39 | Design an inference deployment plan using this range. How will you choose endpoint mode, rollout safely, and enforce latency/SLO targets? Include an explicit iam tradeoff analysis. | Deployment strategy doc + canary/shadow rollout plan + SLO/rollback thresholds. |
| `sagemaker-dg-6000:1001-1001` | `deployment_inference` + `monitoring_reliability` | 0 | Design an inference deployment plan using this range. How will you choose endpoint mode, rollout safely, and enforce latency/SLO targets? Include an explicit model monitor tradeoff analysis. | Deployment strategy doc + canary/shadow rollout plan + SLO/rollback thresholds. |
| `sagemaker-dg-7000:0001-0200` | `deployment_inference` + `security_network` | 27 | Design an inference deployment plan using this range. How will you choose endpoint mode, rollout safely, and enforce latency/SLO targets? Include an explicit iam tradeoff analysis. | Deployment strategy doc + canary/shadow rollout plan + SLO/rollback thresholds. |
| `sagemaker-dg-7000:0201-0400` | `deployment_inference` + `security_network` | 15 | Design an inference deployment plan using this range. How will you choose endpoint mode, rollout safely, and enforce latency/SLO targets? Include an explicit iam tradeoff analysis. | Deployment strategy doc + canary/shadow rollout plan + SLO/rollback thresholds. |
| `sagemaker-dg-7000:0401-0600` | `deployment_inference` + `security_network` | 24 | Design an inference deployment plan using this range. How will you choose endpoint mode, rollout safely, and enforce latency/SLO targets? Include an explicit iam tradeoff analysis. | Deployment strategy doc + canary/shadow rollout plan + SLO/rollback thresholds. |
| `sagemaker-dg-7000:0601-0800` | `pipeline_registry` + `deployment_inference` | 14 | Build a production pipeline design for this range. What stage contracts and approval gates will you enforce before promotion? Include an explicit endpoint tradeoff analysis. | Pipeline DAG + promotion gate policy + artifact lineage map. |
| `sagemaker-dg-7000:0801-1000` | `studio_platform` + `pipeline_registry` | 3 | Build a SageMaker Studio operating design for this page range. How will you structure domains, user profiles, spaces, and guardrails so teams can ship quickly without breaking governance? Include an explicit pipeline tradeoff analysis. | Studio architecture diagram + IAM boundary matrix + onboarding checklist. |
| `sagemaker-dg-7000:1001-1001` | `pipeline_registry` + `deployment_inference` | 0 | Build a production pipeline design for this range. What stage contracts and approval gates will you enforce before promotion? Include an explicit endpoint tradeoff analysis. | Pipeline DAG + promotion gate policy + artifact lineage map. |
| `sagemaker-dg-8000:0001-0200` | `monitoring_reliability` + `pipeline_registry` | 14 | Build a production monitoring and incident response design for this range. How will you detect drift, triage alerts, and trigger safe retraining? Include an explicit pipeline tradeoff analysis. | Monitoring spec + alert severity matrix + incident and retraining workflow. |
| `sagemaker-dg-8000:0201-0400` | `data_labeling` + `monitoring_reliability` | 5 | Design and run a labeling/data-quality workflow for this range. How will you define labeling policy, quality gates, and relabel triggers tied to measurable model impact? Include an explicit model monitor tradeoff analysis. | Labeling SOP + QA metrics spec + relabel decision playbook. |
| `sagemaker-dg-8000:0401-0600` | `data_labeling` + `feature_data_engineering` | 6 | Design and run a labeling/data-quality workflow for this range. How will you define labeling policy, quality gates, and relabel triggers tied to measurable model impact? Include an explicit feature store tradeoff analysis. | Labeling SOP + QA metrics spec + relabel decision playbook. |
| `sagemaker-dg-8000:0601-0800` | `security_network` + `training_optimization` | 3 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit training tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |
| `sagemaker-dg-8000:0801-1000` | `security_network` + `studio_platform` | 0 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit studio tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |
| `sagemaker-dg-8000:1001-1001` | `security_network` + `studio_platform` | 0 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit studio tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |
| `sagemaker-dg-8318:0001-0200` | `security_network` + `deployment_inference` | 10 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit endpoint tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |
| `sagemaker-dg-8318:0201-0319` | `security_network` + `training_optimization` | 1 | Design a security control plane for this page range. How will you enforce least privilege, key management, and network isolation while keeping operations practical? Include an explicit training tradeoff analysis. | IAM role model + VPC/KMS architecture + access review and incident checklist. |

## Totals

- Total segments: **49**
- Approx pages covered: **8326**
- Theme distribution across segments:
  - `studio_platform`: 9
  - `training_optimization`: 9
  - `security_network`: 8
  - `distributed_hyperpod`: 6
  - `deployment_inference`: 6
  - `data_labeling`: 6
  - `feature_data_engineering`: 2
  - `pipeline_registry`: 2
  - `monitoring_reliability`: 1

## Suggested Usage

1. Complete one segment challenge per study session.
2. For each answer, include architecture diagram, decision rationale, and rollback plan.
3. Validate answers against exact page ranges in the referenced segment ID.
