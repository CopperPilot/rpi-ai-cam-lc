# Compact CM5 AI Camera — Enclosure & Mechanical Design

## Overview
Two-part snap-fit FDM enclosure (`59.0 x 44.0 x 27.5 mm`, `5.0 mm` outer plan-view corner radius, `2.0 mm` top/bottom walls, `1.75 mm` side walls) housing the 6-layer `1.6 mm` (`55.0 x 40.0 mm`, Lion Circuits `SU-06L-0165-GDM140-001` `GDM-140` stack-up, `1.65 mm` finished thickness, `1 oz` outer / `0.5 oz` inner copper) controlled-impedance carrier PCB, generated parametrically from `rea/spec.yaml` by `case/generate_case.py` using `rea_hardware.cad` and `rea_hardware.parts.ai_camera`.

## Enclosure Parts (`case/out/*.stl`)
- **`front_shell.stl`** (`Z = -0.42 .. +20.00 mm`, grown by `5.5 mm` to enclose the raised AI Camera lens front at `Z = +19.75 mm`):
  - **F1 Camera Lens Window**: `Ø8.0 mm` opening at `(23.0, -15.7)` aligned with the `Ø5.75 mm` AI Camera lens front (`Z = +19.75 mm`), clearing the full `66.3 x 52.3 deg +/- 3 deg` field of view (horizontal along `y` with `rot_deg=90`).
  - **F2 Power Button Bore**: `Ø4.5 mm` upper bore with `Ø6.8 mm` retaining counterbore and `Ø9.2 mm` internal guide boss at `(38.5, -27.6)` over `SW1`, moved outside the `y = -23.7 .. -7.7 mm` (`16.0 mm` wide) FFC U-turn band.
  - **F3 BOOT Pinhole**: `Ø2.0 mm` paperclip pinhole with `Ø4.6 mm` retaining counterbore and `Ø6.6 mm` internal guide boss at `(4.5, -10.5)` over `SW2`.
  - **F4..F7 Side Port Openings**: Centered on the 3D connector mouths of `J1` (USB-C), `J4` (HDMI), `J2` (USB-A 0), and `J3` (USB-A 1), with an internal vertical relief channel under HDMI for collision-free vertical assembly.
  - **50 mm Fold-Under FFC U-Turn Clearance**: Smooth internal cavity clearance up to `X = 44.0 mm` with a rounded `r = 0.65 mm` sight-stop boss (`X = 44.8 .. 46.2 mm`) behind the `J1`/`J4` gap, housing the `180 deg` U-turn (`min_bend_radius >= 3.37 mm >= 3.0 mm`) of the `50.0 mm` `15-way` `1.0 mm` same-side FFC (`Würth 686615050001`) with nothing sharp near the ribbon.
  - **Corner Hold-Down Bosses & Snap Hook**: Four corner counterbored bosses seating onto the carrier PCB around the M2.5 screw heads, plus a top-wall snap-fit hook (`0.20 mm` barb engagement).
- **`back_shell.stl`** (`Z = -7.50 .. -0.02 mm`):
  - **Corner Insert Bosses**: Four `Ø5.6 mm` bosses (`Z = -5.50 .. -2.63 mm`) with `Ø3.6 mm` bores and `0.05 mm` axial press-fit interference seating the four M2.5 heat-set inserts (`m25_inserts`).
  - **F8 Cooling Vents**: Seven `2.6 x 20.0 mm` rounded ventilation slots centered over the Compute Module 5 (`36.0 x 20.0 mm` array).
  - **Snap-Fit Catch**: Internal catch pocket and ridge on the top wall mating with `front_shell`.
- **`power_button.stl`**: Captive flanged push-button actuator (`Ø4.0 mm` cap, `Ø6.2 mm` flange, `Ø2.8 mm` stem at `Z = 3.25 .. 19.85 mm`) actuating `SW1` at `(38.5, -27.6)` (`0.25 mm` travel).
- **`boot_pin.stl`**: Captive recessed pinhole plunger (`Ø1.6 mm` pin, `Ø4.0 mm` flange, `Ø2.4 mm` stem at `Z = 3.30 .. 19.30 mm`) actuating `SW2` at `(4.5, -10.5)` (`0.20 mm` travel).

## Purchased 3D Models (`case/purchased/*.stl`)
- **`cm5.stl`**: Watertight world-posed Compute Module 5 model (`55.0 x 40.0 x 4.62 mm` at `Z = -5.02 .. -0.40 mm`). Any Compute Module 5 variant with onboard eMMC fits (for example `CM5104016` or `CM5104032`); it is bought outside Lion Circuits (excluded from the Lion Circuits soldered BOM) and pressed into the two bottom-side board-to-board mezzanine connectors (`J6`, `J7`) at final assembly.
- **`ai_camera.stl`**: Fixed 12 MP AI Camera module exported from `rea_hardware.parts.ai_camera((20.431, -15.7), z_underside=10.6, rot_deg=90)` (`23.862 x 25.0 x 11.9 mm` at `Z = 7.85 .. 19.75 mm`, PCB underside at `Z = 10.60 mm`, `2.75 mm` 15-pin socket strip down to `Z = 7.85 mm`, `1.85 mm` underside component slab down to `Z = 8.75 mm`, enforcing `<= 5.75 mm` component height under `.socket_rect` and `<= 6.65 mm` under `.outline_rect` with `0.5 mm` margin).
- **`m2_washers.stl`**: Eight `M2 x 0.5 mm` flat nylon washers (`two per spacer`, `1.0 mm` stack at `Z = 9.60 .. 10.60 mm`) atop the four `Würth 9774080243R` `M2 x 8.0 mm` SMT spacers (`SP1..SP4` at `(10.5, 5.2)`, `(23.0, 5.2)`, `(10.5, 26.2)`, `(23.0, 26.2)`).
- **`camera_m2_screws.stl`**: Four `Essentra 50M020040N003` `M2 x 4 mm` pan-head nylon screws (`Z = 7.72 .. 12.92 mm`, providing `1.88 mm >= 1.8 mm` thread engagement inside `SP1..SP4`).
- **`m25_inserts.stl`**: Four `M2.5 x 3.5 mm` brass heat-set inserts (`Z = -6.50 .. -3.00 mm`).
- **`m25_screws.stl`**: Four `M2.5 x 8 mm` pan-head machine screws (`Z = -6.40 .. 3.40 mm`).

## Assembly Sequence & Pre-Power Verification
1. **Fold-Under Camera & FFC Assembly**: Plug the `50 mm` `Würth 686615050001` 15-way same-side FFC cable into the AI Camera (`J_CAM`) first, close `J5`'s (`Amphenol SFW15R-1STE1LF` bottom-contact 15-pin FFC socket under the camera) latch with the camera lifted, then fold the `180 deg` U-turn (`>= 3.0 mm` radius) and screw the camera down onto the four `M2 x 8.0 mm` spacers (`SP1..SP4`) + two `0.5 mm` washers per spacer using the four `M2 x 4 mm` nylon screws.
2. **Pre-Power Multimeter & Seating Check**: Before applying power for the first time, check with a meter that `J5` pin 15 (`+3V3`) reaches camera pin 15 and `J5` pin 1 (`GND`) reaches camera pin 1, and verify that the camera sits flat on all four spacers without rocking.
3. **Compute Module 5 Installation (Off-BOM Final Assembly)**: Press the Compute Module 5 (any CM5 variant with eMMC fits, e.g., `CM5104016` or `CM5104032`; bought outside Lion Circuits and kept out of the Lion BOM) onto the two bottom-side `100-pin` board-to-board mezzanine receptacles (`J6`, `J7`) until seated flat against the four `1.5 mm` spacers (`SP5..SP8`).
4. **Final Closure & Software**: Seat the assembly into `front_shell`, pass the four `M2.5 x 8 mm` corner screws through the carrier board, `SP5..SP8`, and CM5 into the `back_shell` heat-set inserts (`m25_inserts`), and snap `back_shell` closed; configure Raspberry Pi OS with `dtparam=ant1` and `dtoverlay=imx500,cam0` (portrait image rotated in software).
