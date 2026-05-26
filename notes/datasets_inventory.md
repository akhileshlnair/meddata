# Dataset Inventory

This file tracks datasets discovered during the literature sweep.

Columns to capture:

- Name
- Domain
- Source
- License / access constraints
- Size
- Format
- Why it is useful for SFT
- Download status
- Notes

## 2026-05-26 - MedQA
- Domain: medical exam QA
- Source: https://github.com/jind11/MedQA
- License / access constraints: public repo with linked data files
- Size: 12,723 English; 34,251 simplified Chinese; 14,123 traditional Chinese
- Format: QA pairs / multiple choice
- Why it is useful for SFT: strong instruction-style medical reasoning corpus
- Download status: identified
- Notes: one of the most reusable medical benchmarks for both training and eval.

## 2026-05-26 - MedMCQA
- Domain: medical exam QA
- Source: https://github.com/medmcqa/medmcqa
- License / access constraints: public benchmark repo
- Size: 194k+ questions
- Format: multiple choice QA
- Why it is useful for SFT: broad subject coverage and large scale
- Download status: identified
- Notes: especially useful for exam-style reasoning and answer formatting.

## 2026-05-26 - PubMedQA
- Domain: biomedical research QA
- Source: https://pubmedqa.github.io/ and https://github.com/pubmedqa/pubmedqa
- License / access constraints: public repo
- Size: 1k expert labeled, 61.2k unlabeled, 211.3k artificial
- Format: question, abstract context, long answer, yes/no/maybe label
- Why it is useful for SFT: evidence-grounded biomedical reasoning
- Download status: identified
- Notes: valuable for literature-based answer generation.

## 2026-05-26 - HealthSearchQA
- Domain: consumer medical QA
- Source: described in https://arxiv.org/abs/2212.13138
- License / access constraints: check paper / released benchmark materials
- Size: 3,173 questions
- Format: free-response consumer health questions
- Why it is useful for SFT: practical health question answering and safety-sensitive response style
- Download status: identified
- Notes: pairs well with MultiMedQA-style eval and safety tuning.

## 2026-05-26 - MIMIC-IV
- Domain: EHR / clinical data
- Source: https://physionet.org/content/mimiciv/2.2/
- License / access constraints: credentialed PhysioNet access required
- Size: contemporary ICU and hospital EHR at scale
- Format: structured clinical tables
- Why it is useful for SFT: source material for clinical reasoning, summarization, and note generation
- Download status: identified
- Notes: must respect access workflow and storage planning.

## 2026-05-26 - MIMIC-CXR
- Domain: radiology images + reports
- Source: https://physionet.org/content/mimic-cxr/
- License / access constraints: credentialed PhysioNet access required
- Size: 377,110 images / 227,835 studies
- Format: DICOM + free-text reports
- Why it is useful for SFT: radiology report generation, VQA, and multimodal alignment
- Download status: identified
- Notes: huge and high value, but storage-heavy.

## 2026-05-26 - CheXpert
- Domain: chest x-ray classification
- Source: https://stanfordmlgroup.github.io/competitions/chexpert/
- License / access constraints: registration and agreement required
- Size: large chest radiograph corpus
- Format: X-ray images with uncertainty labels
- Why it is useful for SFT: clinical imaging supervision and label generation
- Download status: identified
- Notes: useful companion to MIMIC-CXR for imaging tasks.

## 2026-05-26 - MedDialog-EN / MedDialog-CN
- Domain: patient-doctor dialogue
- Source: https://arxiv.org/abs/2004.03329 and https://github.com/sidney1994/Medical-Dialogue-System
- License / access constraints: source-specific download links; verify terms
- Size: 0.3M conversations EN / 1.1M conversations CN
- Format: dialogue turns
- Why it is useful for SFT: conversational medical instruction tuning
- Download status: identified
- Notes: especially relevant for chatbot-style medical assistance.

## 2026-05-26 - BioASQ
- Domain: biomedical semantic indexing and QA
- Source: https://bioasq.org/ and https://participants-area.bioasq.org/
- License / access constraints: challenge data access and sign-up
- Size: multi-task challenge datasets, updated each cycle
- Format: questions, snippets, answers, indexing targets
- Why it is useful for SFT: biomedical QA and retrieval-aligned supervision
- Download status: identified
- Notes: important for evidence retrieval and answer synthesis.

## 2026-05-26 - CORD-19
- Domain: COVID-19 scientific literature
- Source: https://arxiv.org/abs/2004.10706
- License / access constraints: open research dataset, verify current distribution
- Size: large corpus of scientific papers and metadata
- Format: full text + metadata
- Why it is useful for SFT: scientific reading, synthesis, and citation-grounded response generation
- Download status: identified
- Notes: valuable if Vivral wants literature-heavy biomedical retrieval.

## 2026-05-26 - TREC-COVID
- Domain: biomedical information retrieval
- Source: https://arxiv.org/abs/2104.09632
- License / access constraints: benchmark task resources
- Size: 50 topics over rounds of judgments
- Format: queries, relevance judgments, scientific corpus
- Why it is useful for SFT: retrieval, ranking, and evidence selection
- Download status: identified
- Notes: useful for training search-then-answer workflows.

## 2026-05-26 - MedAlign
- Domain: clinician-generated instruction following on EHRs
- Source: https://github.com/som-shahlab/medalign
- License / access constraints: check repo / dataset terms
- Size: 983 clinician-curated instructions grounded in 275 longitudinal EHRs
- Format: instruction-response grounded in records
- Why it is useful for SFT: direct instruction-following clinical supervision
- Download status: identified
- Notes: a high-signal supervised tuning asset.

## 2026-05-26 - DrugEHRQA
- Domain: medicine-related EHR QA
- Source: https://arxiv.org/abs/2205.01290
- License / access constraints: verify release details
- Size: paper-reported QA dataset on structured and unstructured EHRs
- Format: question answering over EHR data
- Why it is useful for SFT: medication and record-grounded QA
- Download status: identified
- Notes: promising for medicine-related query answering.

## 2026-05-26 - emrQA
- Domain: QA over electronic medical records
- Source: https://emrqa.github.io/
- License / access constraints: build from i2b2 NER data, follow repo instructions
- Size: large clinical QA benchmark
- Format: questions, paraphrases, logical forms, answers
- Why it is useful for SFT: structured clinical QA and reasoning
- Download status: identified
- Notes: very useful for note-grounded QA and paraphrase robustness.

## 2026-05-26 - EHRXQA
- Domain: multimodal EHR QA
- Source: https://arxiv.org/abs/2310.18652 and https://github.com/baeseongsu/ehrxqa
- License / access constraints: verify repo terms / access for derived resources
- Size: built from multimodal EHR + chest X-ray resources
- Format: question answering over structured EHR and X-ray images
- Why it is useful for SFT: cross-modal clinical reasoning
- Download status: identified
- Notes: especially useful if Vivral needs grounding across tabular and imaging data.

## 2026-05-26 - SLAKE
- Domain: medical visual question answering
- Source: https://arxiv.org/abs/2102.09542 and http://www.med-vqa.com/slake
- License / access constraints: verify website terms
- Size: bilingual dataset with physician semantic labels
- Format: image-question-answer with knowledge-enhanced labels
- Why it is useful for SFT: multimodal medical dialogue and visual grounding
- Download status: identified
- Notes: strong fit for medical image understanding plus answer generation.

## 2026-05-26 - VQA-Med
- Domain: radiology visual question answering
- Source: referenced in medical VQA papers and ImageCLEF/VQA-Med challenge materials
- License / access constraints: challenge data access may apply
- Size: official splits in the thousands of QA pairs
- Format: image-question-answer
- Why it is useful for SFT: radiology-centric visual reasoning
- Download status: identified
- Notes: a classic medical VQA benchmark and useful multimodal seed.

## 2026-05-26 - PathVQA
- Domain: pathology visual question answering
- Source: cited in medical VQA papers and public challenge materials
- License / access constraints: verify source website / paper repository
- Size: 32,632 QA pairs on 4,289 images
- Format: pathology image-question-answer
- Why it is useful for SFT: pathology reasoning and answer generation
- Download status: identified
- Notes: one of the highest-yield pathology QA datasets.

## 2026-05-26 - ECG-QA
- Domain: electrocardiogram QA
- Source: https://arxiv.org/abs/2306.15681 and https://github.com/Jwoo5/ecg-qa
- License / access constraints: verify repo terms and linked ECG data policy
- Size: 70 question templates covering broad ECG topics
- Format: ECG interpretation QA
- Why it is useful for SFT: text+signal clinical reasoning
- Download status: identified
- Notes: useful for cardiac reasoning and diagnostic explanations.

## 2026-05-26 - K-QA
- Domain: consumer medical QA
- Source: https://arxiv.org/abs/2401.14493
- License / access constraints: public benchmark release
- Size: 1,212 patient questions
- Format: patient questions with physician answers and decomposed statements
- Why it is useful for SFT: realistic medical answer generation and hallucination evaluation
- Download status: identified
- Notes: good for grounded, physician-style response supervision.

## 2026-05-26 - AMQA
- Domain: adversarial medical QA
- Source: https://github.com/XY-Showing/AMQA
- License / access constraints: verify repo terms and HF page terms
- Size: dataset derived from USMLE clinical vignettes with adversarial variants
- Format: original vignette + neutralized version + adversarial variants
- Why it is useful for SFT: bias testing and robustness tuning
- Download status: identified
- Notes: useful for fairness and sensitivity checks around medical QA.

## 2026-05-26 - ViHealthQA
- Domain: Vietnamese healthcare QA
- Source: cited in SPBERTQA / related medical QA literature
- License / access constraints: verify repository or paper release
- Size: 10,015 question-answer passage pairs
- Format: question-answer-passage
- Why it is useful for SFT: multilingual medical QA and retrieval-grounded answers
- Download status: identified
- Notes: useful if multilingual expansion matters.

## 2026-05-26 - TM-PATHVQA
- Domain: multilingual spoken pathology QA
- Source: https://arxiv.org/abs/2407.11383
- License / access constraints: verify repository release
- Size: 98,397 spoken QA pairs and 70 hours of audio
- Format: audio-question-answer over pathology images
- Why it is useful for SFT: multimodal and speech-enabled medical QA
- Download status: identified
- Notes: useful for future voice-first clinical assistants.

## 2026-05-26 - Medical Meadow / MedAlpaca
- Domain: medical conversational instruction data
- Source: https://arxiv.org/abs/2304.08247 and https://github.com/kbressem/medAlpaca
- License / access constraints: verify each underlying source dataset
- Size: roughly 1.5 million data points across multiple tasks
- Format: instruction-following / Q-A style medical tasks
- Why it is useful for SFT: one of the best open instruction-tuning corpora in medicine
- Download status: identified
- Notes: likely the first source we should actually mirror in derived form.

## 2026-05-26 - ChatDoctor
- Domain: medical dialogue
- Source: https://arxiv.org/abs/2303.14070
- License / access constraints: verify platform source and release terms
- Size: 100,000 patient-doctor dialogues
- Format: dialogue turns / medical chat
- Why it is useful for SFT: conversational medical assistance and dialogue conditioning
- Download status: identified
- Notes: strong companion to MedDialog and Medical Meadow.

## 2026-05-26 - MLEC-QA
- Domain: Chinese biomedical exam QA
- Source: https://github.com/Judenpech/MLEC-QA
- License / access constraints: MIT repo with Google Drive data link
- Size: 136,236 questions
- Format: multi-choice QA
- Why it is useful for SFT: high-volume Chinese biomedical reasoning data
- Download status: identified
- Notes: useful for multilingual expansion and exam-style medical reasoning.

## 2026-05-26 - MEDIQA-Chat
- Domain: doctor-patient dialogue summarization and note generation
- Source: https://arxiv.org/abs/2305.02220
- License / access constraints: shared-task release / organizer page
- Size: shared-task data, exact size depends on task split
- Format: dialogue to clinical note generation
- Why it is useful for SFT: documentation and summarization supervision
- Download status: identified
- Notes: strong fit for clinician note drafting.

## 2026-05-26 - MEDIQA-Sum
- Domain: patient dialogue summarization
- Source: https://arxiv.org/abs/2307.02006
- License / access constraints: shared-task release / organizer page
- Size: shared-task data, exact size depends on task split
- Format: dialogue to medical record summarization
- Why it is useful for SFT: summary generation from conversations
- Download status: identified
- Notes: useful for robust medical summarization behavior.

## 2026-05-26 - MIRIAD
- Domain: million-scale medical query-response
- Source: https://github.com/eth-medical-ai-lab/MIRIAD
- License / access constraints: verify repo release and dataset card
- Size: 4.4M and 5.8M versions
- Format: query-response pairs grounded in biomedical literature
- Why it is useful for SFT: one of the highest-scale directly relevant sources for the target corpus
- Download status: identified
- Notes: this is a top-priority source for scaling.

## 2026-05-26 - medical-o1-reasoning-SFT
- Domain: medical reasoning SFT
- Source: https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT
- License / access constraints: Hugging Face dataset terms
- Size: 19,704 English; 20,171 Chinese
- Format: question / complex chain-of-thought / response
- Why it is useful for SFT: explicit reasoning supervision in a clean instruction format
- Download status: downloaded
- Notes: very useful for reasoning-heavy medical assistants; the English and Chinese configs are already mirrored locally.
