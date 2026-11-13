# Compact CM5 AI Camera (`rpi-ai-cam-lc`) — Lion Circuits BOM Availability & Procurement Readiness Report

## 1. Executive Summary

- **Live Lion Circuits BOM Tool Verification (`https://www.lioncircuits.com/parts/bom-tool/6af6dd47e3e6758a9b7c5a6b`):** **100% Available (`33 / 33` BOM lines in stock, `81 / 81` component placements per board, `noOfNotAvailable = 0`)**.
- **Single MPN Indexing Resolution (`J1`):**
  - On initial upload of `fab/rpi-ai-cam-lc-bom-lioncircuits.csv`, `32 / 33` BOM lines matched in stock immediately, while row 13 (`J1`, `GCT USB4105-GF-A` 16-pin USB 2.0 Type-C horizontal SMT receptacle) reported `Not Available` because Lion Circuits' parts database indexes this exact GCT part without hyphens as **`USB4105GFA`** (verified against Lion Circuits' hosted datasheet `1_usb4105-spec.pdf` and manufacturer image `1_MFGUSB4105-GF-A.jpg`).
  - Updating `J1`'s `MPN` to **`USB4105GFA`** resolves row 13 with **`389,128` units in stock** at **`₹101.96` / unit** (`MOQ = 1`, `status = ready`).
- **Synchronized Design & Manufacturing Files:**
  - Updated `J1` `MPN` to `USB4105GFA` (preserving `Value = USB4105-GF-A`, `Footprint = lcsc:TYPE-C-SMD_SBC-160S1A-20-S412`, `LCSC = C3020560`, and `Datasheet = https://www.lcsc.com/datasheet/C3020560.pdf`) across:
    - `hardware/rpi-ai-cam-lc.kicad_sch`
    - `hardware/rpi-ai-cam-lc.kicad_pcb`
    - `hardware/lcsc.kicad_sym`
    - `hardware/lcsc.pretty/TYPE-C-SMD_SBC-160S1A-20-S412.kicad_mod`
    - `fab/panel/rpi-ai-cam-lc-panel.kicad_pcb`
    - `fab/rpi-ai-cam-lc-bom.csv`
    - `fab/rpi-ai-cam-lc-bom-lioncircuits.csv`
    - `rea/spec.yaml` and `rea/spec.locked.yaml`
- **KiCad Verification After MPN Sync:**
  - Schematic ERC (`hardware/rpi-ai-cam-lc.kicad_sch`): **`0` errors, `0` warnings**
  - Main PCB DRC & Schematic Parity (`hardware/rpi-ai-cam-lc.kicad_pcb`): **`0` errors, `0` warnings, `0` unconnected items, `0` schematic parity mismatches**
  - 2-Up Panel PCB DRC (`fab/panel/rpi-ai-cam-lc-panel.kicad_pcb`): **`0` errors, `0` warnings, `0` unconnected items**

---

## 2. Lion Circuits Live Component Kit Pricing Summary

| Build Quantity | Available Lines | Unavailable Lines | Component Kit Subtotal (INR) | Per-Board Component Cost (INR) | GST @ 18% (INR) | Total Component Kit Cost incl. GST (INR) |
|---|---:|---:|---:|---:|---:|---:|
| **1 Board (Prototype)** | `33 / 33` | `0` | `₹6,926.84` | `₹6,926.84` | `₹1,246.83` | **`₹8,174.00`** |
| **6 Boards (Owner Target Run)** | `33 / 33` | `0` | `₹23,769.78` | `₹3,961.63` | `₹4,278.56` | **`₹28,048.00`** |

*(Note: In Lion Circuits' BOM Tool, passive lines marked `adjusted` indicate automatic reel/cut-tape minimum line-value rounding to ~₹100 while being 100% in stock with `noOfNotAvailable: 0`.)*

---

## 3. Complete 33-Line BOM Availability Table (Verified on Lion Circuits for 6 Boards)

| # | Designators | Qty / Board | Req Qty (6 Boards) | Order Qty (6 Boards) | Lion Circuits MPN | Manufacturer | Package / Footprint | Lion Stock | Unit Price (INR) | Line Total for 6 Boards (INR) | Lion Status |
|---:|---|---:|---:|---:|---|---|---|---:|---:|---:|---|
| 1 | `C1` | 1 | 6 | 9 | `CL21B225KBYNNWE` | Samsung Electro-Mechanics | `C0805` | `793` | `₹12.22` | `₹109.99` | In Stock (`adjusted`) |
| 2 | `C8, C10, C11, C12, C34` | 5 | 30 | 30 | `GRM155R61E105KE11J` | Murata | `C0402` | `434,522` | `₹7.27` | `₹109.10` | In Stock (`ready`) |
| 3 | `C2, C3, C19` | 3 | 18 | 18 | `CL10A226MO7JZNC` | Samsung Electro-Mechanics | `C0603` | `104,501` | `₹56.70` | `₹274.70` | In Stock (`ready`) |
| 4 | `C4, C5, C6, C7, C20, C21, C25, C33` | 8 | 48 | 52 | `GRM155R71H104KE14D` | Murata | `C0402` | `944,740` | `₹1.94` | `₹482.09` | In Stock (`adjusted`) |
| 5 | `C22, C23, C24` | 3 | 18 | 49 | `GRM155R71H472KA01D` | Murata | `C0402` | `58,853` | `₹2.04` | `₹107.02` | In Stock (`adjusted`) |
| 6 | `C26, C27, C28, C29, C30, C31` | 6 | 36 | 36 | `T520B107M010ATE070` | KEMET | `CAP-SMD_L3.5-W2.8` | `6,835` | `₹37.91` | `₹326.69` | In Stock (`ready`) |
| 7 | `C9, C32` | 2 | 12 | 13 | `GRM188Z71E225KE43D` | Murata | `C0603` | `126,100` | `₹7.92` | `₹102.34` | In Stock (`adjusted`) |
| 8 | `D1, D2, D3` | 3 | 18 | 18 | `USBLC6-2SC6` | STMicroelectronics | `SOT-23-6_L2.9-W1.6-P0.95-LS2.8-BL` | `26,780` | `₹19.99` | `₹184.18` | In Stock (`ready`) |
| 9 | `D5, D6, D7, D9, D10, D11` | 6 | 36 | 36 | `TPD1E05U06DPYR` | Texas Instruments | `X1SON-2_L1.0-W0.6-P0.65-RD-1` | `55,840` | `₹6.71` | `₹336.48` | In Stock (`ready`) |
| 10 | `D12` | 1 | 6 | 9 | `BAT54S` | Rectron | `SOT-23_L2.9-W1.3-P1.90-LS2.4-BR` | `13,629` | `₹11.69` | `₹112.13` | In Stock (`adjusted`) |
| 11 | `D4` | 1 | 6 | 6 | `TVS2200DRVR` | Texas Instruments | `WSON-6_L2.0-W2.0-P0.65-TL-EP` | `514` | `₹179.70` | `₹179.70` | In Stock (`ready`) |
| 12 | `D8` | 1 | 6 | 6 | `PESD3V3S1BLYL` | Nexperia | `DFN1006-2L-BI` | `52,527` | `₹26.76` | `₹107.04` | In Stock (`ready`) |
| 13 | **`J1`** | **1** | **6** | **6** | **`USB4105GFA`** *(updated from `USB4105-GF-A`)* | **GCT** | **`TYPE-C-SMD_SBC-160S1A-20-S412`** | **`389,128`** | **`₹101.96`** | **`₹101.96`** | **In Stock (`ready`)** |
| 14 | `J2, J3` | 2 | 12 | 12 | `629104190121` | Wurth Elektronik | `USB-A-SMD_629104190121` | `20,502` | `₹159.32` | `₹382.35` | In Stock (`ready`) |
| 15 | `J4` | 1 | 6 | 6 | `10029449-111RLF` | Amphenol ICC / FCI | `HDMI-SMD_10029449-001RLF` | `7,777` | `₹85.79` | `₹171.59` | In Stock (`ready`) |
| 16 | `J5` | 1 | 6 | 6 | `SFW15R-1STE1LF` | Amphenol Communications Solutions | `CONN-SMD_15P-P0.50_SFW15R-1STE1LF` | `3,028` | `₹79.56` | `₹159.11` | In Stock (`ready`) |
| 17 | `J6, J7` | 2 | 12 | 12 | `10164227-1001A1RLF` | Amphenol Communications Solutions | `CONN-SMD_100P-P0.40_10164227-1001A1RLF` | `7,426` | `₹186.45` | `₹440.03` | In Stock (`ready`) |
| 18 | `R1, R2, R16` | 3 | 18 | 99 | `RC0402FR-0743KL` | Yageo | `R0402` | `6,978` | `₹1.02` | `₹109.68` | In Stock (`adjusted`) |
| 19 | `R6, R7, R10, R11` | 4 | 24 | 98 | `RC0402FR-0722KL` | Yageo | `R0402` | `191,802` | `₹1.02` | `₹102.28` | In Stock (`adjusted`) |
| 20 | `R12` | 1 | 6 | 8 | `RC0402FR-07390KL` | Yageo | `R0402` | `62,694` | `₹13.45` | `₹107.63` | In Stock (`adjusted`) |
| 21 | `R13` | 1 | 6 | 9 | `RC0402FR-0749K9L` | Yageo | `R0402` | `206,405` | `₹11.36` | `₹102.28` | In Stock (`adjusted`) |
| 22 | `R14` | 1 | 6 | 9 | `RC0402FR-07107KL` | Yageo | `R0402` | `6,319` | `₹11.36` | `₹102.28` | In Stock (`adjusted`) |
| 23 | `R8, R9, R15, R20` | 4 | 24 | 202 | `RC0402FR-07100KL` | Yageo | `R0402` | `115,382` | `₹0.50` | `₹100.48` | In Stock (`adjusted`) |
| 24 | `R5, R17, R18` | 3 | 18 | 98 | `RC0402FR-071K33L` | Yageo | `R0402` | `82,241` | `₹1.02` | `₹102.28` | In Stock (`adjusted`) |
| 25 | `R19` | 1 | 6 | 74 | `RC0402FR-076K8L` | Yageo | `R0402` | `78,345` | `₹1.37` | `₹101.35` | In Stock (`adjusted`) |
| 26 | `SP1, SP2, SP3, SP4` | 4 | 24 | 24 | `9774080243R` | Würth Elektronik | `SMD-1_BD4.4-D2.8` | `589` | `₹101.94` | `₹466.10` | In Stock (`ready`) |
| 27 | `SP5, SP6, SP7, SP8` | 4 | 24 | 24 | `9774015960R` | Würth Elektronik | `SMD_BD6.0-D4.2` | `9,018` | `₹225.59` | `₹938.01` | In Stock (`ready`) |
| 28 | `SW1` | 1 | 6 | 6 | `PTS526SM15SMTR2LFS` | C&K Components | `SW-SMD_4P-L5.2-W5.2-P3.70-LS6.4` | `52,986` | `₹20.40` | `₹101.98` | In Stock (`ready`) |
| 29 | `SW2` | 1 | 6 | 6 | `B3U-1000P` | Omron | `KEY-SMD_B3U-1000PM` | `71,415` | `₹25.91` | `₹112.43` | In Stock (`ready`) |
| 30 | `U1` | 1 | 6 | 6 | `TPD12S016PWR` | Texas Instruments | `TSSOP-24_L7.8-W4.4-P0.65-LS6.4-BL` | `2,890` | `₹154.23` | `₹154.57` | In Stock (`ready`) |
| 31 | `U2, U3` | 2 | 12 | 12 | `AP2553W6-7` | Diodes Incorporated | `SOT-26_L3.0-W1.6-P0.95-LS2.8-BL` | `60,585` | `₹27.13` | `₹102.32` | In Stock (`ready`) |
| 32 | `U4, U5` | 2 | 12 | 12 | `TPS259470ARPWR` | Texas Instruments | `VQFN-10_L2.0-W2.0-P0.45-TL` | `3,225` | `₹149.58` | `₹361.42` | In Stock (`ready`) |
| 33 | `U6` | 1 | 6 | 6 | `TPD6S300ARUKR` | Texas Instruments | `WQFN-20_L3.0-W3.0-P0.40-TL-EP1.7` | `7,155` | `₹175.62` | `₹175.28` | In Stock (`ready`) |
