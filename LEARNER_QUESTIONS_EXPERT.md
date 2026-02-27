# Learner Questions (Expert Level, Evidence-Grounded)

## Evidence Snapshot From This Repo

This question set is grounded in high-frequency concepts found in:

- [sagemaker-dg-1000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-1000/document.md): Studio, IAM, Autopilot, JumpStart, endpoint basics
- [sagemaker-dg-2000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-2000/document.md): HyperPod-heavy operations, VPC/KMS/IAM integration
- [sagemaker-dg-3000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-3000/document.md): Ground Truth labeling + security-heavy patterns
- [sagemaker-dg-4000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-4000/document.md): Data Wrangler + Feature Store + lineage
- [sagemaker-dg-5000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-5000/document.md): Debugger, Profiler, distributed-training controls
- [sagemaker-dg-6000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-6000/document.md): Model/data parallelism + HyperPod + deployment crossover
- [sagemaker-dg-7000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-7000/document.md): Endpoint + Pipeline + shadow/multi-model endpoint depth
- [sagemaker-dg-8000](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-8000/document.md): Clarify, Model Monitor, drift, processing jobs
- [sagemaker-dg-8318](/private/tmp/aws-sgmkr-ml/output/sagemaker-dg-8318/document.md): Security and network architecture concentration
- [orchastrator](/private/tmp/aws-sgmkr-ml/output/orchastrator.md): ingestion integrity and dataset contracts

## Expert Answer Standard

For each answer, include:

1. Architecture decision.
2. Risk and failure mode.
3. Control/mitigation.
4. Measurable acceptance criterion.

## Section 1: Platform Architecture and Governance

1. Design a multi-account SageMaker operating model that separates experimentation, staging, and production while preserving artifact lineage end-to-end.
2. Define a governance boundary between platform-owned infrastructure and team-owned model assets. Which controls are mandatory at the boundary?
3. Propose an approval workflow that balances release velocity with compliance requirements for regulated ML workloads.
4. What architectural signals tell you your current SageMaker setup has become “platform debt” instead of “productivity infrastructure”?
5. How would you redesign your operating model if one business unit requires strict data residency while others do not?
6. What is your escalation policy when platform guardrails conflict with model team delivery deadlines?
7. Which policies should be global by default and which should be delegated to domain teams?
8. Build a decision matrix for when to centralize vs federate MLOps ownership.

## Section 2: Studio, Autopilot, and JumpStart at Scale

1. When is Studio the right system-of-engagement, and when should teams be forced into pipeline-only workflows?
2. How would you constrain Autopilot usage to avoid unmanaged cost growth while still enabling rapid prototyping?
3. Create a promotion path from JumpStart prototype to production model with security and reproducibility gates.
4. What anti-patterns in Studio usage predict future production incidents?
5. How would you enforce environment consistency across Studio users without blocking custom experimentation?
6. Which IAM and network controls are non-negotiable for shared Studio domains?
7. Propose a scorecard for “prototype quality” before a team can request production deployment.
8. How do you prevent shadow MLOps workflows from emerging around Studio notebooks?

## Section 3: Data Quality, Labeling, and Ground Truth

1. Design a Ground Truth QA framework that detects annotation policy drift before it reaches model training.
2. How would you quantify the marginal business value of improved annotation quality?
3. Which label quality metrics should block training and which should only warn?
4. Propose a migration strategy when taxonomy changes invalidate historical labels.
5. How do you identify and mitigate annotator-induced bias in a multilingual dataset?
6. What lineage artifacts are required to reproduce a model trained with evolving labels?
7. How would you architect feedback loops from production errors back into relabeling priorities?
8. Define a rollback plan for a harmful labeling guideline update already propagated to production models.

## Section 4: Data Wrangler, Processing Jobs, and Feature Store

1. Decide which transformations belong in Data Wrangler flows vs reproducible processing code. What criterion do you use?
2. How do you guarantee point-in-time feature correctness across offline training and online inference?
3. Propose a feature schema-evolution policy that avoids breaking deployed models.
4. Which lineage metadata must be captured for every feature to pass an audit?
5. How do you validate that feature freshness SLOs match business latency requirements?
6. Design a strategy for feature backfills that minimizes both cost and data skew risk.
7. How would you test feature pipelines against silent null/scale/encoding regressions?
8. What governance model prevents duplicate feature definitions across teams?

## Section 5: Training System Design and Cost-Performance Tradeoffs

1. Build a decision tree for selecting built-in algorithms, framework containers, or custom containers.
2. How would you optimize training job configuration for reproducibility under strict cost ceilings?
3. Which three training metrics are the earliest reliable indicators of inevitable failure?
4. Define a checkpointing strategy for long-running jobs that balances recovery time and storage overhead.
5. How do you choose objective functions and evaluation metrics when business cost is asymmetric?
6. What safeguards prevent accidental overfitting during aggressive hyperparameter tuning?
7. How do you evaluate whether training-data growth is still yielding marginal model gains?
8. When do you terminate an experiment campaign as non-viable?

## Section 6: Debugger, Profiler, and Deep Performance Diagnostics

1. Design a Debugger rule pack for early detection of exploding gradients, dead layers, and stalled learning.
2. How would you integrate Profiler outputs into automated pipeline gates?
3. What telemetry distinguishes data-loading bottlenecks from compute bottlenecks?
4. How do you decide whether to optimize model architecture, data pipeline, or infrastructure first?
5. Build a postmortem template for failed high-cost training runs using Debugger/Profiler evidence.
6. Which runtime traces should be retained long-term versus summarized?
7. How do you validate that performance optimizations did not silently degrade model quality?
8. What “performance false positives” commonly mislead teams in distributed setups?

## Section 7: Distributed Training, HyperPod, and Parallelism Strategy

1. Create a framework for choosing data parallelism, model parallelism, or hybrid parallelism.
2. What signals show network topology is your dominant scaling limiter?
3. How do you define horizontal scaling efficiency targets for HyperPod clusters?
4. Which failure modes are unique to large cluster training compared with single-node jobs?
5. How do you tune communication/computation overlap to maximize throughput?
6. Propose a capacity planning model for recurring distributed workloads with variable demand.
7. What rollback strategy should exist when a cluster-level change degrades convergence?
8. How do you prove your parallel training setup is deterministic enough for audit needs?

## Section 8: Pipelines, Model Registry, and Promotion Controls

1. Architect a SageMaker Pipeline that enforces strict stage contracts between data prep, training, evaluation, and deployment.
2. What should constitute a “hard fail” in a model package approval gate?
3. How do you encode policy-as-code for deployment readiness without creating false blockers?
4. Design a registry versioning and deprecation strategy across many model families.
5. How would you handle emergency patches that bypass normal approval flow while preserving auditability?
6. Which lineage joins are necessary to answer “what code+data produced this endpoint artifact?”
7. How do you detect promotion churn caused by unstable validation metrics?
8. Propose a pipeline observability dashboard that lets executives and engineers share the same truth.

## Section 9: Endpoint Architecture and Inference Reliability

1. Build a decision matrix for real-time endpoints, async inference, serverless, and batch transform.
2. How do you detect whether latency regressions originate from model complexity, feature fetch, or infrastructure saturation?
3. Design autoscaling policies that avoid both cold-start pain and wasteful overprovisioning.
4. What controls make multi-model endpoints safe in mixed-criticality workloads?
5. How would you run shadow deployments and canary releases with objective rollback thresholds?
6. Define SLOs and error budgets for inference systems with heterogeneous traffic patterns.
7. How do you isolate noisy-neighbor effects across models sharing endpoint infrastructure?
8. What runbook steps should execute in the first 15 minutes of a severe endpoint incident?

## Section 10: Monitoring, Drift, and Explainability (Clarify/Model Monitor)

1. Design a drift monitoring strategy that distinguishes natural seasonality from harmful drift.
2. Which Clarify explainability outputs are decision-useful versus compliance-only?
3. How do you tie monitor alarms to retraining triggers without creating retrain storms?
4. What statistical thresholds should be adaptive vs fixed?
5. How do you validate monitoring quality itself (false-positive and false-negative rates)?
6. Propose an incident workflow for fairness regressions detected post-deployment.
7. How do you prioritize model updates when multiple monitors fire conflicting signals?
8. What evidence bundle should be generated automatically for each drift incident?

## Section 11: IAM, VPC, KMS, and Security Architecture

1. Design least-privilege IAM role segmentation for data scientists, pipelines, training jobs, and endpoints.
2. How do you verify that private subnet + VPC endpoint architecture truly blocks unintended egress?
3. Which KMS key boundaries are required between teams to satisfy separation-of-duties?
4. How do you prevent permissive IAM policies from accumulating over time?
5. What is your strategy for cross-account model deployment with cryptographic and policy controls?
6. How should short-lived credentials be handled for long-running jobs?
7. Define mandatory detective controls for policy drift and unauthorized role assumption.
8. Build an incident response sequence for leaked credentials tied to production endpoint roles.

## Section 12: Reliability Engineering and Failure Injection

1. What failure-injection experiments would you run quarterly for SageMaker pipelines and endpoints?
2. How do you quantify blast radius before enabling a new rollout strategy?
3. Which chaos tests are safe in staging but unsafe in production, and why?
4. Design recovery time objectives (RTO) and recovery point objectives (RPO) for model-serving systems.
5. How do you ensure retries do not create duplicate side effects in downstream systems?
6. What data integrity checks must run after partial pipeline failures?
7. How would you test rollback logic under simultaneous drift alarms and infrastructure errors?
8. Which “unknown unknowns” in MLOps deserve explicit simulation despite low probability?

## Section 13: Dataset and Retrieval Engineering (Repo-Specific)

1. Design a chunking policy over `document.md` that optimizes retrieval precision without losing diagram context.
2. How should diagram references be embedded or indexed for multimodal retrieval?
3. What is the best schema for joining text chunks to `manifest.json` image metadata at query time?
4. How do you detect duplicate or near-duplicate chunks across `1000..8000` sources?
5. Propose a benchmark suite for answer faithfulness using this repository’s extracted data.
6. How would you guard against hallucinated page/image references in downstream assistants?
7. What retrieval metrics should be monitored continuously as documents are reprocessed?
8. How do you design a backward-compatible re-index when extraction parameters change?

## Section 14: Executive Architecture Defense Questions

1. Defend your full SageMaker architecture to a panel of security, finance, and reliability stakeholders with conflicting priorities.
2. If your budget is cut by 50%, what three capabilities do you preserve at all costs and why?
3. If compliance requirements double, what immediate architectural changes are mandatory?
4. Which single dependency in your design represents the highest systemic risk, and how do you mitigate it?
5. What are the strongest arguments against your architecture, and what evidence would change your mind?
6. Define your “go/no-go” criteria for production launch in one page.
7. How do you prove long-term maintainability rather than short-term correctness?
8. What would have to be true for you to replace parts of SageMaker with custom platform components?
