# Compact CM5 AI Camera (`rpi-ai-cam-lc`) — Project Index

## Overview
- **Product:** Compact CM5 AI Camera (`55.0 x 40.0 mm`, `3.0 mm` corner radius, 6-layer `1.6 mm` nominal / `1.65 mm` finished carrier PCB with 2-up `113.1 x 56.1 mm` assembly panel).
- **Primary KiCad Files:**
  - Schematic: `hardware/rpi-ai-cam-lc.kicad_sch` (A2 sheet, 8 functional module containers, 84 components, 174 nets)
  - PCB: `hardware/rpi-ai-cam-lc.kicad_pcb` (6 copper layers: `F.Cu`, `In1.Cu`, `In2.Cu`, `In3.Cu`, `In4.Cu`, `B.Cu`)
  - Project Settings: `hardware/rpi-ai-cam-lc.kicad_pro`
  - 2-Up Assembly Panel: `fab/panel/rpi-ai-cam-lc-panel.kicad_pcb`, `fab/panel/rpi-ai-cam-lc-panel.kicad_pro`, `fab/panel/fp-lib-table`
- **Fabrication & Assembly Package:** `fab/` (`fab/rpi-ai-cam-lc-gerbers.zip`, `fab/rpi-ai-cam-lc-panel-gerbers.zip`, `fab/rpi-ai-cam-lc-bom.csv`, `fab/rpi-ai-cam-lc-bom-lioncircuits.csv`, `fab/rpi-ai-cam-lc-cpl.csv`, `fab/rpi-ai-cam-lc-panel-cpl.csv`, `fab/rpi-ai-cam-lc-pos-top.csv`, `fab/rpi-ai-cam-lc-pos-bottom.csv`, `fab/rpi-ai-cam-lc-pos.zip`, `fab/rpi-ai-cam-lc.step`, `fab/rpi-ai-cam-lc-schematic.pdf`).

## Architecture & Power Budget
- **USB-C Input (`J1`, `USB4105-GF-A` / Lion Circuits MPN `USB4105GFA`):** Protected by `D4` (`TVS2200DRVR` 22 V flat-clamp surge TVS), `U6` (`TPD6S300ARUKR` 24 V CC1/CC2 OVP + IEC 61000-4-2 ESD + dead-battery Rd), `D1` (`USBLC6-2SC6`), and `2.3 uF` nominal (`C1 = 2.2 uF 50 V` + `C4 = 100 nF 50 V` <= `10 uF` USB-C `cSink` limit).
- **Parallel Ideal-Diode / OVP eFuses (`U4`, `U5`, `TPS259470ARPWR`):** Active-standby parallel stage (`R_ON(typ) = 14.15 mOhm` combined, `I_LIM(typ) = 2.50 A` per channel / `5.0 A` combined via `R17 = R18 = 1.33 kOhm`, `C22 = 4.7 nF` soft-start, `R12/R13/R14` setting `UVLO_R = 4.18 V` and `OVLO_R = 6.13 V` typ, and `D12` `BAT54S` + `R19` + `C32` shaping `PMIC_ENABLE`).
- **Dual USB 2.0 Host Ports (`J2`, `J3`, `629104190121`):** Controlled by `U2`/`U3` (`AP2553W6-7`, `R1 = R2 = 43 kOhm` for `0.615 A` typ limit, `222 uF` nominal polymer tantalum + MLCC output storage per port, `U3` independently gated by `GPIO26` / `USB1_VBUS_EN` with `22 kOhm` pull-down `R11` so boot load stays `<= 2.935 A`).
- **HDMI 0 Output (`J4`, `10029449-111RLF`):** Conditioned by `U1` (`TPD12S016PWR`, `55 mA` `5V_OUT`, `LS_OE = GND`, TMDS ESD protection) and `D9..D11` (`TPD1E05U06DPYR` on `HDMI0_SCL`/`SDA`/`CEC`).
- **CAM0 2-Lane MIPI CSI-2 (`J5`, `SFW15R-1STE1LF`):** 15-pin 1.0 mm bottom-contact FFC socket connected via 50 mm same-side FFC (`686615050001`) to the IMX500 AI Camera (`SC1174`) on four 8.0 mm SMT spacers (`SP1..SP4`).

## Reports & Notes
- [Schematic Review, Thermal, EMI & Layout Cleanup Report](notes/design-review-and-cleanup.md)
- [DFM & Assembly Readiness Report](notes/dfm-and-assembly-readiness.md)
- [Lion Circuits BOM Availability & Procurement Report](notes/lioncircuits-bom-availability-report.md)
