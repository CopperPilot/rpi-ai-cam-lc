# Final Placement, Orientation, JLCPCB DFM, and Lion Circuits BOM Sign-Off Report

## 1. Executive Summary

| Verification Domain | Target / Tool | Status | Key Result |
|---|---|---|---|
| **Schematic ERC** | `hardware/rpi-ai-cam-lc.kicad_sch` (`kicad-cli 10.0.4`) | **PASS** | `0` errors, `0` warnings |
| **Main PCB DRC & Parity** | `hardware/rpi-ai-cam-lc.kicad_pcb` (`55.0 x 40.0 mm`, 6L) | **PASS** | `0` DRC errors, `0` warnings, `0` unconnected, `0` parity errors |
| **2-Up Panel PCB DRC** | `fab/panel/rpi-ai-cam-lc-panel.kicad_pcb` (`113.0 x 56.0 mm`, 6L) | **PASS** | `0` DRC errors, `0` warnings, `0` unconnected items |
| **CPL / POS / Panel Sync** | `81` placements (`75` Top, `6` Bottom) across PCB, Panel, CPL, POS | **PASS** | `0` coordinate, rotation, or side mismatches (`< 0.001 mm`, `0.0 deg`) |
| **Component Orientation & Polarity** | Connectors (`J1..J7`), Switches (`SW1..SW2`), Spacers (`SP1..SP8`), ICs (`U1..U6`), Diodes (`D1..D12`), Tantalum Caps (`C26..C31`) | **PASS** | 100% verified against datasheets, 3D STEP models, and enclosure cutouts |
| **JLCPCB Live DFM** | `https://jlcdfm.com/viewer?pcbUploadFileId=644061065261510657` | **PASS** | `27/27` checks analyzed; `0` actionable layout dangers (`0` pad spacing, `0` soldermask bridge, `0` exposed trace, `0` sharp corner, `0` silkscreen danger) |
| **Lion Circuits Live BOM** | `https://www.lioncircuits.com/parts/bom-tool/6af6dd47e3e6758a9b7c5a6b` | **PASS** | `33/33` BOM lines (`81` parts/board) 100% in stock (`0` Out of Stock, `0` Limited Stock; `₹8,174.00` for 1 board / `₹28,048.00` for 6 boards incl. GST) |

---

## 2. Component Placement, Facing Direction, Pin-1, and Polarity Audit

### 2.1 Connectors, Switches, and Mechanical Spacers (`17` Key Mechanical Parts)

| Ref | MPN | Side | Position `(x, y)` mm | Rotation | Facing / Mating Direction | Pin-1 / Mechanical Verification |
|---|---|---|---|---|---|---|
| `J1` | `USB4105GFA` | Top (`F.Cu`) | `(51.25, 11.40)` | `90.0°` | Mouth faces **`+x` (Right edge `x=55.0 mm`)** | Overhangs right edge by `1.22 mm` into enclosure cutout `F4`; signal pads (`x=48.88 mm`) inside board; Pin `A1` (`GND`) at `(48.88, 14.75)` matches silkscreen/fab dot at `(-5.4, -2.4)` |
| `J4` | `10029449-111RLF` | Top (`F.Cu`) | `(49.00, 24.80)` | `90.0°` | Mouth faces **`+x` (Right edge `x=55.0 mm`)** | Overhangs right edge by `0.55 mm` into enclosure cutout `F5`; 19 SMT pads at `x=46.05 mm`; Pin `1` (`HDMI0_TX2_P`) at `(46.05, 20.05)` matches silkscreen/fab dot |
| `J2` | `629104190121` | Top (`F.Cu`) | `(16.00, 34.15)` | `0.0°` | Mouth faces **`+y` (Bottom edge `y=40.0 mm`)** | Overhangs bottom edge by `1.04 mm` into enclosure cutout `F6`; SMT pads `1..4` at `y=30.70 mm`; Pin `1` (`USB0_VBUS`) at `(12.47, 30.70)` (left) |
| `J3` | `629104190121` | Top (`F.Cu`) | `(35.50, 34.15)` | `0.0°` | Mouth faces **`+y` (Bottom edge `y=40.0 mm`)** | Overhangs bottom edge by `1.04 mm` into enclosure cutout `F7`; SMT pads `1..4` at `y=30.70 mm`; Pin `1` (`USB1_VBUS`) at `(31.97, 30.70)` (left) |
| `J5` | `SFW15R-1STE1LF` | Top (`F.Cu`) | `(13.50, 15.70)` | `90.0°` | FFC mouth & latch face **`+x` (Interior U-turn)** | Bottom-contact ZIF FFC socket under camera; pads `1..15` at `x=12.45 mm`; Pin `1` (`GND`) at `y=8.70 mm` and Pin `15` (`+3V3`) at `y=22.70 mm` align 1:1 with rotated AI Camera (`rot=90°`) via 180° FFC U-turn |
| `J6` | `10164227-1001A1RLF` | Bottom (`B.Cu`) | `(25.00, 37.00)` | `180.0°` | Mates **`-Z` (Downward to CM5 GPIO/Power)** | 100-pin 0.4 mm pitch mezzanine socket; Pin `1` (`GND`) at `(34.80, 38.54)` with `B.SilkS` pin-1 circle; Pin `99` (`PMIC_ENABLE`) at `(15.20, 38.54)`; `34.00 mm` Y-spacing from `J7` |
| `J7` | `10164227-1001A1RLF` | Bottom (`B.Cu`) | `(25.00, 3.00)` | `180.0°` | Mates **`-Z` (Downward to CM5 High-Speed)** | 100-pin 0.4 mm pitch mezzanine socket; Pin `1` (`USB_OTG_ID`, NC) at `(34.80, 4.54)` with `B.SilkS` pin-1 circle; Pin `100` (`HDMI0_SCL`) at `(15.20, 1.46)` |
| `SW1` | `PTS526SM15SMTR2LFS` | Top (`F.Cu`) | `(38.50, 27.30)` | `0.0°` | Actuates **`-Z` from Top (`+Z` plunger)** | Aligned under front shell power button (`F2`); Pads `1, 2` (`y=25.45`) on `PWR_BUT`, Pads `3, 4` (`y=28.80`) on `GND` |
| `SW2` | `B3U-1000P` | Top (`F.Cu`) | `(4.50, 10.50)` | `90.0°` | Actuates **`-Z` from Top (`+Z` pinhole)** | Aligned under front shell boot pinhole (`F3`); Pad `1` `(4.50, 12.20)` on `nRPIBOOT`, Pad `2` `(4.50, 8.80)` on `GND` |
| `SP1..SP4` | `9774080243R` | Top (`F.Cu`) | `(10.5/23.0, 5.2/26.2)` | `0.0°` | Mates **`+Z` (Upward to AI Camera)** | Four M2×8.0 mm internal-thread SMT spacers forming `12.5 x 21.0 mm` camera mounting rectangle (`rot=90°`), all grounded (`GND`) |
| `SP5..SP8` | `9774015960R` | Bottom (`B.Cu`) | `(3.5/51.5, 3.5/36.5)` | `0.0°` | Mates **`-Z` (Downward to CM5 corners)** | Four Ø3.3 mm ID × 1.5 mm SMT spacers coaxial with `H1..H4` (`48.0 x 33.0 mm` CM5 mounting rectangle), matching `1.5 mm` `J6`/`J7` stack height |

### 2.2 Integrated Circuits (`U1..U6`)

| Ref | MPN | Package | Position `(x, y)` mm | Rotation | Pin-1 Location & Orientation Check |
|---|---|---|---|---|---|
| `U1` | `TPD12S016PWR` | `TSSOP-24` | `(28.00, 18.80)` | `-90.0°` (`270°`) | Pin `1` (`+3V3`) at top-left `(24.98, 15.23)` with silkscreen dot; TMDS output pins `15..23` (`x=31.02 mm`) face `+x` directly toward HDMI `J4` (`x=46.05 mm`) |
| `U2` | `AP2553W6-7` | `SOT-26` | `(9.60, 20.50)` | `0.0°` | Pin `1` (`+5V` IN) at bottom-left `(8.65, 21.65)` with silkscreen dot; Pin `6` (`USB0_VBUS` OUT) at top-left `(8.65, 19.35)` |
| `U3` | `AP2553W6-7` | `SOT-26` | `(19.50, 25.40)` | `0.0°` | Pin `1` (`+5V` IN) at bottom-left `(18.55, 26.55)` with silkscreen dot; Pin `6` (`USB1_VBUS` OUT) at top-left `(18.55, 24.25)` |
| `U4` | `TPS259470ARPWR` | `VQFN-10` | `(39.50, 8.50)` | `180.0°` | Pin `1` (`VBUS_UVLO`) at bottom-right `(40.41, 9.40)` with silkscreen dot; Pin `5` (`VBUS_IN` bar) at `x=39.74` (right, toward `J1`) and Pin `6` (`+5V` bar) at `x=39.26` (left, toward interior) |
| `U5` | `TPS259470ARPWR` | `VQFN-10` | `(39.50, 13.50)` | `180.0°` | Pin `1` (`VBUS_U5_EN`) at bottom-right `(40.41, 14.40)` with silkscreen dot; Pin `5` (`VBUS_IN` bar) at `x=39.74` (right) and Pin `6` (`+5V` bar) at `x=39.26` (left) |
| `U6` | `TPD6S300ARUKR` | `WQFN-20` | `(42.50, 18.25)` | `180.0°` | Pin `1` at bottom-right `(44.00, 19.05)` with silkscreen dot; connector-side `C_CC1`/`C_CC2` (`x=44.00`) face `+x` toward `J1`, system-side `CC1`/`CC2` (`x=41.00`) face `-x` toward `J6` |

### 2.3 Polarized Polymer Tantalum Capacitors (`C26..C31`) and Diodes/TVS (`D1..D12`)

| Ref | MPN | Position `(x, y)` mm | Rotation | Polarity / Pin-1 Verification |
|---|---|---|---|---|
| `C26` | `T520B107M010ATE070` | `(3.50, 31.50)` | `0.0°` | Pad `1` (`+` Anode, silkscreen/fab dot) at `(5.30, 31.50)` on `/USB0_VBUS`; Pad `2` (`-` Cathode) at `(1.70, 31.50)` on `/GND` |
| `C27` | `T520B107M010ATE070` | `(25.75, 35.15)` | `180.0°` | Pad `1` (`+` Anode, silkscreen/fab dot) at `(23.95, 35.15)` on `/USB0_VBUS`; Pad `2` (`-` Cathode) at `(27.55, 35.15)` on `/GND` |
| `C28` | `T520B107M010ATE070` | `(26.25, 29.55)` | `0.0°` | Pad `1` (`+` Anode, silkscreen/fab dot) at `(28.05, 29.55)` on `/USB1_VBUS`; Pad `2` (`-` Cathode) at `(24.45, 29.55)` on `/GND` |
| `C29` | `T520B107M010ATE070` | `(32.65, 26.80)` | `-90.0°` (`270°`) | Pad `1` (`+` Anode, silkscreen/fab dot) at `(32.65, 28.60)` on `/USB1_VBUS`; Pad `2` (`-` Cathode) at `(32.65, 25.00)` on `/GND` |
| `C30` | `T520B107M010ATE070` | `(32.50, 12.20)` | `0.0°` | Pad `1` (`+` Anode, silkscreen/fab dot) at `(34.30, 12.20)` on `/+5V`; Pad `2` (`-` Cathode) at `(30.70, 12.20)` on `/GND` |
| `C31` | `T520B107M010ATE070` | `(32.50, 5.50)` | `0.0°` | Pad `1` (`+` Anode, silkscreen/fab dot) at `(34.30, 5.50)` on `/+5V`; Pad `2` (`-` Cathode) at `(30.70, 5.50)` on `/GND` |
| `D1..D3` | `USBLC6-2SC6` | `(47.45, 3.80)`, `(16.00, 25.95)`, `(28.00, 25.20)` | `0.0°` | Pin `1` at bottom-left with silkscreen dot; Pin `2` on `/GND`, Pin `5` on rail clamp (`VBUS_D1_CLAMP`, `USB0_VBUS`, `USB1_VBUS`), flow-through `D+/D-` pairs aligned |
| `D4` | `TVS2200DRVR` | `(45.30, 8.35)` | `90.0°` | Unidirectional 22 V surge TVS; Pins `4, 5, 6` (`y=7.32`, IN/Cathode) on `/VBUS_IN`, Pins `1, 2, 3, 7` (`y=9.38/8.35`, GND/Anode) on `/GND` |
| `D5..D7`, `D9..D11` | `TPD1E05U06DPYR` | See CPL | `-90°` / `0°` / `180°` | Unidirectional 5.5 V ESD TVS; Pad `1` (Cathode/IO, marked by silkscreen dot) on protected signal (`CC1`, `CC2`, `PWR_BUT`, `HDMI0_SCL`, `HDMI0_SDA`, `HDMI0_CEC`), Pad `2` (Anode) on `/GND` |
| `D8` | `PESD3V3S1BLYL` | `(6.50, 12.20)` | `90.0°` | Symmetric bidirectional 3.3 V ESD TVS; Pad `1` `(6.50, 12.62)` on `/nRPIBOOT`, Pad `2` `(6.50, 11.78)` on `/GND` |
| `D12` | `BAT54S` | `(38.50, 3.50)` | `90.0°` | Dual series Schottky; Pad `1` `(39.45, 2.35)` (Anode 1, silkscreen dot) on `/VBUS_AUXOFF`, Pad `2` `(37.55, 2.35)` (Cathode 2) on `/+5V`, Pad `3` `(38.50, 4.65)` (Common) on `/PMIC_ENABLE` |

---

## 3. Live JLCPCB Online DFM Verification (`jlcdfm.com`)

- **Viewer URL**: `https://jlcdfm.com/viewer?pcbUploadFileId=644061065261510657`
- **Detected Board**: `6 layer board of 40x55mm (1.575x2.165 inches)`
- **Analyzed Checks**: `27` checks (`0` unanalyzed)

| Section | DFM Check | Danger | Warning | Good | Disposition |
|---|---|---:|---:|---:|---|
| Routing layer analysis | `Sharp trace corner` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `BGA pad` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Via placed within a pad` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Trace to board edge` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Trace spacing` | `0` | `8` | `92` | **PASS** (`0.1524 mm` = `6 mil` controlled-impedance gap on `Diff90`/`Diff100`, above JLCPCB's `0.09 mm` 6L min) |
| Routing layer analysis | `Unconnected trace end` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Trace width` | `0` | `0` | `100` | **PASS** |
| Routing layer analysis | `Fiducial` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Pad to board edge` | `0` | `0` | `6` | **PASS** |
| Routing layer analysis | `Pad spacing` | `0` | `0` | `100` | **PASS** |
| Routing layer analysis | `Plated through-hole to trace clearance` | `0` | `0` | `32` | **PASS** |
| Routing layer analysis | `Annular ring` | `0` | `0` | `100` | **PASS** |
| Routing layer analysis | `tht to smd` | `21` | `13` | `22` | **EXPECTED (Datasheet Geometry)**: Fixed intra-footprint shield-slot/NPTH-peg to SMD pad spacing inside GCT `USB4105GFA` (`J1`), Amphenol `10029449-111RLF` (`J4`), and Wurth `629104190121` (`J2`, `J3`) |
| Routing layer analysis | `Via to pad` | `0` | `0` | `0` | **PASS** |
| Soldermask layer analysis | `Soldermask bridge` | `0` | `0` | `100` | **PASS** |
| Soldermask layer analysis | `Solder mask opening exposing trace` | `0` | `0` | `2` | **PASS** |
| Soldermask layer analysis | `Soldermask opening with multiple segments` | `0` | `5` | `0` | **INFO**: `U4`/`U5` VQFN-10 custom corner pad polygons |
| Soldermask layer analysis | `Negative soldermask expansion` | `0` | `0` | `0` | **PASS** |
| Silkscreen layer analysis | `Silkscreen to pad` | `0` | `2` | `24` | **PASS** (`0` dangers; `>= 0.135 mm` clearance) |
| Silkscreen layer analysis | `Silkscreen to hole` | `0` | `1` | `7` | **PASS** (`0` dangers; `>= 0.145 mm` clearance) |
| Silkscreen layer analysis | `Silkscreen line width` | `0` | `0` | `64` | **PASS** |
| Drill layer analysis | `Unconnected via` | `0` | `0` | `0` | **PASS** |
| Drill layer analysis | `Missing plated through-hole` | `0` | `1` | `0` | **INFO**: Intentional NPTH mounting hole |
| Drill layer analysis | `Plated through-hole spacing` | `0` | `0` | `0` | **PASS** |
| Drill layer analysis | `Short slot detection` | `0` | `0` | `0` | **PASS** |
| Drill layer analysis | `Slot width check` | `0` | `4` | `0` | **PASS** (`J1` `0.70 x 1.70 mm` and `0.70 x 1.40 mm` oval shield slots per GCT datasheet; above JLCPCB `0.50 mm` min) |
| Drill layer analysis | `Via to PTH spacing` | `0` | `0` | `0` | **PASS** |

---

## 4. Live Lion Circuits BOM Verification (`lioncircuits.com`)

- **Portal URL**: `https://www.lioncircuits.com/parts/bom-tool/6af6dd47e3e6758a9b7c5a6b`
- **BOM Files**: `fab/rpi-ai-cam-lc-bom.csv` and `fab/rpi-ai-cam-lc-bom-lioncircuits.csv`
- **Procurement Readiness**: **`100%` (`33` of `33` rows ready to procure; `20` Ready, `13` MOQ-Adjusted, `0` Out of Stock, `0` Limited Stock)**
- **Kit Pricing (1 Board)**: `₹6,926.84` subtotal + `₹1,246.83` GST (18%) = **`₹8,174.00`** (Free Shipping, `0` procurement fees)
- **Kit Pricing (6 Boards)**: `₹23,769.78` subtotal (`₹3,961.63`/board) + `₹4,278.56` GST (18%) = **`₹28,048.00`** (Free Shipping, `0` procurement fees)
- **Catalog MPN Normalization**: `J1` uses `USB4105GFA` (`389,128` in stock at `₹101.96`), which is Lion Circuits' unhyphenated catalog identifier for GCT `USB4105-GF-A`.
