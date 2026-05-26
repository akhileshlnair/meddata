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
- Current derived corpus total: 898,199 lines.
