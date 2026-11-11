# Scope Observation & Mechanical/Electrical Contract Analysis

## 1. Product Overview & Reference Measurements
- **Product:** Compact AI Camera carrier board and two-part snap-fit FDM enclosure built around the Compute Module 5 (`CM5104016`) and the 12 MP Intelligent Vision Camera (`SC1174`).
- **Fabrication & Assembly:** Lion Circuits (`fab/lioncircuits.yaml`), 6-layer 1.6 mm FR-4 PCB with controlled impedance on Lion's published 6-layer 1.6 mm Custom-tier stack-up (`F.Cu` signal / `0.12 mm` `2116*1` prepreg / `In1.Cu` unbroken GND / `0.36 mm` `NP-140` core / `In2.Cu` slow signals / `0.48 mm` `2116*4` prepreg / `In3.Cu` `+5V` & `+3V3` power / `0.36 mm` `NP-140` core / `In4.Cu` unbroken GND / `0.12 mm` `2116*1` prepreg / `B.Cu` signal; 100 ohm differential for HDMI TMDS and 2-lane MIPI0 CSI-2 with `0.1524 mm` width / `0.18 mm` gap, 90 ohm differential for USB 2.0 with `0.175 mm` width / `0.1524 mm` gap; minimum 6 mil trace/space, 0.35 mm via drill / 0.66 mm via pad, 0.30 mm copper-to-edge), panelized 2-up (`>= 50 x 100 mm`) for machine assembly with MPN-keyed BOM and top/bottom CPL.
- **Reference Photos, Drawings & Fixed Camera Helper:**
  - `inputs/ref-cm5-ai-cam-3d_top.jpg`, `inputs/ref-cm5-ai-cam-3d_bottom.jpg`, `inputs/ref-cm5-ai-cam-3d_iso.jpg`: CM5 camera carrier reference (`55.0 x 40.0 mm` PCB with `3.0 mm` corner radius and four M2.5 mounting holes at `(3.5, 3.5)`, `(51.5, 3.5)`, `(3.5, 36.5)`, `(51.5, 36.5)`).
  - `inputs/ai-camera-drawing.jpg`, `inputs/camera-module-3-drawing.jpg`, & `rea_hardware.parts.ai_camera(center=(20.431, -15.7), z_underside=10.6, rot_deg=90)`: Fixed camera model from AI Camera Product Brief p.4 (`25.0 x 23.862 mm` board, `1.12 mm` thick; Ø2.2 mm holes `21.0 x 12.5 mm` apart; lens Ø5.75 mm on the second hole row; 15-pin 1.0 mm socket `19.61 mm` wide, `5.71 mm` deep, `2.75 mm` below the board, centred on the cable edge; `11.9 mm` overall depth; field of view `66.3 x 52.3 deg +/- 3 deg`). Rotated `rot_deg=90` CCW so the cable exits through the right edge (`+x` at `x = 32.362 mm`), with board outline spanning `x_board` in `[8.5, 32.362]`, `y_board` in `[3.2, 28.2]` (clear of the `x = 0..8 mm` antenna keepout).
  - **Camera Cable:** Würth `686615050001` (`15-way`, `1.0 mm` pitch, `50.0 mm +/- 3 mm` length, contacts on the **same** side, `16.0 mm` width, `10.0 mm` stiffeners with `5.0 mm` contact strips, `0.3 mm` thick at the contacts; Lion stock).

## 2. World Frame, Stack-up & Envelope Derivation
- **Carrier Board (`pcba`):**
  - Outline: `55.0 x 40.0 x 1.6 mm`, `3.0 mm` corner radius.
  - World frame: `X` in `[0.0, 55.0]`, `Y` in `[-40.0, 0.0]` (`y_board = -Y`), `Z` in `[0.0, 1.6]` (`B.Cu` at `Z = 0.0`, `F.Cu` at `Z = 1.6`).
- **Underside CM5 Stack (`Z < 0`):**
  - Two 100-pin mezzanine receptacles (`J6`, `J7`: Amphenol `10164227-1001A1RLF`, 1.5 mm stacking height) at `(25.0, 37.0)` and `(25.0, 3.0)` on `B.Cu` (`rot_deg: 180`), plus four unthreaded 1.5 mm SMT spacers (`SP5..SP8`: Würth `9774015960R`) at the four M2.5 corner holes `(3.5, 3.5)`, `(51.5, 3.5)`, `(3.5, 36.5)`, `(51.5, 36.5)`.
  - `CM5104016` module (`cm5`, `CM5_module.stl`, `[55.0, 40.0, 4.62]` mm) seats at `Z` in `[-5.02, -0.40]`.
  - CM5 PCB antenna keepout: `8.0 x 15.0 mm` copper-free and component-free zone on **all six** copper layers (`F.Cu`, `In1.Cu`, `In2.Cu`, `In3.Cu`, `In4.Cu`, `B.Cu`) at the left board edge (`x` in `[0.0, 8.0]`, `y` in `[14.0, 29.0]`), facing the plastic left wall of the case.
- **Top-Side Camera Stack (`Z > 1.6`), Fold-Under Cable & Height Zones:**
  - Four Würth WA-SMSI M2 8.0 mm SMT threaded spacers (`SP1..SP4`: `9774080243R`, Lion stock) sit on `F.Cu` (`Z` in `[1.6, 9.6]`) at `.holes`: `(10.5, 5.2)`, `(23.0, 5.2)`, `(10.5, 26.2)`, and `(23.0, 26.2)`.
  - Two 0.5 mm flat M2 washers per spacer (`1.0 mm` stack, `Z` in `[9.6, 10.6]`) sit atop `SP1..SP4`; the camera PCB underside rests at `Z = 10.6 mm` (`9.0 mm` above `F.Cu`), fastened by four Essentra `50M020040N003` M2 x 4 mm nylon screws (`4.0 mm` shank - `1.12 mm` camera PCB - `1.00 mm` washers = `1.88 mm >= 1.8 mm` thread engagement inside `SP1..SP4`).
  - Camera module (`ai_camera`, `dims_mm: [23.862, 25.0, 11.9]`, `position_mm: [8.5, -28.2, 7.85]`) spans `Z` in `[7.85, 19.75]` (`2.75 mm` underside socket strip down to `Z = 7.85 mm`, `1.85 mm` underside component slab down to `Z = 8.75 mm`, camera ribbon centre `J_CAM` at `[32.362, -15.7, 9.225]` with pin 1 at `[32.362, -8.7, 9.225]`, and lens barrel front at `[23.0, -15.7, 19.75]`).
  - `board.height_zones` (`0.5 mm` margin):
    - `camera_socket_strip`: `.socket_rect` `rect_mm: [26.652, 5.895, 32.362, 25.505]`, `max_height_mm: 5.75` (`(10.6 - 2.75) - 1.6 - 0.5 = 5.75 mm`), `allow_refs: [J5]`.
    - `camera_body`: `.outline_rect` `rect_mm: [8.5, 3.2, 32.362, 28.2]`, `max_height_mm: 6.65` (`(10.6 - 1.85) - 1.6 - 0.5 = 6.65 mm`), `allow_refs: [SP1, SP2, SP3, SP4, J5]`.
- **Outer Enclosure Envelope:**
  - Two-part FDM snap-fit case (`front_shell` and `back_shell`, `2.0 mm` wall thickness):
    - `width_mm: 59.0` (`X` in `[-2.0, 57.0]`)
    - `height_mm: 44.0` (`Y` in `[-42.0, 2.0]`)
    - `depth_mm: 27.5` (`Z` in `[-7.5, 20.0]`, grown by `5.5 mm` on the front half to enclose the lens front at `Z = +19.75 mm`)
    - `corner_radius_mm: 5.0`
    - `front_origin_world_mm: [-2.0, 2.0, 20.0]` (mapping board `(x, y)` to front-view `(x + 2.0, y + 2.0)`).

## 3. Connector, Control & Fold-Under Cable Arrangement
- **Right Short Edge (`x = 55.0`, `view: right`):**
  - `J1` (USB-C power & rpiboot flashing, GCT `USB4105-GF-A`): `x_mm: 51.5, y_mm: 11.5, side: top, rot_deg: 90` (mouth faces `+x`).
  - `J4` (Full-size HDMI 0 output, Amphenol `10029449-111RLF`): `x_mm: 49.0, y_mm: 25.0, side: top, rot_deg: 90` (mouth faces `+x`).
- **Bottom Long Edge (`y = 40.0`, `view: bottom`):**
  - `J2` (USB 2.0 Type-A host port 0, Würth `629104190121`): `x_mm: 16.0, y_mm: 34.3, side: top, rot_deg: 0` (mouth faces `+y`).
  - `J3` (USB 2.0 Type-A host port 1, Würth `629104190121`): `x_mm: 35.5, y_mm: 34.3, side: top, rot_deg: 0` (mouth faces `+y`).
- **Front Controls (`view: front`) & Under-Camera 15-Pin FFC Socket:**
  - `SW1` (Power button on `PWR_BUT`, C&K `PTS526SM15SMTR2LFS`): moved to `x_mm: 38.5, y_mm: 27.6, side: top, rot_deg: 0` (`F2` at front-view `[40.5, 29.6]`), clear of the `y_board = 7.7..23.7 mm` 16 mm FFC ribbon band, actuated by `power_button` along `[0, 0, -1]`.
  - `SW2` (BOOT pinhole button on `nRPIBOOT`, Omron `B3U-1000P`): `x_mm: 4.5, y_mm: 10.5, side: top, rot_deg: 90`, actuated via front pinhole by `boot_pin` along `[0, 0, -1]`.
  - `J5` (15-pin 1.0 mm right-angle bottom-contact FFC socket, Amphenol `SFW15R-1STE1LF`, LCSC `C3168538`, `2.71 mm` tall with slot centre at `Z = 2.925 mm`): placed under the camera at `x_mm: 13.5, y_mm: 15.7, side: top, rot_deg: 90` (mouth at `x = 18.35 mm` facing `+x` towards the U-turn, long axis along `y`, pin 1 at `y_board = 8.7 mm` / `Y_world = -8.7 mm` matching `J_CAM` pin 1). Wired to CM5 camera port 0 (`CAM/DISP 0`: `1=GND, 2=MIPI0_D0_N, 3=MIPI0_D0_P, 4=GND, 5=MIPI0_D1_N, 6=MIPI0_D1_P, 7=GND, 8=MIPI0_C_N, 9=MIPI0_C_P, 10=GND, 11=CAM_GPIO0, 12=CAM_GPIO1, 13=SCL0, 14=SDA0, 15=+3V3`; no external I2C pull-ups on `SCL0`/`SDA0` since CM5 and AI Camera have onboard pull-ups).
  - `camera_fpc` (Würth `686615050001`, `50 mm` same-side 15-way 1.0 mm FFC): leaves `J_CAM` (`Z = 9.225 mm`, contacts up `[0,0,1]`) heading `+x` straight for the stiffener, folds through a single `180 deg` U-turn of radius `>= 3.37 mm` (`6.30 mm >= 6.0 mm` vertical separation between ribbon levels, outer edge `x = 43.73 mm <= 44.0 mm` clearing `D1/D4-D6/C1/C4`, `J1`, and `J4`), and runs `-x` under the camera into `J5` (`Z = 2.925 mm` slot, contacts down `[0,0,-1]`).

## 4. First-Article Assembly, Continuity Check & Pending Release Items
- **Assembly Order:** Plug the 50 mm `686615050001` FFC cable into the AI Camera (`J_CAM`) first, close `J5`'s latch on the carrier board with the camera lifted, then fold the 180 deg U-turn and screw the camera down onto the four 8.0 mm spacers (`SP1..SP4` + two 0.5 mm M2 washers per spacer) with the four M2 x 4 mm nylon screws.
- **Pre-Power Multimeter & Mechanical Checks:**
  - Before applying power for the first time, check with a multimeter that `J5` pin 15 (`+3V3`) has continuity to camera pin 15 and `J5` pin 1 (`GND`) has continuity to camera pin 1.
  - Verify that the camera sits flat on all four spacers without rocking and that the M2 x 4 mm screws engage cleanly (`1.88 mm >= 1.8 mm` thread engagement).
- **Pending Software & Release Notes:**
  - Flash OS via `rpiboot` over `J1` (USB-C) while holding `SW2` (`nRPIBOOT` low within 2 ms of 5 V rise); enable `dtparam=ant1` for the CM5 PCB antenna and `dtoverlay=imx500,cam0` for the AI Camera on CM5 camera port 0 (portrait image rotated in software).
  - Open items for release notes: physical verification of AI Camera underside heights against a production sample; confirmation of final mechanical assembly (fitting CM5, camera on 8 mm spacers + washers, 50 mm fold-under FFC, and FDM case) with Lion Circuits; confirmation of 6-layer controlled-impedance stack-up with Lion Circuits' fabrication quote.
