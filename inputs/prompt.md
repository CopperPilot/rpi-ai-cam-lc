Build a compact AI camera around a Raspberry Pi Compute Module 5: a carrier board exactly the size of the CM5,
the CM5 plugged in underneath, the Raspberry Pi AI Camera screwed on top, and a simple two-part case. The
reference photos are an earlier CopperPilot CM5 camera carrier (same size and idea, different parts and fab) and
the official drawings of the camera and its cable.

**The whole board is fabricated and assembled by Lion Circuits (India), not JLCPCB.** Every soldered part must be
in Lion's live catalogue and in stock (`rea-hw lion-parts check <MPN>`); the BOM is by manufacturer part number.
All parts are surface mount. Through-hole parts only if truly needed, with the reason written down (none are
expected: the USB-A, HDMI and USB-C parts below are surface mount).

## Interfaces (all decided with the owner)
- **USB-C ×1, power and flashing:** GCT USB4105-GF-A (16-pin USB 2.0 receptacle, data pins wired). VBUS is the
  board's 5 V input; CC1/CC2 go to the CM5's own CC1/CC2 pins (the CM5 negotiates 5 V / 5 A from a USB PD supply
  by itself, and runs at 3 A from a laptop or a plain supply). D+/D- go to the CM5's USB 2.0 port (not the two
  USB 3.0 ports), so a laptop can flash the eMMC with rpiboot over this one cable and later use it as a USB network
  link. ESD protection on all of it. Keep the 5 V path short and wide: at 3 A from a laptop the CM5 needs at least
  4.75 V, so the cable, connector and copper may drop no more than about 0.25 V. No switch or fuse in series.
- **USB-A ×2, data:** Würth 629104190121 (USB 2.0 Type-A, horizontal, surface mount). Data from the USB 2.0 pairs
  of the CM5's USB3-0 and USB3-1 ports (USB 2.0 speed by choice: every USB 3.0 Type-A at Lion is through-hole).
  VBUS through current-limited USB power switches (TPS2553 or AP2553 class) enabled by the CM5's VBUS_EN, ESD on
  the data lines.
- **HDMI ×1, full size:** Amphenol 10029449-111RLF, from the CM5's HDMI0, through a TPD12S016PWR (HPD/DDC/CEC level
  shifting, ESD and the 5 V supply to the port).
- **Camera:** Raspberry Pi AI Camera (SC1174, a bought module, Lion stocks it), on its own 15-pin, 1.0 mm, 2-lane
  standard (what the camera itself uses). Board socket J5: Amphenol SFW15R-1STE1LF (15-pin 1.0 mm right-angle,
  bottom contact, Lion stock), wired to the CM5's camera port 0 exactly as the CM5 IO board's CAM/DISP 0: 1 GND,
  2/3 MIPI0_D0_N/P, 4 GND, 5/6 MIPI0_D1_N/P, 7 GND, 8/9 MIPI0_C_N/P, 10 GND, 11 CAM_GPIO0 (camera power enable),
  12 CAM_GPIO1, 13 SCL0, 14 SDA0, 15 +3V3 (`dtoverlay=imx500,cam0`).
- **Power button:** one momentary surface-mount push button on the CM5's PWR_BUT (short press on/off, hold 5 s to
  force off; plugging in power starts it). No slide switch.
- **BOOT button:** a small surface-mount button on nRPIBOOT behind a pinhole in the case (hold it with a paperclip
  while plugging in USB-C to enter flash mode; it must be low within 2 ms of 5 V rising).
- **Serial console:** test pads for GPIO14/GPIO15 (UART) and GND for boot logs. No GPIO header, no other GPIO.
- **No SD card slot.**

## Compute module
- CM5104016 (4 GB RAM, 16 GB eMMC, Wi-Fi/Bluetooth), a bought module from Lion. Use the real module model and pin
  table from `rea-hw ref cm5`. Mezzanine connectors: two Amphenol 10164227-1001A1RLF (the part Raspberry Pi
  names; 1.5 mm stacking height, which the CM5 datasheet says leaves **no clearance under the CM5**). Each
  connector is its own footprint with its own MPN and placement (Lion places them as two parts: a single
  module footprint covering both would give the pick-and-place file one position for two connectors).
- **Everything except the CM5 side is on the top layer.** The bottom carries only the two CM5 connectors and the
  four CM5 spacers below; nothing on the bottom may stand taller than the 1.5 mm stack, and nothing may poke
  through from the top (no through-hole leads, no screw tips, no nuts).
- **Wi-Fi antenna:** the CM5 datasheet forbids ground planes or metal directly under its PCB antenna and asks for
  a copper-free cut-out of at least 6.5 x 11 mm, ideally 8 x 15 mm. Our board sits right over it: keep an
  8 x 15 mm area over the antenna free of copper on every layer and of parts, at the board edge, facing the case
  edge (plastic), with no metal near it.

## Board
- Exactly the CM5 outline: 55 x 40 mm, rounded corners matching the module (the reference board used 3.0 mm),
  with the CM5's four M2.5 holes (3.5 mm in from the edges).
- 6 layers, 1.6 mm (owner, 3 Nov: 4 layers left 12 slow nets unroutable), Lion Circuits Custom tier with impedance control: 100 ohm differential for HDMI TMDS and the
  camera CSI lanes, 90 ohm for USB, length-matched within each pair per the CM5 datasheet. Lion's limits (from
  the fab profile): 6 mil tracks and gaps, vias at least 0.35 mm drill with 0.152 mm rings.
- Lion only machine-assembles boards of at least 50 x 100 mm, so the fab package includes a 2-up assembly panel
  with rails, tooling holes and fiducials (`rea-hw fab` makes it).
- Fit: the USB-A pair, HDMI, USB-C, the two buttons, the camera socket and the camera all on the top side of a
  55 x 40 mm board with corner screw heads. A workable arrangement: the two USB-A on one long edge, HDMI and USB-C
  on one short edge, the camera socket next to the camera; check it against the real 3D models.

## Camera mounting (owner, 3 Nov, checked against the AI Camera product brief p.4; be exact)
- The camera is modelled from its product brief by `rea_hardware.parts.ai_camera(center, z_underside, rot_deg)`:
  25 x 23.862 mm board, 1.12 mm thick; four Ø2.2 mm holes (Ø4.75 mm pads) 21 x 12.5 mm apart, 2.0 mm in from the
  sides and 2.0 / 14.5 mm in from the edge opposite the cable socket; lens Ø5.75 mm centred across, on the second
  hole row; the 15-pin 1.0 mm socket 19.61 mm wide, 5.71 mm deep and 2.75 mm below the board, centred on the cable
  edge; 11.9 mm overall; field of view 66.3 x 52.3 deg ±3. Use it (solid, connector, lens, holes, zones); do not
  draw your own.
- **Turned 90 deg** (`rot_deg=90`): the cable leaves through the camera's right edge (+x). Images are portrait,
  rotated in software (owner accepts). The camera stays clear of the antenna zone.
- **Fold-under:** four Würth 9774080243R M2 x 8 mm SMT spacers (Lion stock), flat M2 washers (one or two each, so the
  U-turn below fits), the camera, M2 x 4 mm nylon screws (Essentra 50M020040N003, Lion stock). The ribbon leaves the
  camera heading +x, makes one 180 deg U-turn of at least 3 mm radius to the right of the camera, and runs back under
  the camera into J5, which sits under the camera facing +x with its pin 1 on the same edge of the ribbon as the
  camera's pin 1 (lens down, connector right: pin 1 is the pin nearest you).
- **Height zones (`board.height_zones`, 0.5 mm margin):** under the camera's socket strip and under the rest of the
  camera, from the real heights (camera underside - 2.75 mm, and - 1.85 mm for the parts Camera Module 3 has under
  the same board), board top 1.6 mm. J5 and the ribbon are checked by the cable gates.
- Assembly: cable into the camera first, J5's latch closed with the camera lifted, then fold and screw down. First
  unit: the camera sits on all four spacers without rocking, and a meter shows J5 pin 1 to camera pin 1 and pin 15
  to pin 15 before power.

## Camera cable (owner, 3 Nov)
- Würth 686615050001: 15-way, 1.0 mm, 50 mm, contacts on the same side (the U-turn turns the ribbon over, which is
  why J5 is bottom-contact), 16 mm wide, 10 mm stiffeners. `cables` entry kind ffc, `pins: 15`, `pitch_mm: 1.0`,
  `length_mm: 50`, `width_mm: 16`, `min_bend_radius_mm: 3.0`, `stiff_end_mm` about 6, `contacts: same`.
- Modelled as it really lies: straight out of each socket for its stiffener, the U-turn as an arc of at least 3 mm,
  never a crease, never sideways in its own plane, and clear of every part across its whole width.

## Case
- Basic FDM case around the device: a **front** half and a **back** half that **clip into each other** (snap fits
  sized for FDM). Front: the camera's lens window (aim the camera straight out of the front face), the power button
  reachable, the BOOT pinhole, room for the cable's U-turn; the lens window clears the full field of view
  (`integration.camera_view`). Back: M2.5 heat-set inserts for the four CM5 screws, and vents over
  the CM5 (it sits against the back half and needs airflow).
- Openings at the exact connector mouths: USB-C, both USB-A, HDMI.
- CM5 mounting: four plain (unthreaded) 1.5 mm Würth WA-SMST surface-mount spacers on our bottom side at the CM5
  holes (9774015960R, Lion stock) fill the 1.5 mm gap; M2.5 screws (about 8 mm) go from our top through the board,
  spacer and CM5 into the back half's inserts. The screw heads on our top need a small clear area at each corner.
- Bought outside Lion (agreed): the flat M2 washers, the M2.5 screws, the heat-set inserts and the printed case.

## Software (not built here, record it as pending)
Flash Raspberry Pi OS with rpiboot / Raspberry Pi Imager over the USB-C port (hold BOOT while plugging in);
`dtparam=ant1` for the CM5's PCB antenna; the AI Camera works with the standard IMX500 overlay.

Open items to carry into the release notes: AI Camera heights checked only against its product brief (its side
view reuses Camera Module 3's figures), not a real unit; Lion to confirm
final assembly (fitting the CM5 and camera, the case); impedance stack-up to be confirmed with Lion's quote.
