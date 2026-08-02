---
applyTo: "**"
---

# GitHub Profile Repo (`sutz2001/sutz2001`)

This repository is the special profile README for https://github.com/sutz2001.

## Keep instruction files in sync

Whenever you change project rules or agent instructions, update **all** instruction files in the same change:

- `.cursor/rules/**/*.mdc`
- `.github/copilot-instructions.md`
- `.github/instructions/**/*.instructions.md`

Do not leave Cursor and Copilot guidance diverging. Prefer identical substance; adapt only format/frontmatter required by each tool.

## Active profile surface

- `README.md` — profile content only; keep it short
- `assets/about-mac.svg` — System 7 style header (hero brand)

Do not reintroduce third-party stats cards, streak widgets, activity graphs, or visitor counters. They break often and are not official GitHub features. The native contribution graph on the profile page is enough.

## Branding in the header SVG

- Hero name: `sutz2001` (large), then `Marc` underneath
- Look: mostly System 7 black/white/gray + thin classic Apple rainbow accent + colored fact bullets
- Keep the blinking cursor animation
- Prefer ASCII punctuation in the SVG (`-`, `|`) to avoid encoding glitches

## Editing workflow

1. Change copy/layout in `assets/about-mac.svg` and/or `README.md`
2. Preview the SVG locally in a browser before pushing
3. Profile updates go live after commit + push to `main`

## Archive / legacy

- `archive/README.pre-mac-header.md` — previous card-based README
- `archive/legacy-terminal/` — old gifos terminal generator (unused)

Do not wire `generate_terminal.py`, `terminal.gif`, or `GITHUB_TOKEN_SETUP.md` back into the live README unless explicitly requested.

## Secrets and ignore rules

- Never commit `.env`, `.venv/`, or tokens
- No CI workflows are required for the current static profile; `.github/` holds Copilot instructions only
