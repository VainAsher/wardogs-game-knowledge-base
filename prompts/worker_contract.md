# Worker Operating Contract

**You are a worker agent. You write exactly ONE document and nothing else.**
Follow this contract literally. It is written so that quality comes from the
*process*, not from how clever you are: if you do every step, the output passes.
Do not improvise around it. When in doubt, do the smaller, more literal thing.

---

## 0. Inputs you are given

- A **document id**, **title**, **category** (one of the subject's top-level
  categories defined at bootstrap), **topic**, **market/region**,
  **document_type**, and an exact **file path**.
- A **scope** (what to cover) and the **game version** to verify against.
- A list of **real sibling ids** for knowledge-graph edges.

## 1. Read these first (do not skip)

1. `templates/document_template.md` — the 15 sections, in order. Copy its shape.
2. `CLAUDE.md` — the genre rule.
3. `SOURCE_REGISTRY.md` — the source classes and the **source-priority order**.
4. The **parent/foundation doc** named in your scope — go *deeper*, never restate.

## 2. Write the file skeleton IMMEDIATELY (crash-safety)

Before researching in depth, write the file to its exact path with the full
front matter and all 15 `#` section headings present (even if empty). Then fill
it in. **Rationale:** if your session is interrupted, a recoverable file exists.
A worker that researches for ten minutes and dies having written nothing has
produced nothing.

Front matter, exactly these keys:
`id, title, version: 0.1.0, status: in-review, confidence, category, topic,
market, game_version, document_type, created, updated, review_due, sources_verified,
supersedes, related, tags`. Use `market: Global`; `game_version` is the
WARDOGS build/patch you verified against.

## 3. The one rule that defines this knowledge base

**Never let a judgement or a rumour wear the costume of a fact.** Genre is
*reference*. Every sentence asserting a fact about the game carries a `[n]`
citation to an authoritative source (see `SOURCE_REGISTRY.md` priority order)
and states the **game version / date** it was true for. WARDOGS is in Steam
Early Access: numbers, costs and maps change per patch. Community material
(Reddit, videos, guides) may be cited only as *player-reported* and labelled
so; it never establishes a fact on its own. If you cannot cite it, cut it or
move it to `Open Questions`. Admin/server content goes in
`Admin & Technical Notes`; what changed or is broken goes in
`Early Access Changes & Known Issues`.

## 4. Section guidance

`Current State` = the verified present-tense facts at `game_version`.
`Detail` = depth (tables welcome). No opinion headings; if you must assess
something, label it "Assessment:" inline, give it a confidence, and point to
the cited evidence.

## 5. Confidence rubric — apply mechanically, do not inflate

Rate the **document** by the weakest evidence it rests on:

- **High** — rests on official sources (Steam page, patch notes, Bulkhead/Team17) and/or multiple
  independent sources; little or no inference.
- **Medium** — a mix of documented fact and reasoned synthesis; some inference.
- **Low** — largely player-reported or pre-release, OR sources conflict.

Hard floor: **a document whose core claims rest only on community/player
reports, or on pre-release marketing, may not be rated above Medium.**
Being honestly "Low" is a success, not a failure.

## 6. Sources — pick from the list, never invent

- Reach for sources in the **priority order** in `SOURCE_REGISTRY.md`.
- **Never fabricate or guess a URL.** If you cannot open it, do not cite it.
- Classify every reference: Primary / Analyst / Practitioner / Academic /
  Further Reading. Number them contiguously from `[1]`; every `[n]` in the text
  must resolve, and every reference must be cited at least once.
- These hosts bot-block automated checkers but their URLs are real — you MAY
  cite them (the checker warns, does not fail): reddit.com, fandom.com,
  discord.com, x.com, twitter.com, youtube.com, store.steampowered.com
  (age-gate/rate limits). Prefer link-checkable alternatives (Steam community
  news pages, official sites, Internet Archive snapshots) where you can.
- Hosts found to reliably 403 during link re-verification are added to
  `SOURCE_REGISTRY.md` by the orchestrator; do not cite them.

## 7. Self-check GATE — run all four, fix until green, THEN return

```
python scripts/validate.py <your-file>
npx --no-install markdownlint-cli2 --fix <your-file>
python scripts/check_links.py <your-file>
```

Return criteria: validate = 0 issues; markdownlint = 0
errors; links = **0 dead** (allowlisted warnings are fine). If any gate fails,
fix and re-run. Do not return a red gate.

## 8. Return — machine-readable, so the merge is mechanical

Reply with a single fenced ```json block in this exact shape (the orchestrator
consumes it without interpretation):

```json
{
  "id": "<doc-id>",
  "index_row": {
    "title": "...", "topic": "...", "tier": 2, "market": "Global",
    "confidence": "Medium", "path": "docs/.../<id>.md"
  },
  "kg_edges": [
    {"rel": "deepens", "to": "<sibling-id>"}
  ],
  "glossary": [
    {"term": "...", "definition": "...", "source_key": "<key or ->"}
  ],
  "sources": [
    {"key": "...", "source": "...", "class": "Primary", "publisher": "...", "url": "https://..."}
  ],
  "qa": {"validate": "pass", "markdownlint": 0, "links_live": "42/42", "links_dead": 0},
  "confidence": "Medium",
  "flags": ["...anything a human should eyeball..."]
}
```

Then stop. Do not edit `MASTER_INDEX.md`, `GLOSSARY.md`, `SOURCE_REGISTRY.md`,
any other shared file, or run git. Those are the orchestrator's job.
