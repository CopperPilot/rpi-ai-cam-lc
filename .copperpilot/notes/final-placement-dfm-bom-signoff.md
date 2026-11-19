# Final Placement, Orientation, Mechanical Clearance (`C1`, `D12`, `J1–J5`, `SP1–SP8`), JLCPCB DFM, and Lion Circuits BOM Sign-Off Report

## 1. Executive Summary

| Verification Domain | Target / Tool | Status | Key Result |
|---|---|---|---|
| **Schematic ERC** | `hardware/rpi-ai-cam-lc.kicad_sch` (`kicad-cli 10.0.4`) | **PASS** | `0` errors, `0` warnings |
| **Main PCB DRC & Parity** | `hardware/rpi-ai-cam-lc.kicad_pcb` (`55.0 x 40.0 mm`, 6L) | **PASS** | `0` DRC errors, `0` warnings, `0` unconnected, `0` parity errors, `0` courtyard overlaps |
| **2-Up Panel PCB DRC** | `fab/panel/rpi-ai-cam-lc-panel.kicad_pcb` (`113.0 x 56.0 mm`, 6L) | **PASS** | `0` DRC errors, `0` warnings, `0` unconnected items |
| **CPL / POS / Panel Sync** | `81` placements (`75` Top, `6` Bottom) across PCB, Panel, CPL, POS | **PASS** | `0` coordinate, rotation, or side mismatches (`< 0.001 mm`, `0.0 deg`) |
| **Dedicated Part Audit (`C1`, `D12`, `J1–J5`, `SP1–SP8`)** | Courtyard, Fab Body, Copper Pad, and PTH/NPTH Drill Clearances | **PASS** | Resolved same-net `/GND` pad/drill overlap between `C1` Pad 1 and `J4` Pad 20 by shifting `C1` from `(47.35, 15.40)` to `(47.35, 14.65)` (`+0.195 mm` copper gap, `+0.545 mm` drill gap, `1.150 mm` courtyard gap to `J4`, `0.900 mm` courtyard gap to `J1`) |
| **JLCPCB Live DFM** | `https://jlcdfm.com/viewer?pcbUploadFileId=646166314504847361` | **PASS** | `31/31` checks analyzed (`28/31` at `0` dangers and `0` warnings; `0` pad spacing, `0` trace spacing, `0` soldermask bridge, `0` exposed trace, `0` sharp corner, `0` slot width, `0` missing PTH, and `0` silkscreen-to-pad/hole dangers or warnings) |
| **Lion Circuits Live BOM** | `https://www.lioncircuits.com/parts/bom-tool/6af6dd47e3e6758a9b7c5a6b` | **PASS** | `33/33` BOM lines (`81` parts/board) 100% in stock (`0` Out of Stock, `0` Limited Stock; `₹8,174.00` for 1 board / `₹28,048.00` for 6 boards incl. GST) |

---

## 2. Detailed Mechanical, Courtyard, Pad, and Assembly Audit: `C1`, `D12`, `J1`, `J2`, `J3`, `J4`, `J5`, and `SP1–SP8`

| Ref | MPN / Package | Layer & Pose `(x, y, rot)` | Courtyard & Physical Body Clearances | Pad-to-Pad & Pad-to-Drill Clearances | Assembly & Orientation Readiness |
|---|---|---|---|---|---|
| **`C1`** | `CL21B225KBYNNWE` (`2.2uF 50V 0805`) | `F.Cu` at `(47.35, 14.65, 90.0°)` | Courtyard `(46.73..47.97, 13.65..15.65)`: **`1.150 mm`** to `J4`, **`0.900 mm`** to `J1`, **`2.544 mm`** to `C33`, **`2.747 mm`** to `U6` | **Fixed:** Shifted `-0.75 mm` Y from `15.40` to `14.65 mm` (and `/C_CC1` via from `(46.15, 13.508)` to `(45.60, 13.25)`), eliminating a `-0.555 mm` same-net `/GND` copper overlap and `-0.205 mm` drill overlap with `J4` Pad 20 (`(47.05, 17.55)`). Now **`+0.195 mm`** copper gap and **`+0.545 mm`** drill gap to `J4.20`, and **`+0.280 mm`** to `J1.A1` | Non-polarized 0805 MLCC (`Pad 1` `/GND` at `(47.35, 15.65)`, `Pad 2` `/VBUS_IN` at `(47.35, 13.65)`). Completely isolated solder paste aperture prevents solder thief into `J4` PTH shield hole |
| **`D12`** | `BAT54S` (`SOT-23`) | `F.Cu` at `(38.50, 3.50, 90.0°)` | Courtyard `(37.05..39.95, 2.85..4.15)`: **`0.250 mm`** to `R19` `(40.20..41.20, 3.75..4.25)`, **`0.689 mm`** to `C32`, **`1.200 mm`** to `R5`, **`2.800 mm`** to `C31` | **`+0.180 mm`** to `R5.1`, **`+0.547 mm`** to `U4.1`, **`+0.911 mm`** to `R19.2`, **`+1.080 mm`** to `C32.1` | Dual series Schottky: `Pad 1` `(39.45, 2.35)` (Anode 1, pin-1 dot) on `/VBUS_AUXOFF`, `Pad 2` `(37.55, 2.35)` (Cathode 2) on `/+5V`, `Pad 3` `(38.50, 4.65)` (Common) on `/PMIC_ENABLE` |
| **`J1`** | `USB4105GFA` (GCT 16-pin USB-C) | `F.Cu` at `(51.25, 11.40, 90.0°)` | Courtyard `(48.87..56.22, 6.93..15.87)`: **`0.930 mm`** to `J4` (`1.430 mm` housing gap), **`0.900 mm`** to `C1`, **`1.470 mm`** to `C4`, **`2.320 mm`** to `D1` | **`+0.254 mm`** copper gap and **`+0.804 mm`** drill gap between `J1` Pad 4 oval shield slot `(53.27, 15.72)` and `J4` Pad 20 PTH `(51.95, 16.95)`; **`+0.280 mm`** to `C1.2` | Mouth faces **`+x` (`x=55.0 mm`)** with `1.22 mm` overhang into enclosure cutout `F4`; two Ø0.65 mm NPTH locating pegs `(50.03, 8.50)` and `(50.03, 14.30)` seated cleanly |
| **`J2`** | `629104190121` (Wurth USB-A 2.0) | `F.Cu` at `(16.00, 34.15, 0.0°)` | Courtyard `(9.00..23.00, 30.10..41.04)`: **`0.650 mm`** to `C27`, **`0.850 mm`** to `C28`, **`1.500 mm`** to `C9`, **`3.500 mm`** to `C26` | **`+0.455 mm`** to `C9.1`, **`+0.517 mm`** to `C26.1`, **`+0.522 mm`** to `C27.1`, **`+0.702 mm`** to `C28.2` | Mouth faces **`+y` (`y=40.0 mm`)** with `1.04 mm` overhang into enclosure cutout `F6`; Pin 1 (`/USB0_VBUS`) at `(12.47, 30.70)`; 4 SMD shield pads + 2 NPTH locating pegs |
| **`J3`** | `629104190121` (Wurth USB-A 2.0) | `F.Cu` at `(35.50, 34.15, 0.0°)` | Courtyard `(28.50..42.50, 30.10..41.04)`: **`0.650 mm`** to `C27`, **`0.850 mm`** to `C28`, **`1.900 mm`** to `SW1`, **`2.900 mm`** to `C29` | **`+0.296 mm`** to `C29.1`, **`+0.550 mm`** to `SW1.3`, **`+0.552 mm`** to `C27.2`, **`+0.552 mm`** to `C28.1` | Mouth faces **`+y` (`y=40.0 mm`)** with `1.04 mm` overhang into enclosure cutout `F7`; Pin 1 (`/USB1_VBUS`) at `(31.97, 30.70)`; `5.50 mm` courtyard gap to `J2` |
| **`J4`** | `10029449-111RLF` (Amphenol HDMI-A) | `F.Cu` at `(49.00, 24.80, 90.0°)` | Courtyard `(45.35..55.55, 16.80..32.80)`: **`0.930 mm`** to `J1`, **`1.150 mm`** to `C1`, **`1.425 mm`** to `U6`, **`1.930 mm`** to `C8` | **`+0.195 mm`** copper gap and **`+0.545 mm`** drill gap to `C1.1`; **`+0.254 mm`** copper gap and **`+0.804 mm`** drill gap to `J1.4`; **`+0.351 mm`** drill-to-pad gap to bottom-side `SP8` (`(51.50, 36.50)`) | Mouth faces **`+x` (`x=55.0 mm`)** with `0.55 mm` overhang into enclosure cutout `F5`; Pin 1 (`HDMI0_TX2_P`) at `(46.05, 20.05)`; 4 PTH shield tabs (`Pad 20`, Ø1.30 mm drill / Ø2.00 mm pad) |
| **`J5`** | `SFW15R-1STE1LF` (Amphenol 15-pin FFC) | `F.Cu` at `(13.50, 15.70, 90.0°)` | Courtyard `(11.80..17.75, 5.20..26.20)`: **`1.119 mm`** to `SP1`/`SP3` (`F.CrtYd` circles, **`0.719 mm`** to `Ø4.4 mm` solder ring), **`1.202 mm`** to `U3`, **`1.610 mm`** to `C5`/`C6` | **`+0.822 mm`** to `C11.1`, **`+1.119 mm`** to `SP1.1` / `SP3.1`, **`+1.476 mm`** to `C10.2` | Bottom-contact 1.0 mm ZIF FFC socket under AI Camera; FFC mouth & latch face **`+x`**; Pin 1 (`GND`) at `(12.45, 8.70)` and Pin 15 (`+3V3`) at `(12.45, 22.70)` |
| **`SP1–SP4`** | `9774080243R` (Wurth M2×8.0 mm SMT Spacer) | `F.Cu` at `(10.5, 5.2)`, `(23.0, 5.2)`, `(10.5, 26.2)`, `(23.0, 26.2)` (`rot=0.0°`) | `12.50 x 21.00 mm` rectangle matching rotated AI Camera M2 holes (`100%` coaxial with `CameraHole_M2`). Closest neighbor: `SP1`/`SP3` to `J5` (`1.119 mm` courtyard, `0.719 mm` pad-to-body) | Pad `1` (`Ø4.40 mm` copper ring, `Ø2.80 mm` NPTH drill for `Ø2.80 mm` alignment spigot; M2 thread starts at `Z=0..8.0 mm` above `F.Cu` and does not protrude through PCB). Zero foreign copper inside `r < 2.20 mm` on any layer (`closest inner trace at r=2.074 mm on In2.Cu > r_drill=1.40 mm by 0.674 mm`) | Top-side (`F.Cu`) SMT reflow spacers (`GND`) supporting the AI Camera at `Z=+10.6 mm` above `F.Cu` (`8.0 mm` spacer + `2 × 0.5 mm` nylon washers) |
| **`SP5–SP8`** | `9774015960R` (Wurth Ø3.3 mm ID × 1.5 mm SMT Spacer) | `B.Cu` at `(3.5, 3.5)`, `(51.5, 3.5)`, `(3.5, 36.5)`, `(51.5, 36.5)` (`rot=0.0°`) | `48.00 x 33.00 mm` rectangle matching CM5 corner mounting holes (`100%` coaxial with `H1..H4` `MountingHole_4.4mm`). All top-side components (`C26`, `J2`, `J3`, `J4`) are strictly on `F.Cu` while `SP5..SP8` are on `B.Cu` | Pad `1` (`Ø6.00 mm` `B.Cu` ring, `Ø4.20 mm` drill coaxial with `H1..H4` `Ø4.40 mm` NPTH drill for `Ø4.17 mm` spacer spigot). `SP8` (`B.Cu`) has `+0.351 mm` clearance to `J4.20` (`(51.95, 32.65)`) PTH drill hole (`r=0.65 mm`) | Bottom-side (`B.Cu`) SMT reflow spacers (`GND`) matching `1.5 mm` `J6`/`J7` mezzanine height; M2.5 screws pass from rear shell through CM5, `SP5..SP8`/`H1..H4`, and thread into front shell brass heat-set inserts |

---

## 3. Component Placement, Facing Direction, Pin-1, and Polarity Audit

### 3.1 Connectors, Switches, and Mechanical Spacers (`17` Key Mechanical Parts)

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

### 3.2 Integrated Circuits (`U1..U6`)

| Ref | MPN | Package | Position `(x, y)` mm | Rotation | Pin-1 Location & Orientation Check |
|---|---|---|---|---|---|
| `U1` | `TPD12S016PWR` | `TSSOP-24` | `(28.00, 18.80)` | `-90.0°` (`270°`) | Pin `1` (`+3V3`) at top-left `(24.98, 15.23)` with silkscreen dot; TMDS output pins `15..23` (`x=31.02 mm`) face `+x` directly toward HDMI `J4` (`x=46.05 mm`) |
| `U2` | `AP2553W6-7` | `SOT-26` | `(9.60, 20.50)` | `0.0°` | Pin `1` (`+5V` IN) at bottom-left `(8.65, 21.65)` with silkscreen dot; Pin `6` (`USB0_VBUS` OUT) at top-left `(8.65, 19.35)` |
| `U3` | `AP2553W6-7` | `SOT-26` | `(19.50, 25.40)` | `0.0°` | Pin `1` (`+5V` IN) at bottom-left `(18.55, 26.55)` with silkscreen dot; Pin `6` (`USB1_VBUS` OUT) at top-left `(18.55, 24.25)` |
| `U4` | `TPS259470ARPWR` | `VQFN-10` | `(39.50, 8.50)` | `180.0°` | Pin `1` (`VBUS_UVLO`) at bottom-right `(40.41, 9.40)` with silkscreen dot; Pin `5` (`VBUS_IN` bar) at `x=39.74` (right, toward `J1`) and Pin `6` (`+5V` bar) at `x=39.26` (left, toward interior) |
| `U5` | `TPS259470ARPWR` | `VQFN-10` | `(39.50, 13.50)` | `180.0°` | Pin `1` (`VBUS_U5_EN`) at bottom-right `(40.41, 14.40)` with silkscreen dot; Pin `5` (`VBUS_IN` bar) at `x=39.74` (right) and Pin `6` (`+5V` bar) at `x=39.26` (left) |
| `U6` | `TPD6S300ARUKR` | `WQFN-20` | `(42.50, 18.25)` | `180.0°` | Pin `1` at bottom-right `(44.00, 19.05)` with silkscreen dot; connector-side `C_CC1`/`C_CC2` (`x=44.00`) face `+x` toward `J1`, system-side `CC1`/`CC2` (`x=41.00`) face `-x` toward `J6` |

### 3.3 Polarized Polymer Tantalum Capacitors (`C26..C31`) and Diodes/TVS (`D1..D12`)

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

## 4. Live JLCPCB Online DFM Verification (`jlcdfm.com`)

- **Viewer URL**: `https://jlcdfm.com/viewer?pcbUploadFileId=646166314504847361`
- **Summary Artifact**: `./.copperpilot/fab/jlcpcb/dfm/20261119-090553-summary.json` (and `./.copperpilot/fab/jlcpcb/shots/20261119-090553-dfm-overview.png`)
- **Detected Board**: `6 layer board of 40x55mm (1.575x2.165 inches)`
- **Analyzed Checks**: `31` checks (`0` unanalyzed; `28/31` checks at `0` dangers and `0` warnings)

| Section | DFM Check | Danger | Warning | Good | Disposition |
|---|---|---:|---:|---:|---|
| Routing layer analysis | `Sharp trace corner` | `0` | `0` | `0` | **PASS** (`0` `90°`/acute corners across all `1,396` copper segments) |
| Routing layer analysis | `BGA pad` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Via placed within a pad` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Trace to board edge` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Trace spacing` | `0` | `0` | `102` | **PASS** (`0` dangers, `0` warnings) |
| Routing layer analysis | `Unconnected trace end` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Trace width` | `0` | `0` | `100` | **PASS** |
| Routing layer analysis | `Fiducial` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Pad to board edge` | `0` | `0` | `0` | **PASS** |
| Routing layer analysis | `Pad spacing` | `0` | `0` | `100` | **PASS** |
| Routing layer analysis | `Plated through-hole to trace clearance` | `0` | `0` | `17` | **PASS** |
| Routing layer analysis | `Annular ring` | `0` | `0` | `100` | **PASS** |
| Routing layer analysis | `tht to smd` | `3` | `1` | `0` | **EXPECTED (Datasheet Geometry)**: Advisory wave-soldering fixture spacing threshold (`2.03 mm / 3.05 mm`) on `B.Cu` between `SP6`/`SP8` bottom corner spacers (`(51.5, 3.5)` and `(51.5, 36.5)`) and `J1`/`J4` oval PTH shield tabs; top copper `F.Cu` has `0` `tht to smd` dangers or warnings |
| Routing layer analysis | `Via to pad` | `0` | `0` | `0` | **PASS** |
| Soldermask layer analysis | `Soldermask bridge` | `0` | `0` | `100` | **PASS** |
| Soldermask layer analysis | `Solder mask opening exposing trace` | `0` | `0` | `2` | **PASS** |
| Soldermask layer analysis | `Soldermask opening with multiple segments` | `0` | `0` | `0` | **PASS** (`0` dangers, `0` warnings) |
| Soldermask layer analysis | `Negative soldermask expansion` | `0` | `0` | `0` | **PASS** |
| Silkscreen layer analysis | `Silkscreen to pad` | `0` | `0` | `26` | **PASS** (`0` dangers, `0` warnings; `>= 0.210 mm` clearance) |
| Silkscreen layer analysis | `Silkscreen to hole` | `0` | `0` | `9` | **PASS** (`0` dangers, `0` warnings; `>= 0.192 mm` clearance) |
| Silkscreen layer analysis | `Silkscreen line width` | `0` | `0` | `64` | **PASS** |
| Drill layer analysis | `Unconnected via` | `0` | `0` | `0` | **PASS** |
| Drill layer analysis | `Missing plated through-hole` | `0` | `0` | `0` | **PASS** (`0` dangers, `0` warnings) |
| Drill layer analysis | `Plated through-hole spacing` | `0` | `0` | `0` | **PASS** |
| Drill layer analysis | `Pth without pad` | `0` | `16` | `0` | **INFO**: `10` intentional NPTH drill holes (`4 × H1..H4` + `2 × J1` pegs + `4 × J2/J3` pegs) in `rpi-ai-cam-lc-NPTH.drl` |
| Drill layer analysis | `Short slot detection` | `0` | `6` | `0` | **INFO**: `J1` and `J4` oval PTH shield slots (`0.85 x 1.70 mm`, `0.85 x 1.40 mm`, and `1.00 x 1.40 mm`), above JLCPCB `0.85 mm` slot width alert threshold |
| Drill layer analysis | `Slot width check` | `0` | `0` | `0` | **PASS** (`0` dangers, `0` warnings) |
| Drill layer analysis | `Via to PTH spacing` | `0` | `0` | `0` | **PASS** |
| Drill layer analysis | `Via without pad` | `0` | `0` | `0` | **PASS** |

---

## 5. Live Lion Circuits BOM Verification (`lioncircuits.com`)

- **Portal URL**: `https://www.lioncircuits.com/parts/bom-tool/6af6dd47e3e6758a9b7c5a6b`
- **BOM Files**: `fab/rpi-ai-cam-lc-bom.csv` and `fab/rpi-ai-cam-lc-bom-lioncircuits.csv`
- **Procurement Readiness**: **`100%` (`33` of `33` rows ready to procure; `20` Ready, `13` MOQ-Adjusted, `0` Out of Stock, `0` Limited Stock)**
- **Kit Pricing (1 Board)**: `₹6,926.84` subtotal + `₹1,246.83` GST (18%) = **`₹8,174.00`** (Free Shipping, `0` procurement fees)
- **Kit Pricing (6 Boards)**: `₹23,769.78` subtotal (`₹3,961.63`/board) + `₹4,278.56` GST (18%) = **`₹28,048.00`** (Free Shipping, `0` procurement fees)
- **Catalog MPN Normalization**: `J1` uses `USB4105GFA` (`389,128` in stock at `₹101.96`), which is Lion Circuits' unhyphenated catalog identifier for GCT `USB4105-GF-A`.
