# Silo RPG Document Class

This README records the audience boundaries, routing rules, style exceptions, and reference-sheet convention for the Silo RPG document class. It is not a replacement for the player guide, GM references, or [document index](gaming_silo_index.md). Players should use only documents marked Player-safe; GMs and agents can use the GM-only material as needed.

## Purpose and Audiences

The audience labels below follow the purposes stated in the document index. The starter campaign is GM-only because its ten arcs include hidden premises, even though the GM may hand player archetypes to the group.

| Document | Audience |
|---|---|
| [Player Guide](gaming_silo_player_guide.md) | Player-safe |
| [Player Reference Sheet](gaming_reference_silo_player.md) | Player-safe |
| [GM Secrets](gaming_silo_gm_secrets.md) | GM-only |
| [Comprehensive Bible](gaming_silo_comprehensive_bible.md) | GM-only |
| [Starter Campaign](gaming_silo_starter_campaign.md) | GM-only |
| [GM Reference Sheet](gaming_reference_silo_gm.md) | GM-only |
| [Campaign Reference Sheet](gaming_reference_silo_campaign.md) | GM-only |
| [Document Index](gaming_silo_index.md) | GM-only |
| [Reference-Sheet Index](gaming_reference_silo_index.md) | GM-only |

## Spoiler Partition

Keep setting-level revelations in GM-only documents. The GM-only vocabulary includes Operation Fifty, Silo 1, nanobot, argon, heat-tape, Digger, cryo, and amnesiac. Check the player-facing guide and reference sheet for these spoiler terms with:

```bash
grep -n -i -E 'operation fifty|silo 1\b|nanobot|argon|heat-tape|digger|cryo|amnesi' gaming_silo_player_guide.md gaming_reference_silo_player.md
```

The command should print no matches.

## Index and Reading Rule

Use [gaming_silo_index.md](gaming_silo_index.md) as the routing map for lore, rules, mechanics, and campaign content. A pull request that adds, removes, or renames a document, chapter, or section listed by the index updates the index in the same pull request.

Agents must read `gaming_silo_index.md` first when asked about Silo lore, rules, mechanics, setting, or campaign content. Never load `gaming_silo_comprehensive_bible.md`, `gaming_silo_player_guide.md`, `gaming_silo_gm_secrets.md`, or `gaming_silo_starter_campaign.md` in full. Use targeted searches and line-range reads for the sections the index identifies. The four reference sheets are small and may be read in full.

## Style-Guide Applicability

Use UK English in all repository-authored prose. The Style Guide applies to Silo with these existing mechanics exceptions: use `*` bullets, retain manual heading numbers such as `## 1. ...`, and do not use `--number-sections`. Use descriptive Title Case headings, following D5. Recipe titles in `Justfile` are currently ALL-CAPS; heading-case sweep #161 will recase them.

Tables and callouts follow STYLE_GUIDE (D15, D16) in the five Silo documents. In the four reference sheets a table may follow its heading directly; the heading is the lead-in. This D16 layout exception applies only to [gaming_reference_silo_index.md](gaming_reference_silo_index.md), [gaming_reference_silo_player.md](gaming_reference_silo_player.md), [gaming_reference_silo_gm.md](gaming_reference_silo_gm.md), and [gaming_reference_silo_campaign.md](gaming_reference_silo_campaign.md).

## Reference Sheets

The reference sheets are condensed, table-use companions to their source documents. The four source mappings are:

| Reference Sheet | Source |
|---|---|
| [Index Sheet](gaming_reference_silo_index.md) | [Document Index](gaming_silo_index.md) |
| [Player Sheet](gaming_reference_silo_player.md) | [Player Guide](gaming_silo_player_guide.md) |
| [GM Sheet](gaming_reference_silo_gm.md) | Chapters 30–33 of the [Comprehensive Bible](gaming_silo_comprehensive_bible.md) |
| [Campaign Sheet](gaming_reference_silo_campaign.md) | [Starter Campaign](gaming_silo_starter_campaign.md) |

The GM secrets document has no reference sheet by design because its contents are spoilers.

## Keeping Sheets in Sync

A pull request that changes a bible's content also updates its companion reference sheet in the same pull request. Mechanical sweeps — including spelling, heading case, punctuation, and re-renders — are exempt. There is no CI date check: file dates are not meaningful after mechanical sweeps.

## Current Build

Run `cd gaming_silo_rpg && just silo-all` to build the five Silo documents currently in the build. The reference sheets join the build under issue #165, which will update this note.
