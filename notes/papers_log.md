# Papers Log

This file is the working notebook for medicine-related ML papers relevant to Vivral.

Format for each entry:

## `YYYY-MM-DD` - Title
- Link:
- Why it matters:
- Method:
- Dataset(s):
- Notes:
- Follow-up references:

## 2026-05-26 - Large Language Models Encode Clinical Knowledge
- Link: https://arxiv.org/abs/2212.13138
- Why it matters: Core MultiMedQA paper; establishes the benchmark mix that is still useful for SFT and eval curation.
- Method: PaLM / Flan-PaLM / Med-PaLM prompting plus instruction tuning.
- Dataset(s): MedQA, MedMCQA, PubMedQA, MMLU clinical topics, HealthSearchQA.
- Notes: Strong source for what "medical competence" data looks like in practice; follow references into human eval design and long-form answer quality.
- Follow-up references: MultiMedQA, HealthSearchQA.

## 2026-05-26 - Towards Expert-Level Medical Question Answering with Large Language Models
- Link: https://arxiv.org/abs/2305.09617
- Why it matters: Med-PaLM 2 paper; shows the jump from broad medical QA to clinician-preferred long-form answers.
- Method: Medical domain finetuning, prompting, ensemble refinement.
- Dataset(s): MedQA, MedMCQA, PubMedQA, consumer medical QA, adversarial long-form questions.
- Notes: Useful for SFT data shaping around factuality, utility, and harm avoidance.
- Follow-up references: clinician evaluation rubrics, adversarial question set.

## 2026-05-26 - PubMedQA: A Dataset for Biomedical Research Question Answering
- Link: https://arxiv.org/abs/1909.06146
- Why it matters: Research-abstract QA with long-answer rationales; good fit for literature-grounded SFT.
- Method: Biomedical QA over abstracts with yes/no/maybe labels and long answers.
- Dataset(s): PQA-L, PQA-U, PQA-A.
- Notes: Good candidate for extracting instruction-response pairs from biomedical evidence summaries.
- Follow-up references: PubMedQA site and GitHub repo.

## 2026-05-26 - MedMCQA: A Large-scale Multi-Subject Multi-Choice Dataset for Medical domain Question Answering
- Link: https://arxiv.org/abs/2203.14371
- Why it matters: Large exam-style QA set with broad coverage across medical subjects.
- Method: Multiple-choice medical QA benchmark.
- Dataset(s): 194k+ MCQs from AIIMS/NEET PG-style exams.
- Notes: High-value for classification-style SFT and benchmark-style instruction tuning.
- Follow-up references: official MedMCQA repository.

## 2026-05-26 - What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams
- Link: https://arxiv.org/abs/2009.13081
- Why it matters: MedQA is a foundational exam QA corpus and one of the most reused medical benchmarks.
- Method: Open-domain medical exam QA with retrieval plus reading.
- Dataset(s): English, simplified Chinese, traditional Chinese versions.
- Notes: Useful for cross-lingual medical reasoning and answer-format normalization.
- Follow-up references: MedQA code/data repo.

## 2026-05-26 - Med-Flamingo: a Multimodal Medical Few-shot Learner
- Link: https://arxiv.org/abs/2307.15189
- Why it matters: Important multimodal medical data paper; helps identify image-text corpora and VQA-style supervision.
- Method: Continued pretraining on paired/interleaved medical image-text data.
- Dataset(s): multiple medical VQA and vision-language sources.
- Notes: Good reference for multimodal expansion beyond text-only SFT.
- Follow-up references: open-ended medical VQA datasets.

## 2026-05-26 - MedDialog: Two Large-scale Medical Dialogue Datasets
- Link: https://arxiv.org/abs/2004.03329
- Why it matters: One of the earliest large medical dialogue corpora, directly useful for SFT on patient-doctor dialogue.
- Method: Large-scale dialogue collection from real medical Q&A sources.
- Dataset(s): MedDialog-EN, MedDialog-CN.
- Notes: Particularly useful for conversational style and triage-style instruction data.
- Follow-up references: UCSD-AI4H medical dialogue repo.

## 2026-05-26 - MedREQAL: Examining Medical Knowledge Recall of Large Language Models via Question Answering
- Link: https://arxiv.org/abs/2406.05845
- Why it matters: Newer biomedical QA set built from systematic reviews; good for evidence-grounded answer generation.
- Method: Question-answer pairs extracted from systematic reviews.
- Dataset(s): MedREQAL.
- Notes: Useful bridge between literature mining and SFT.
- Follow-up references: systematic review extraction pipeline.

## 2026-05-26 - MultifacetEval: Multifaceted Evaluation to Probe LLMs in Mastering Medical Knowledge
- Link: https://arxiv.org/abs/2406.02919
- Why it matters: Shows how to stress-test depth, precision, and coverage beyond one-shot exam accuracy.
- Method: Multifaceted evaluation across comparison, rectification, discrimination, verification.
- Dataset(s): MultiDiseK, MultiMedQA.
- Notes: Good template for generating harder training/eval splits from existing medical QA.
- Follow-up references: project repo and rephrasing pipeline.

## 2026-05-26 - EHRXQA: A Multi-Modal Question Answering Dataset for Electronic Health Records with Chest X-ray Images
- Link: https://arxiv.org/abs/2310.18652
- Why it matters: Bridges structured EHR and imaging, which is exactly the kind of cross-modal supervision that tends to pay off in healthcare assistants.
- Method: Combine uni-modal EHR QA and chest X-ray VQA into one multimodal benchmark.
- Dataset(s): MIMIC-CXR-VQA, EHRSQL (MIMIC-IV).
- Notes: Strong reference for multimodal grounding and cross-modal clinical reasoning.
- Follow-up references: linked EHRSQL and VQA resources.

## 2026-05-26 - MedAlign: A Clinician-Generated Dataset for Instruction Following with Electronic Medical Records
- Link: https://arxiv.org/abs/2308.14089
- Why it matters: Direct instruction-following from EHRs, which is very close to what SFT on a healthcare assistant needs.
- Method: Clinician-curated instructions with reference responses and longitudinal EHR grounding.
- Dataset(s): 983 instructions, 303 reference responses, 276 longitudinal EHRs.
- Notes: One of the highest-signal instruction datasets in the medical space.
- Follow-up references: clinician evaluation methodology.

## 2026-05-26 - K-QA: A Real-World Medical Q&A Benchmark
- Link: https://arxiv.org/abs/2401.14493
- Why it matters: Real patient questions and physician answers, plus statement-level decomposition for factuality checks.
- Method: Benchmark with physician-authored responses and hallucination/comprehensiveness metrics.
- Dataset(s): 1,212 patient questions.
- Notes: Useful for both SFT and eval of response accuracy.
- Follow-up references: answer decomposition and NLI metric design.

## 2026-05-26 - SLAKE: A Semantically-Labeled Knowledge-Enhanced Dataset for Medical Visual Question Answering
- Link: https://arxiv.org/abs/2102.09542
- Why it matters: Bilingual Med-VQA with semantic labels and knowledge base support.
- Method: Physician-annotated semantic labels over medical images and questions.
- Dataset(s): SLAKE.
- Notes: Good for multimodal medical instruction tuning and grounding.
- Follow-up references: med-vqa.com/slake.

## 2026-05-26 - ECG-QA: A Comprehensive Question Answering Dataset Combined With Electrocardiogram
- Link: https://arxiv.org/abs/2306.15681
- Why it matters: Adds ECG interpretation into the QA mix, broadening beyond text and images.
- Method: 70 ECG question templates validated by an ECG expert.
- Dataset(s): ECG-QA.
- Notes: Useful for cardiac reasoning and signal-grounded medical assistance.
- Follow-up references: ECG-QA repo.

## 2026-05-26 - MedAlpaca -- An Open-Source Collection of Medical Conversational AI Models and Training Data
- Link: https://arxiv.org/abs/2304.08247
- Why it matters: One of the strongest open medical SFT collections; broad coverage and directly usable instruction data.
- Method: Fine-tuning on Medical Meadow style instruction datasets.
- Dataset(s): Medical Flashcards, Wikidoc, StackExchange Health, ChatDoctor, and others in the Medical Meadow family.
- Notes: Excellent seed for a large SFT corpus because it already packages multiple medical tasks in instruction format.
- Follow-up references: Medical Meadow dataset family and downstream fine-tuning scripts.

## 2026-05-26 - ChatDoctor: A Medical Chat Model Fine-Tuned on a Large Language Model Meta-AI (LLaMA) Using Medical Domain Knowledge
- Link: https://arxiv.org/abs/2303.14070
- Why it matters: Large patient-doctor dialogue source with practical conversational tuning value.
- Method: Fine-tuning on 100k patient-doctor dialogues and retrieval augmentation.
- Dataset(s): 100k patient-doctor dialogues from online medical consultation platform.
- Notes: Strong source for conversational medical SFT and dialogue style.
- Follow-up references: online consultation source and retrieval setup.

## 2026-05-26 - MLEC-QA: A Chinese Multi-Choice Biomedical Question Answering Dataset
- Link: https://aclanthology.org/2021.emnlp-main.698/
- Why it matters: Large Chinese biomedical QA set that broadens language coverage and domain diversity.
- Method: Open-domain multi-choice biomedical QA over Chinese medical licensing exam style questions.
- Dataset(s): 136,236 Chinese multi-choice biomedical questions with multiple subfields.
- Notes: High-value if multilingual Chinese medical reasoning matters.
- Follow-up references: retrieval and reader pipeline described in the repo.

## 2026-05-26 - MEDIQA-Chat 2023 and MEDIQA-Sum 2023 shared-task papers
- Link: https://arxiv.org/abs/2305.02220 and https://arxiv.org/abs/2307.02006
- Why it matters: Shared-task data for doctor-patient conversation summarization and note generation.
- Method: Clinical note generation and dialogue-to-record summarization with PLMs and LLMs.
- Dataset(s): MEDIQA-Chat, MEDIQA-Sum shared-task datasets.
- Notes: Good source for clinician-facing summarization and documentation workflows.
- Follow-up references: task organizers and shared-task data release pages.

## 2026-05-26 - MIRIAD: Augmenting LLMs with millions of medical query-response pairs
- Link: https://arxiv.org/abs/2506.06091
- Why it matters: Million-scale medical query-response corpus that is directly aligned with the scale target.
- Method: Operationalized query-response pairs grounded in peer-reviewed literature.
- Dataset(s): MIRIAD 4.4M and 5.8M variants.
- Notes: This is a major scaling candidate for the SFT corpus, subject to access and licensing review.
- Follow-up references: MIRIAD repo and retrieval/data generation pipeline.
