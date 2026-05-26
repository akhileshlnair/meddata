# Data Layout

The heavy corpus artifacts live under this directory.

Suggested structure:

- `data/raw/`: source downloads and archives
- `data/cache/`: intermediate extraction and parsing caches
- `data/derived/`: cleaned text, chunked corpora, and SFT-ready shards
- `data/manifests/`: tracked metadata, checksums, and source lists

The raw directories are ignored by git; only small manifests and notes should be committed here unless a future push strategy is explicitly chosen.
