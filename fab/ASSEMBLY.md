# Compact CM5 AI Camera: manufacturing and assembly

Generated from `rea/spec.yaml` and the board package; the collision, retention and cable gates check the same steps. Directions are in the product frame (+Z is up through the board's top side).

## 1. Boards (fab house: PCB + assembly)

- Fab profile `lioncircuits`: 6 layers, 1.6 mm, assembled on top and bottom.
- Soldered parts: 75 placements on top, 6 on the bottom (`fab/rpi-ai-cam-lc-cpl.csv`).
- Files:
  - `fab/rpi-ai-cam-lc-gerbers.zip`
  - `fab/rpi-ai-cam-lc-cpl.csv`
  - `fab/rpi-ai-cam-lc-bom.csv`
  - `fab/rpi-ai-cam-lc-bom-lioncircuits.csv`
  - `fab/rpi-ai-cam-lc-pos-top.csv`
  - `fab/rpi-ai-cam-lc-pos-bottom.csv`
  - `fab/rpi-ai-cam-lc-pos.zip`
  - `fab/rpi-ai-cam-lc.step`
  - `fab/rpi-ai-cam-lc-schematic.pdf`
- Assembly panel (`fab/panel/`): 2 boards, 113 x 56 mm with rails, fiducials and tooling holes, for machine assembly of a board below the fab's minimum size.

## 2. Bought parts fitted after soldering

| Part | MPN | What it is | Where it goes |
|---|---|---|---|
| cm5 | - | Compute Module 5 with eMMC (any eMMC variant such as CM5104016 or CM5104032; bought outside Lion Circuits, excluded from the Lion PCBA BOM, and pressed into J6/J7 at final assembly) | pcba |
| ai_camera | SC1174 | 12 MP IMX500 Intelligent Vision Camera Module | pcba |
| m2_washers | - | Eight flat M2 x 0.5 mm nylon washers (two per spacer, 1.0 mm stack height, OD 4.0 mm, ID 2.2 mm) placed atop SP1..SP4 | - |
| camera_m2_screws | 50M020040N003 | Four Essentra M2 x 4 mm pan-head nylon screws fastening ai_camera through m2_washers into SP1..SP4 | - |
| m25_inserts | - | Four M2.5 x 3.5 mm brass heat-set threaded inserts (OD 3.5 mm) pressed into back_shell corner bosses | - |
| m25_screws | - | Four M2.5 x 8 mm pan-head machine screws passing from carrier top through SP5..SP8 and the module into m25_inserts | - |

## 3. Final assembly, in order

1. **front_shell (fdm)**. The base the rest is built on.
   Front enclosure shell inverted on assembly fixture (first-article sub-assembly: plug 50 mm 686615050001 FFC into camera J_CAM first, close J5's latch with camera lifted, fold 180 deg U-turn and screw camera down onto all four spacers without rocking; before first power, check with a meter that J5 pin 15 (+3V3) reaches camera pin 15 and J5 pin 1 reaches camera pin 1)
2. **power_button (fdm)**: insert along +Z (25 mm travel). Held captive by a part fitted later.
   Captive power button cap seated into front_shell bore at (38.5, -27.6)
3. **boot_pin (fdm)**: insert along +Z (25 mm travel). Held captive by a part fitted later.
   Captive boot pinhole plunger seated into front_shell pinhole
4. **camera_m2_screws (Four Essentra M2 x 4 mm pan-head nylon screws fastening ai_camera through m2_washers into SP1..SP4)**: insert along +Z (30 mm travel). Held captive by a part fitted later.
   Four M2x4 nylon screws positioned for AI Camera mounting (1.88 mm thread engagement in SP1..SP4)
5. **ai_camera (12 MP IMX500 Intelligent Vision Camera Module)**: insert along +Z (35 mm travel). Held captive by a part fitted later.
   AI Camera (rot_deg=90) seated over M2 screws with lens barrel aligned in front window
6. **m2_washers (Eight flat M2 x 0.5 mm nylon washers (two per spacer, 1.0 mm stack height, OD 4.0 mm, ID 2.2 mm) placed atop SP1..SP4)**: insert along +Z (35 mm travel). Held captive by a part fitted later.
   Eight 0.5 mm flat M2 washers (two per spacer, 1.0 mm stack) placed on M2 screw shanks against AI Camera
7. **m25_screws (Four M2.5 x 8 mm pan-head machine screws passing from carrier top through SP5..SP8 and the module into m25_inserts)**: insert along +Z (40 mm travel). Held captive by a part fitted later.
   Four M2.5x8 machine screws positioned in corner counterbores
8. **the assembled board (PCBA)**: insert along +Z (40 mm travel). Held captive by a part fitted later.
   Carrier PCBA seated onto 8.0 mm camera spacers SP1..SP4, buttons, and corner screw shanks
9. **cm5 (Compute Module 5 with eMMC (any eMMC variant such as CM5104016 or CM5104032; bought outside Lion Circuits, excluded from the Lion PCBA BOM, and pressed into J6/J7 at final assembly))**: insert along +Z (45 mm travel). Held captive by a part fitted later.
   Compute Module 5 (any eMMC variant such as CM5104016 or CM5104032, bought outside Lion Circuits and excluded from Lion BOM) pressed onto J6/J7 and SP5..SP8 at final assembly
10. **m25_inserts (Four M2.5 x 3.5 mm brass heat-set threaded inserts (OD 3.5 mm) pressed into back_shell corner bosses)**: insert along +Z (45 mm travel). Held captive by a part fitted later.
   Four M2.5 heat-set inserts engaged on M2.5 screw shanks
11. **back_shell (fdm)**: insert along +Z (50 mm travel). Snaps in with front_shell.
   Rear shell snaps onto front_shell, capturing CM5 and heat-set inserts

## 4. Enclosure parts

| Part | Qty | Process | Material | File |
|---|---|---|---|---|
| back_shell | 1 | fdm | PLA | `fab/mech/back_shell.stl` |
| front_shell | 1 | fdm | PLA | `fab/mech/front_shell.stl` |
| power_button | 1 | fdm | PLA | `fab/mech/power_button.stl` |
| boot_pin | 1 | fdm | PLA | `fab/mech/boot_pin.stl` |
