# Swiss Gambit Dragon Opening Reorganization Review

Status: proposal only. No files have been moved, renamed, merged, archived, or edited.

## Scope

This document captures the proposed reorganization for Swiss Gambit Dragon Opening so it can be reviewed before any workspace changes are made.

## Current Inventory Confirmed

Current top level inside Swiss Gambit Dragon Opening:

- PROJECT_SUMMARY.md
- SWISS_WORKING_SUMMARY.md
- Swiss Gambit Dragon Opening.md
- Swiss Gambit Dragon Opening.docx
- working_notes/

Current flat notes inside working_notes:

- SWISS_ARC_1_HIGH_LEVEL_BEATS.md
- SWISS_ARC_1_PROGRESSION_NOTE.md
- SWISS_EARTH_LOADOUTS_NOTE.md
- SWISS_EQUIPMENT_AND_LOW_MAGIC_NOTE.md
- SWISS_HERO_CORE_NOTE.md
- SWISS_HERO_WAR_KIT_NOTE.md
- SWISS_MANA_AND_GAMBIT_RULES_NOTE.md
- SWISS_PARTY_AND_SIGNATURE_GEAR_NOTE.md
- SWISS_PIVOT_LOGISTICS_NOTE.md
- SWISS_PRETRANSFER_BACKSTORY_OPTIONS.md
- SWISS_STRENGTH_AND_SUMMON_RECOMMENDATION.md
- SWISS_TELEPORTATION_AND_ANCHOR_MODEL.md
- SWISS_TIMELINE_AND_IDENTITY_RECOMMENDATION.md
- SWISS_TWO_YEAR_POWER_MODEL_NOTE.md
- SWISS_VIABILITY_AND_DIRECTION_NOTE.md

Current scene folder inside working_notes/swiss_scene:

- SUMMARY.md
- [START HERE] SWISS_ESCAPE_AND_BERN_SCENE_NOTE.md
- SWISS_BERN_OFFICE_SCENE_NOTE.md
- SWISS_DIPLOMATIC_OPENING_NOTE.md
- SWISS_FIELD_KIT_CONTENTS_NOTE.md

## Proposed Target Structure

Swiss Gambit Dragon Opening/

- PROJECT_SUMMARY.md
- SWISS_WORKING_SUMMARY.md
- Swiss Gambit Dragon Opening.md
- Swiss Gambit Dragon Opening.docx
- lore/
  - CHARACTERS_AND_PARTY.md
  - MAGIC_SYSTEM.md
  - GEAR_AND_LOADOUTS.md
  - TIMELINE_AND_BACKSTORY.md
  - VIABILITY_AND_DIRECTION.md
- scenes/
  - SUMMARY.md
  - [START HERE] SWISS_ESCAPE_AND_BERN_SCENE_NOTE.md
  - SWISS_BERN_OFFICE_SCENE_NOTE.md
  - SWISS_DIPLOMATIC_OPENING_NOTE.md
  - SWISS_FIELD_KIT_CONTENTS_NOTE.md
- archive/
  - superseded flat notes and any replaced intermediate material

## Planned Operations

### Keep unchanged

- PROJECT_SUMMARY.md stays in place.
- SWISS_WORKING_SUMMARY.md stays in place as the master direction document.
- Swiss Gambit Dragon Opening.md stays in place and must not be edited.
- Swiss Gambit Dragon Opening.docx is outside the requested reorganization and would be left alone unless you say otherwise.

### Rename and move scenes

- Rename working_notes/swiss_scene/ to top-level scenes/.
- Move all 5 scene files unchanged.
- Only update cross-file references if a path actually breaks.
- Filename-relative references are expected to remain valid.

### Consolidate flat notes into lore

Proposed merge map:

- CHARACTERS_AND_PARTY.md
  - SWISS_HERO_CORE_NOTE.md
  - SWISS_PARTY_AND_SIGNATURE_GEAR_NOTE.md
  - SWISS_STRENGTH_AND_SUMMON_RECOMMENDATION.md
  - SWISS_TWO_YEAR_POWER_MODEL_NOTE.md

- MAGIC_SYSTEM.md
  - SWISS_MANA_AND_GAMBIT_RULES_NOTE.md
  - SWISS_TELEPORTATION_AND_ANCHOR_MODEL.md

- GEAR_AND_LOADOUTS.md
  - SWISS_EARTH_LOADOUTS_NOTE.md
  - SWISS_EQUIPMENT_AND_LOW_MAGIC_NOTE.md
  - SWISS_HERO_WAR_KIT_NOTE.md

- TIMELINE_AND_BACKSTORY.md
  - SWISS_TIMELINE_AND_IDENTITY_RECOMMENDATION.md
  - SWISS_PRETRANSFER_BACKSTORY_OPTIONS.md
  - SWISS_ARC_1_HIGH_LEVEL_BEATS.md
  - SWISS_ARC_1_PROGRESSION_NOTE.md

- VIABILITY_AND_DIRECTION.md
  - SWISS_VIABILITY_AND_DIRECTION_NOTE.md
  - SWISS_PIVOT_LOGISTICS_NOTE.md

## Preservation Rules To Apply During Reorganization

- Preserve every distinct decision. No information should be dropped during consolidation.
- Do not rewrite old notes for prose cleanup unless required to preserve meaning during merge.
- Do not touch Swiss Gambit Dragon Opening.md.
- Preserve capitalization of filenames.
- Preserve the [START HERE] prefix exactly as-is.
- Aiden in existing working notes should be treated as Wesley Hale going forward, but the existing text should remain untouched unless you later request text rewrites.

## Arc 1 Handling

Special instruction captured from your request:

- SWISS_ARC_1_HIGH_LEVEL_BEATS.md and SWISS_ARC_1_PROGRESSION_NOTE.md must remain easy to work from after compacting.
- They should not be merged into an indistinct blob.
- Two valid implementation options during the actual reorganization:
  - retain them as clearly labeled sections inside TIMELINE_AND_BACKSTORY.md
  - retain them as their own files under lore/ with TIMELINE_AND_BACKSTORY.md acting as an index or synthesis

This is the main point that likely needs your confirmation before execution.

## Archive Policy

- Anything superseded by the new lore files should move to archive/ rather than being deleted.
- Any intermediate merged material that becomes redundant should also go to archive/.
- The intent is reversibility and searchability, not cleanup by deletion.

## Questions To Confirm Before Execution

1. For Arc 1, do you want retained sections inside TIMELINE_AND_BACKSTORY.md, or separate retained files under lore/?
2. Should the original 15 flat source notes all be moved into archive/ after consolidation, even if their contents are fully preserved in lore/?
3. Do you want working_notes/ removed entirely if it becomes empty after moving scenes and archiving the flat notes?
4. Should Swiss Gambit Dragon Opening.docx remain exactly where it is, unchanged?

## Execution Plan Once Approved

1. Create lore/, scenes/, and archive/.
2. Move working_notes/swiss_scene/ content into scenes/ unchanged.
3. Consolidate the 15 flat notes into the agreed lore structure with no information loss.
4. Retain Arc 1 material in the exact form you choose.
5. Move superseded source notes into archive/.
6. Remove or keep working_notes/ depending on your answer.
7. Run a final structure check and report the resulting tree.

## Approval Gate

No reorganization should happen until you explicitly say to proceed.

## Post-Reorganization Naming Note

This section was added after the reorganization pass and follow-up review.

Quick outside title-advice check still points to the same core test: a strong fiction project name usually earns its keep through memorability, tonal fit, and a clear hook, not by literally describing everything in the plot.

My read on `Swiss Gambit Dragon Opening`:

- `Swiss Gambit` is the strongest part of the name. It immediately signals maneuver, risk, politics, neutrality, and a deliberate strategic play.
- `Dragon Opening` is the shakier part. It has energy, but it can read more like a chess variation, card-game line, or beginning-state label than the actual core of the story.
- Given the current project shape, the strongest material is not really "dragon opening" energy. It is returned-hero strain, recognition politics, mana asymmetry, and the Swiss recognition gambit.
- Because of that, the current title works better as an internal project name than as a fully locked final title.

My practical recommendation:

- keep the current name for now if it still helps you find the story's identity quickly
- revisit it later only if you want the eventual public-facing title to foreground the political-bridge premise more directly
- if you ever retitle it, preserve the strategic feel of `Swiss Gambit`, because that phrase is carrying a lot of the project's identity already

## Brief Project Read

The project is in a better place than a lot of portal-fantasy concepts because it has real friction.

- Earth is useful but not magically dominant.
- The fantasy world is powerful but materially constrained.
- The protagonist is important without being omnipotent.
- The Swiss route is interesting because it solves a legitimacy problem, not just a transport problem.

That gives the story a real shape: it is less about spectacle and more about how a person tries to stop both worlds from turning him into property while still extracting enough recognition and support to keep the kingdom alive.
