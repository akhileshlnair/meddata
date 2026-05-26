# Research Log

## 2026-05-26
- Initialized the corpus workspace.
- Created persistent notes files for papers and dataset inventory.
- Seeded the notebook with an initial batch of high-signal medicine + ML papers and datasets:
  - MultiMedQA / Med-PaLM / Med-PaLM 2 lineage
  - PubMedQA, MedQA, MedMCQA, MedDialog
  - MIMIC-IV, MIMIC-CXR, CheXpert, BioASQ, CORD-19, TREC-COVID
  - MedAlign, DrugEHRQA, emrQA
- Next: seed the notebook with a first batch of high-signal medicine + ML papers and dataset leads.

## 2026-05-26 - GitHub wiring
- Attached remote repository: `https://github.com/akhileshlnair/meddata.git`
- Renamed local branch to `main`.
- Pushed the initial corpus workspace commit to GitHub.

## 2026-05-26 - Derived corpus download wave
- Mirrored a first tranche of open MedAlpaca medical datasets into `data/derived/medical_meadow/`.
- Downloaded shards:
  - Medical Flashcards: 33,955 rows
  - Wikidoc: 10,000 rows
  - Wikidoc Patient Information: 5,942 rows
  - MedQA: 10,178 rows
  - MEDIQA: 2,208 rows
  - PubMed Causal: 2,446 rows
  - Health Advice: 8,676 rows
  - CORD-19: 821,007 rows
  - MMMLU: 3,787 rows
- Added FreedomIntelligence medical-o1 reasoning shards:
  - English: 19,704 rows
  - Chinese: 20,171 rows
- Current derived corpus total: 7,031,669 lines.

## 2026-05-26 - SFT-first dataset expansion
- Shifted the collection strategy toward datasets that are actually strong for supervised fine-tuning.
- New high-value targets identified:
  - OpenMed/Medical-Reasoning-SFT-Mega
  - Intelligent-Internet/II-Medical-Reasoning-SFT
  - drwlf/medra-medical-thinking
  - lingshu-medical-mllm/ReasonMed
  - FreedomIntelligence/Huatuo26M-Lite
  - miriad/miriad-5.8M
- Added a reusable medical SFT downloader to normalize messages, QA pairs, and raw text fallbacks.
- Updated the corpus inventory and manifests to track these sources explicitly.
- Live snapshot while downloads are running:
  - Current derived corpus total: 11,267,574 lines
  - II-Medical reasoning mirror: 1,395,743 lines written so far
  - ReasonMed mirror: 1,111,555 lines written so far
  - medra-medical-thinking mirror: 2,777,504 lines written so far
  - MIRIAD mirror: 1,000,000 lines written so far
  - Huatuo encyclopedia QA mirror: 362,420 lines written so far
  - Fully Open Meditron mirror: 601,346 lines written so far
  - GPT-OSS medical reasoning mirror: 506,150 lines written so far
  - Asclepius synthetic clinical notes: 158,114 lines written so far
  - MedicalTranscriptions: 4,999 lines written so far
  - MedReason-Stenographic: 31,535 lines written so far
  - GMAI-Reasoning10K: 7,004 lines written so far
  - MedQuAD: 47,441 lines written so far
  - DataFog medical transcription instruct: 38,924 lines written so far
  - HealthcareMagic 100k: 89,732 lines written so far
  - OpenMedical medical-data: 20,363 lines written so far
  - FunDialogues healthcare minor consultation: 100 lines written so far
  - Medical Guanaco 3000: 3,000 lines written so far
  - Medical QA shared-task toy: 32 lines written so far
  - Starlord medical QA dataset: 5,000 lines written so far
  - Deepfabric 7k medical multi-turn conversation: 7,570 lines written so far
  - MedExpQA mirror: 434 lines written so far
  - MedInstruct mirror: 52,002 lines written so far
  - MedXpertQA-Text mirror: 2,450 lines written so far
  - Medical Intelligence 76k mirror: 76,000 lines written so far
  - firstaid-treatment-instruct mirror: 71,037 lines written so far
  - stage1-doctor-patient-chat mirror: 482 lines written so far
  - MediQAl mcqu mirror: 10,000 lines written so far
  - MediQAl mcqm mirror: 5,767 lines written so far
  - MediQAl oeq mirror: 4,969 lines written so far
  - MedQA-4options mirror: 1,273 lines written so far
  - ECN-QA English mirror: 648 lines written so far
  - medical-o1 reasoning en mirror: 19,704 lines written so far
  - medical-o1 reasoning en_mix mirror: 24,887 lines written so far
  - OpenMedical medical-raw medqa mirror: 10,718 lines written so far
  - OpenMedical medical-raw medmcqa mirror: 4,871 lines written so far
  - OpenMedical medical-raw medbullets_5op mirror: 308 lines written so far
  - OpenMedical medical-raw medexqa mirror: 965 lines written so far
