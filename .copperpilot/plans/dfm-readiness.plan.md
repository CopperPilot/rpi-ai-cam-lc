---
name: ''
overview: ''
todos: []
overall_status: completed
---

# DFM and Assembly Readiness Verification Plan

## Goal
Verify and resolve all JLCPCB and Lion Circuits DFM, DRC, ERC, schematic parity, BOM/CPL/POS, and 2-up panelization readiness checks across `hardware/` and `fab/`.

## Tasks
- [x] Inspect schematic, main PCB, 2-up panel PCB, and `fab/` manufacturing package.
- [x] Fix schematic local net label slash escaping (`199` `net_conflict` parity warnings -> `0`).
- [x] Populate missing `Datasheet` URLs across all `71` BOM components in schematic, symbols, footprints, and PCBs (`parts.bom_fields` -> `0` findings).
- [x] Upgrade `min_text_height` to `1.0 mm` and resize all visible silkscreen Reference designators from `0.8 mm` to `1.0 mm` without overlap (`pcb.rules` and `pcb.drc` -> `0` findings).
- [x] Resolve all `553` DRC violations on `fab/panel/rpi-ai-cam-lc-panel.kicad_pcb` (`fp-lib-table`, mousebite tab placement outside connector courtyards and antenna keepout, `0.85–1.00 mm` hole pitch, `F.CrtYd` outlines, and zone refill).
- [x] Regenerate Gerbers, Excellon drill files, top/bottom POS CSVs (`75` top + `6` bottom = `81` placements), schematic PDF, and ZIP archives.
- [x] Run live JLCPCB online DFM checker (`jlcdfm.com`), resolve all actionable `Pad spacing`, `Soldermask bridge`, `Solder mask opening exposing trace`, `Sharp trace corner`, `Silkscreen to hole`, and `Silkscreen to pad` findings in KiCad, and re-verify on `jlcdfm.com`.
- [x] Remove all stale temporary, staging, and intermediate DFM files and keep only the latest verified design and fabrication deliverables.