# Storage Strategy

We need to balance three things:

1. Large-scale collection of medical ML papers and datasets.
2. Durable notes and source tracking.
3. A git-friendly way to preserve work when local disk pressure rises.

## Working rule

- Keep raw downloads under `data/raw/`.
- Keep parsed text and chunked SFT candidates under `data/derived/`.
- Keep source metadata, checksums, and collection logs in tracked markdown/CSV files.
- Prefer compact, append-only text shards for anything that must be pushed to git.

## GitHub note

GitHub is best used here for:

- notes
- manifests
- small derived shards
- code and download scripts

For the full 50M to 100M line target, raw corpora should be chunked aggressively and only the useful, license-compatible slices should be promoted into git. If future pushes need to include heavy artifacts, that likely means a separate data repo or Git LFS-style handling.

## Current space

- Local free space checked on 2026-05-26: about 68 GiB available on the workspace volume.
