# Download Queue

Priority order for the first useful corpus slices.

## Tier 1: fast, high-yield, public

1. PubMedQA
2. MedQA
3. MedMCQA
4. MedDialog
5. HealthSearchQA

## Tier 2: instruction-following and clinical grounding

6. MedAlign
7. emrQA
8. DrugEHRQA
9. BioASQ

## Tier 3: large or gated clinical sources

10. MIMIC-IV
11. MIMIC-CXR
12. CheXpert
13. CORD-19
14. TREC-COVID

## Notes

- Tier 1 should be mirrored first to establish extraction and normalization.
- Tier 3 may require credentialed access, extra storage, and careful licensing review.
- For each dataset we should capture: source URL, access requirements, size, format, and whether it is safe to promote into a git-backed shard.
