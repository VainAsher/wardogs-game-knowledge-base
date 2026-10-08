# Project Handover

Read `CLAUDE.md`, `SOURCE_REGISTRY.md`, `prompts/worker_contract.md`, `templates/document_template.md`.
Pipeline: spawn one worker per doc (contract verbatim), orchestrator merges into `MASTER_INDEX.md`, `GLOSSARY.md` and `SOURCE_REGISTRY.md`, re-runs gates, freezes at v1.0.0 and tags.
Gate commands: `python scripts/validate.py`, `npx markdownlint-cli2 "docs/**/*.md" "*.md"`, `python scripts/check_links.py`, `python scripts/build_graph.py`, `python scripts/build_site.py`.
