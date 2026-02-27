# Learner Questions (From All Markdown Files)

## Scope Analyzed

- `README.md`
- `output/orchastrator.md`
- `output/sagemaker-dg-1000/document.md`
- `output/sagemaker-dg-2000/document.md`
- `output/sagemaker-dg-3000/document.md`
- `output/sagemaker-dg-4000/document.md`
- `output/sagemaker-dg-5000/document.md`
- `output/sagemaker-dg-6000/document.md`
- `output/sagemaker-dg-7000/document.md`
- `output/sagemaker-dg-8000/document.md`
- `output/sagemaker-dg-8318/document.md`
- `ml-output/sagemaker-dg-8318/document.md` (same topic family, alternate output path)

## Repo Workflow Questions (README + Orchestrator)

1. Why does the repo keep PDF sources local instead of committing them?
2. What are the roles of `document.md`, `manifest.json`, and `images/` in each output package?
3. How does `output/pictures/<source>/` differ from `output/<source>/images/`?
4. Which integrity checks should pass before loading this data into a RAG pipeline?
5. Why is `source + page` a strong primary key for retrieval use cases?
6. What metadata would you add to `manifest.json` to improve traceability for ML experiments?
7. How do worker count, chunk size, and image DPI affect runtime and output quality?
8. If image count and markdown image references mismatch, what is your debugging sequence?

## SageMaker Foundation Questions (1000 Chunk)

1. What is the relationship between SageMaker Studio, domains, users, and spaces?
2. How do notebook instance choices affect performance, cost, and security posture?
3. When would you isolate development in a VPC-only Studio setup?
4. What are the key onboarding steps for a new data scientist in SageMaker Studio?
5. How do IAM permissions shape what a Studio user can create or deploy?
6. What governance controls should be applied before enabling shared Studio environments?
7. What is the difference between interactive experimentation and managed training jobs?
8. How would you document a standard “first-day” workflow for a new ML team member?

## Data, Canvas, and Cluster Questions (2000 Chunk)

1. How would you decide between SageMaker Canvas and code-first workflows?
2. What data quality checks are mandatory before model training begins?
3. How should dataset versioning be handled across repeated experiments?
4. What are the operational risks of running large HyperPod/cluster workloads?
5. How do you right-size compute for data prep versus model training?
6. What metrics indicate that data preprocessing is a pipeline bottleneck?
7. How would you partition training/validation/test datasets for regulated workloads?
8. What reproducibility metadata should be captured for each data-to-model run?

## Labeling and Data Versioning Questions (3000 Chunk)

1. How do you design a labeling job with clear instructions and quality control?
2. What are the tradeoffs between human labeling, active learning, and weak supervision?
3. How would you measure inter-annotator agreement and act on low agreement scores?
4. What versioning strategy prevents label drift from silently degrading models?
5. How do you audit labeling changes across project iterations?
6. When should you relabel versus retrain with existing labels?
7. How do taxonomy changes impact backward compatibility of labeled datasets?
8. What safeguards reduce bias introduced during annotation?

## Feature Engineering and Feature Store Questions (4000 Chunk)

1. Why separate online and offline feature stores, and when do you need both?
2. How do you guarantee point-in-time correctness for training features?
3. What schema and naming conventions make feature reuse easier across teams?
4. How do you detect and handle feature freshness issues in production?
5. Which feature lineage metadata is required for compliance audits?
6. How should feature transformations be tested before promotion?
7. What rollback strategy is needed for broken feature pipelines?
8. How do you balance feature richness with model latency constraints?

## Training and Debugger Questions (5000 Chunk)

1. How do managed training jobs differ from custom training container workflows?
2. Which hyperparameters should be tuned first for a baseline model?
3. How do SageMaker Debugger rules help detect overfitting or vanishing gradients?
4. What metrics should gate model promotion to staging?
5. How do you compare built-in algorithms with framework-based custom training?
6. What cost controls are most effective during large hyperparameter searches?
7. How should failed training jobs be triaged and categorized?
8. What artifacts must be preserved for reproducible retraining?

## Distributed Training Questions (6000 Chunk)

1. When should you use data parallelism vs model parallelism?
2. How do cluster topology and network bandwidth impact distributed training performance?
3. Which indicators show that communication overhead dominates training time?
4. How do you tune batch size, gradient accumulation, and checkpoint cadence together?
5. What fault-tolerance design is needed for long-running distributed jobs?
6. How do you validate numerical stability at scale across multiple nodes?
7. What logging/observability signals are mandatory for distributed debugging?
8. How do you choose instance families for memory-bound vs compute-bound models?

## Pipelines, Endpoints, and Inference Questions (7000 Chunk)

1. How should SageMaker Pipelines stages be structured for reliable CI/CD?
2. What criteria determine whether to deploy a real-time endpoint or a batch transform job?
3. How do you design rollback-safe endpoint update strategies?
4. Which pre-deployment checks should block endpoint promotion?
5. How do you define and enforce model package approval workflows?
6. What monitoring signals indicate inference drift or degradation?
7. How do you handle feature and model version compatibility at inference time?
8. How would you test latency and throughput objectives before production launch?

## Advanced Operations Questions (8000 Chunk)

1. How do you operationalize repeated training and deployment jobs across teams?
2. What runbook should exist for endpoint incidents and latency spikes?
3. How do you design canary and shadow testing for new model versions?
4. What SLOs are appropriate for training pipelines vs real-time inference services?
5. How should job orchestration handle retries, idempotency, and failure notifications?
6. What governance checks should run before any production model update?
7. How do you prioritize technical debt in long-lived ML platforms?
8. How do you measure business impact alongside model quality metrics?

## Security, IAM, and Networking Questions (8318 Chunk)

1. How do IAM policies constrain SageMaker training and deployment blast radius?
2. What is the security impact of running SageMaker in private subnets with VPC endpoints?
3. How do you enforce least privilege for data scientists versus platform engineers?
4. What encryption controls are needed for data at rest and in transit?
5. How should cross-account model deployment be secured and audited?
6. What network controls prevent unintended internet egress from workloads?
7. How do you design access reviews for roles used by pipelines and endpoints?
8. What incident response steps are specific to leaked model or training data access keys?

## Capstone Scenario Questions

1. Design an end-to-end SageMaker workflow for a regulated use case: where do you place data validation, labeling, training, approval, deployment, and monitoring gates?
2. Your model quality is high offline but fails in production. Which three root-cause categories do you investigate first and why?
3. Training costs doubled this month. Build a triage plan using evidence from data size, hyperparameters, infrastructure, and pipeline retries.
4. A security review rejects your deployment architecture. Redesign it using IAM least privilege, VPC isolation, and auditable artifact lineage.
5. You need multi-team feature reuse without breaking existing models. Propose a feature-store governance model.
6. An endpoint rollback is required after a bad release. What controls should have caught the issue earlier?
7. Distributed training is slower than expected. How do you determine if the bottleneck is compute, memory, or network?
8. A stakeholder asks for explainability and reproducibility proofs. Which artifacts from this repo and SageMaker workflows do you provide?
