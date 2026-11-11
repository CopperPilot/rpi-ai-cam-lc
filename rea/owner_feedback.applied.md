Owner changes for rpi-ai-cam-lc (resumed for the Lion Circuits order, 9 Nov). A trial upload to Lion Circuits'
portal found the blockers below. Fix them so the board can be ordered as is: 10 PCBs and 6 assembled boards, with
Lion buying every soldered part.

1. **Out-of-stock parts.** Lion's BOM page shows these lines as out of stock. Swap them for the replacements Lion
   lists as Ready. Each has the same package and footprint, and the same or a higher rating:
   - C8, C10, C11, C12, C34: `GRM155R61E105KA12D` becomes **`GRM155R61E105KE11J`** (Murata 1 uF 25 V X5R 0402).
   - C2, C3, C19: `GRM188R61A226ME15D` becomes **`CL10A226MP8NUNE`** (Samsung 22 uF 10 V X5R 0603).
   - R6, R7: 22 k 0402 becomes **`RC0402FR-0722KL`**, the same MPN as R10 and R11, so they share one BOM line.
   Update the schematic values and MPN fields, the spec's purchased and BOM notes, and anything that quotes the old
   MPNs.
2. **Use Lion's real 6-layer stack-up.** The board stays at **6 layers, 1.6 mm, and keeps HDMI**. The stack-up in
   the board file is not what Lion builds. Lion's standard 6-layer stack-up (document `SU-06L-0165-GDM140-001`,
   GDM-140 laminate, Tg 140, 1.65 mm finished thickness) is, from the top:

   | Layer | Material | Thickness | Dk |
   |---|---|---|---|
   | Solder mask | | 0.020 mm | 3.8 |
   | L1 (F.Cu) | 1 oz copper | 0.035 mm | |
   | Prepreg | 7628 | 0.190 mm | 4.69 |
   | L2 | 0.5 oz copper | 0.0175 mm | |
   | Core | | 0.450 mm | 4.5 |
   | L3 | 0.5 oz copper | 0.0175 mm | |
   | Prepreg | 7628 | 0.190 mm | 4.69 |
   | L4 | 0.5 oz copper | 0.0175 mm | |
   | Core | | 0.450 mm | 4.5 |
   | L5 | 0.5 oz copper | 0.0175 mm | |
   | Prepreg | 7628 | 0.190 mm | 4.69 |
   | L6 (B.Cu) | 1 oz copper | 0.035 mm | |
   | Solder mask | | 0.020 mm | 3.8 |

   - Put exactly this stack-up in the board file and the spec. Inner copper is **0.5 oz**: order it that way and
     design for it.
   - Keep a solid GND plane next to every outer layer that carries high-speed pairs (L2 under F.Cu, L5 over B.Cu).
   - Recompute the widths and gaps for 100 ohm (HDMI TMDS, CSI) and 90 ohm (USB) differential pairs on this
     stack-up: edge-coupled microstrip on F.Cu and B.Cu over 0.190 mm with Dk 4.69, plus stripline on any inner
     layer that carries pairs. Then update the net classes.
   - Re-fit every high-speed route to the new widths and gaps. Keep length matching within each pair and across
     the HDMI lanes, and keep the pairs off plane splits and edges. Keep the placement.
   - Check every power path for 0.5 oz inner copper: the 5 V input, the CM5 supply and the USB VBUS outputs, at
     their full current. Widen traces or move current onto the planes or outer layers where the temperature rise
     exceeds 10 C.
   - Write the stack-up, each pair's target impedance, its layer and its width and gap into the fab notes, so Lion
     can quote impedance control.
3. **Silkscreen clean for assembly.**
   - Clear every silkscreen DRC warning: silk over copper, silk overlap, silk too close to the board edge, and text
     thinner than Lion's minimum (lines at least 0.15 mm, text at least 0.8 mm tall). Move or shrink reference
     designators rather than deleting them; hide them only where there is truly no room, and only on the passives.
   - Resolve the footprint-mismatch warnings against the library, or record why each one is intentional.
4. **Pin 1 and polarity marks.** These are read at assembly and inspection:
   - every IC, diode (including D12), polarized capacitor (C26 to C31) and connector needs a clear pin-1 or polarity
     mark on both the silkscreen and the fab layer;
   - each mark must stay visible next to the part once it is placed, not under its body.
5. **Compute Module 5.**
   - Any CM5 variant with eMMC fits (for example the CM5104016 or CM5104032). It is bought outside Lion and pressed
     into the two board-to-board connectors at final assembly.
   - Keep it out of the Lion BOM, and say so in the BOM notes and in the assembly guide.

Keep everything else: the enclosure, the size, the parts that already pass, and the placements and routes these
changes do not touch.
