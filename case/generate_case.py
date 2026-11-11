#!/usr/bin/env python3
"""Parametric enclosure and purchased-part model generator for Compact CM5 AI Camera.

Supports the 6-layer 1.6 mm (Lion Circuits SU-06L-0165-GDM140-001, 1.65 mm finished thickness) carrier PCB
and any Compute Module 5 variant with onboard eMMC (e.g., CM5104016 or CM5104032, bought outside Lion Circuits
and pressed onto the bottom-side J6/J7 mezzanine receptacles at final assembly).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import trimesh

from rea_hardware import cad, parts


def build_purchased_models(bf: dict, out_dir: Path) -> None:
    """Build watertight 3D models for all purchased parts seated at position_mm within dims_mm."""
    out_dir.mkdir(parents=True, exist_ok=True)
    purchased = bf["purchased"]

    # 1. ai_camera: Fixed 12 MP Intelligent Vision Camera Module from rea_hardware.parts.ai_camera
    # center=(20.431, -15.7), z_underside=10.6, rot_deg=90 -> position_mm: [8.5, -28.2, 7.85], dims_mm: [23.862, 25.0, 11.9]
    cam = parts.ai_camera((20.431, -15.7), z_underside=10.6, rot_deg=90)
    cad.export(cam.solid, out_dir / "ai_camera.stl")
    cam_holes = [(float(hx), float(hy)) for hx, hy in cam.holes]

    # 2. m2_washers: Eight flat M2 x 0.5 mm nylon washers (two per spacer, 1.0 mm stack) atop SP1..SP4
    # position_mm: [8.5, -28.2, 9.6], dims_mm: [16.5, 25.0, 1.0]
    w_pos = purchased["m2_washers"]["position_mm"]
    w_dims = purchased["m2_washers"]["dims_mm"]
    z0_w = float(w_pos[2])
    z1_w = z0_w + float(w_dims[2])
    washers = [cad.standoff(cx, cy, z0_w, z1_w, od=4.0, id_=2.2) for cx, cy in cam_holes]
    cad.export(cad.union(*washers), out_dir / "m2_washers.stl")

    # 3. camera_m2_screws: Four Essentra 50M020040N003 M2 x 4 mm pan-head nylon screws
    # position_mm: [8.5, -28.2, 7.72], dims_mm: [16.5, 25.0, 5.2] -> Z in [7.72, 12.92]
    # Lower tip inside SP1..SP4 (Z=7.72..9.62, 1.88 mm thread engagement) has od=1.44 mm (< 1.57 mm inner bore of SP1..SP4)
    # Upper shank through washers & camera PCB (Z=9.60..11.72) has od=1.90 mm (< 2.20 mm hole in washers & camera)
    # Pan head above camera PCB (Z=11.70..12.92) has od=3.90 mm (spans X=8.55..24.95, Y=-28.15..-3.25)
    m2_screws = []
    for hx, hy in cam_holes:
        tip = cad.standoff(hx, hy, 7.72, 9.62, od=1.44, id_=0.0)
        shank = cad.standoff(hx, hy, 9.60, 11.72, od=1.90, id_=0.0)
        head = cad.standoff(hx, hy, 11.70, 12.92, od=3.90, id_=0.0)
        slot_cut = cad.box(2.2, 0.5, 0.5, at=(hx - 1.1, hy - 0.25, 12.57))
        m2_screws.append(cad.union(tip, shank, head) - slot_cut)
    cad.export(cad.union(*m2_screws), out_dir / "camera_m2_screws.stl")

    # 4. m25_inserts: Four M2.5 x 3.5 mm brass heat-set threaded inserts
    # position_mm: [1.75, -38.25, -6.5], dims_mm: [51.5, 36.5, 3.5] -> Z in [-6.5, -3.0]
    cm5_holes = [
        (3.5, -3.5),
        (51.5, -3.5),
        (3.5, -36.5),
        (51.5, -36.5),
    ]
    inserts = [cad.standoff(hx, hy, -6.50, -3.00, od=3.50, id_=2.50) for hx, hy in cm5_holes]
    cad.export(cad.union(*inserts), out_dir / "m25_inserts.stl")

    # 5. m25_screws: Four M2.5 x 8 mm pan-head machine screws
    # position_mm: [1.25, -38.75, -6.4], dims_mm: [52.5, 37.5, 9.8] -> Z in [-6.4, 3.4]
    # Shank (Z=-6.40..1.62) has od=2.20 mm (< 2.50 mm insert ID, < 2.70 mm CM5 hole, < 3.30 mm SP5..SP8 ID, < 4.40 mm PCB hole)
    # Pan head (Z=1.58..3.40) has od=4.60 mm (r=2.30 mm > 2.20 mm PCB hole radius, spans X=1.20..53.80, Y=-38.80..-1.20)
    m25_screws = []
    for hx, hy in cm5_holes:
        shank = cad.standoff(hx, hy, -6.40, 1.62, od=2.20, id_=0.0)
        head = cad.standoff(hx, hy, 1.58, 3.40, od=4.60, id_=0.0)
        slot_cut = cad.box(2.6, 0.6, 0.6, at=(hx - 1.3, hy - 0.3, 2.95))
        m25_screws.append(cad.union(shank, head) - slot_cut)
    m25_u = cad.union(*m25_screws)
    cad.export(m25_u, out_dir / "cm5_m25_screws.stl")
    cad.export(m25_u, out_dir / "m25_screws.stl")

    # 6. Also write a watertight, world-posed CM5 model to case/purchased/cm5.stl
    ref_cm5 = Path("hardware/rea_refs.3dshapes/CM5_module.stl")
    if ref_cm5.exists():
        raw = trimesh.load(ref_cm5, force="mesh")
        comps = trimesh.graph.connected_components(raw.face_adjacency, min_len=12)
        ms = []
        for idx in comps:
            sub = raw.submesh([idx], append=True)
            if sub.area < 4.0:
                continue
            if len(sub.faces) > 600 or not sub.is_watertight:
                lo, hi = sub.bounds
                ext = hi - lo
                if np.all(ext > 0.05):
                    ms.append(cad.box(float(ext[0]), float(ext[1]), float(ext[2]), at=(float(lo[0]), float(lo[1]), float(lo[2]))))
            else:
                try:
                    ms.append(cad.from_trimesh(sub))
                except Exception:
                    lo, hi = sub.bounds
                    ext = hi - lo
                    if np.all(ext > 0.05):
                        ms.append(cad.box(float(ext[0]), float(ext[1]), float(ext[2]), at=(float(lo[0]), float(lo[1]), float(lo[2]))))
        u = cad.union(*ms)
        cut1 = cad.box(22.70, 3.50, 1.155, at=(13.65, 1.25, -1.12))
        cut2 = cad.box(22.70, 3.50, 1.155, at=(13.65, 35.25, -1.12))
        for hx, hy in [(3.5, 3.5), (51.5, 3.5), (3.5, 36.5), (51.5, 36.5)]:
            u = u - cad.standoff(hx, hy, 0.02, 0.085, od=6.2, id_=0.0)
        pin_keep = cad.box(0.30, 0.30, 1.16, at=(36.40, 2.80, -1.11))
        u = (u - cut1 - cut2) + pin_keep
        tm = cad.to_trimesh(u)
        tf = np.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, -1.0, 0.0, 0.0],
            [0.0, 0.0, -1.0, -1.509],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=float)
        tm.apply_transform(tf)
        tm.fix_normals()
        cad.export(tm, out_dir / "cm5.stl")


def build_enclosure(bf: dict, out_dir: Path) -> None:
    """Build watertight FDM enclosure parts (back_shell, front_shell, power_button, boot_pin)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    spec = bf["spec"]
    env = spec["envelope"]

    env_w = float(env["width_mm"])        # 59.0
    env_h = float(env["height_mm"])       # 44.0
    env_d = float(env["depth_mm"])        # 27.5
    corner_r = float(env["corner_radius_mm"])  # 5.0
    ox, oy, oz = [float(v) for v in env["front_origin_world_mm"]]  # [-2.0, 2.0, 20.0]

    x_min, x_max = ox, ox + env_w         # -2.0 .. 57.0
    y_min, y_max = oy - env_h, oy         # -42.0 .. 2.0
    z_min, z_max = oz - env_d, oz         # -7.5 .. 20.0
    z_split = 0.0                         # Parting line at B.Cu plane Z = 0.0

    wall_xy = 1.75                        # 1.75 mm side walls -> 0.25 mm clearance around 55x40 mm board/CM5
    wall_z = 2.00                         # 2.00 mm top and bottom walls
    z_ceil = z_max - wall_z               # 18.00 mm internal front ceiling
    inner_r = max(corner_r - wall_xy, 2.8)

    cav_x0 = x_min + wall_xy              # -0.25
    cav_y0 = y_min + wall_xy              # -40.25
    cav_w = env_w - 2 * wall_xy           # 55.50
    cav_h = env_h - 2 * wall_xy           # 40.50

    cm5_holes = [(h["x_mm"], -h["y_mm"]) for h in bf["holes"]]
    features = {f["id"]: f for f in spec["fidelity"]["must_match"]}

    # -------------------------------------------------------------------------
    # 1. back_shell (Z = -7.50 .. 0.00)
    # -------------------------------------------------------------------------
    back_h = z_split - z_min  # 7.50 mm
    cx_env = (x_min + x_max) / 2.0
    cy_env = (y_min + y_max) / 2.0

    # Subtle bottom outer chamfer (0.5 mm tall at Z = -7.5..-7.0) so intermediate slices keep exact r = 5.0 mm
    back_outer = cad.loft([
        (z_min, env_w - 0.8, env_h - 0.8, corner_r - 0.4, cx_env, cy_env),
        (z_min + 0.5, env_w, env_h, corner_r, cx_env, cy_env),
        (z_split - 0.02, env_w, env_h, corner_r, cx_env, cy_env),
    ])
    back_cavity = cad.rounded_box(
        cav_w, cav_h, back_h - wall_z + 1.0,
        r=inner_r,
        at=(cav_x0, cav_y0, z_min + wall_z),
    )
    back_shell = back_outer - back_cavity

    # Four corner bosses for M2.5 heat-set inserts and CM5 support (Z = -5.50 .. -2.63)
    # m25_inserts span Z = -6.50 .. -3.00 with OD = 3.50 mm.
    # Boss bore has ID = 3.60 mm (0.05 mm radial clearance) down to Z = -6.45 mm (0.05 mm axial press-fit interference at seat).
    for hx, hy in cm5_holes:
        boss = cad.standoff(hx, hy, z_min + wall_z - 0.2, -2.63, od=5.60, id_=0.0)
        back_shell = back_shell + boss
    for hx, hy in cm5_holes:
        bore = cad.standoff(hx, hy, -6.45, -2.50, od=3.60, id_=0.0)
        back_shell = back_shell - bore

    # Snap-fit catch pocket on inside of top wall (Y in [0.25, 2.00], outside PCBA/CM5 Y=[-40, 0])
    # Pocket spans X in [21.0, 34.0], Y in [0.20, 1.25], Z in [-0.55, 0.05]
    # Catch ridge protrudes inward to Y = 0.95 at Z in [-0.18, -0.02] (0.18 mm catch lip)
    snap_pocket = cad.box(13.0, 1.05, 0.60, at=(21.0, 0.20, -0.55))
    snap_ridge = cad.box(12.6, 0.30, 0.16, at=(21.2, 0.95, -0.18))
    back_shell = (back_shell - snap_pocket) + snap_ridge

    # Rear cooling vents (F8: rear view center_mm=[29.5, 22.0], size_mm=[36.0, 20.0] -> world center (27.5, -20.0))
    f8 = features["F8"]
    vent_cx = ox + env_w - float(f8["center_mm"][0])  # 27.5
    vent_cy = oy - float(f8["center_mm"][1])          # -20.0
    vent_w, vent_h = [float(v) for v in f8["size_mm"]]  # 36.0, 20.0
    n_slots = 7
    slot_w = 2.6
    pitch = (vent_w - slot_w) / (n_slots - 1)
    for i in range(n_slots):
        sx = (vent_cx - vent_w / 2.0 + slot_w / 2.0) + i * pitch
        back_shell = back_shell - cad.slot(sx, vent_cy, w=slot_w, h=vent_h, depth=6.0, r=slot_w / 2.0, z0=z_min - 1.0)

    cad.export(back_shell, out_dir / "back_shell.stl")

    # -------------------------------------------------------------------------
    # 2. front_shell (Z = 0.00 .. 20.00, plus snap hook to Z = -0.42)
    # -------------------------------------------------------------------------
    front_h = z_max - z_split  # 20.00 mm
    front_outer = cad.loft([
        (z_split, env_w, env_h, corner_r, cx_env, cy_env),
        (z_max - 0.6, env_w, env_h, corner_r, cx_env, cy_env),
        (z_max, env_w - 1.0, env_h - 1.0, corner_r - 0.5, cx_env, cy_env),
    ])
    front_cavity = cad.rounded_box(
        cav_w, cav_h, front_h - wall_z + 1.0,
        r=inner_r,
        at=(cav_x0, cav_y0, z_split - 1.0),
    )
    front_shell = front_outer - front_cavity

    # Four corner hold-down bosses reaching down to Z = 1.60 mm (PCBA top face)
    # Outer radius 3.60 mm around each corner hole, intersected with front_outer so it stays inside the shell,
    # with an inner counterbore of radius 2.65 mm (OD = 5.30 mm) from Z = 1.00 .. z_ceil mm to clear m25_screws heads (OD = 4.60 mm, Z = 1.58..3.40).
    # Trim away inner board zones below Z = 8.60 mm so J1 (Y=-15.97..-7.03) and J4 (Y=-33.10..-16.90) have >= 0.50 mm clearance.
    corner_pillars = []
    for hx, hy in cm5_holes:
        pillar = cad.standoff(hx, hy, 1.60, z_ceil + 0.2, od=7.20, id_=5.30)
        corner_pillars.append(pillar)
    pillars_u = cad.union(*corner_pillars) ^ front_outer
    clear_x = cad.box(46.0, 42.0, 8.6, at=(4.5, -41.0, 0.0))
    clear_y = cad.box(60.0, 27.2, 8.6, at=(-1.0, -33.6, 0.0))
    pillars_u = (pillars_u - clear_x) - clear_y
    front_shell = front_shell + pillars_u
    for hx, hy in cm5_holes:
        front_shell = front_shell - cad.standoff(hx, hy, 1.00, z_ceil + 0.05, od=5.30, id_=0.0)

    # F1 camera lens window coordinates at (23.0, -15.7)
    f1 = features["F1"]
    f1_x = ox + float(f1["center_mm"][0])   # 23.0
    f1_y = oy - float(f1["center_mm"][1])   # -15.7
    f1_d = float(f1["size_mm"][0])          # 8.0

    # Internal guide boss for F2 power_button at (38.5, -27.6), clear of the y=-23.7..-7.7 mm FFC U-turn band
    f2 = features["F2"]
    f2_x = ox + float(f2["center_mm"][0])   # 38.5
    f2_y = oy - float(f2["center_mm"][1])   # -27.6
    f2_d = float(f2["size_mm"][0])          # 4.5
    pwr_boss = cad.standoff(f2_x, f2_y, z_max - 5.70, z_ceil + 0.2, od=9.20, id_=0.0)
    front_shell = front_shell + pwr_boss

    # Internal guide boss for F3 boot_pin at (4.5, -10.5)
    f3 = features["F3"]
    f3_x = ox + float(f3["center_mm"][0])   # 4.5
    f3_y = oy - float(f3["center_mm"][1])   # -10.5
    f3_d = float(f3["size_mm"][0])          # 2.0
    boot_boss = cad.standoff(f3_x, f3_y, z_max - 5.70, z_ceil + 0.2, od=6.60, id_=0.0)
    front_shell = front_shell + boot_boss

    # Smooth rounded sight-stop boss behind the J1/J4 gap (X in [44.8, 46.2], Y in [-16.1, -14.1], Z in [2.91, z_ceil+0.2])
    # Blocks +X axis rays at Y = -15.70 mm from escaping through F4 while keeping >= 1.07 mm smooth clearance to the FFC U-turn
    uturn_boss = cad.rounded_box(1.4, 2.0, z_ceil + 0.2 - 2.91, r=0.65, at=(44.8, -16.1, 2.91))
    front_shell = front_shell + uturn_boss

    # Cut F1 camera lens window (d = 8.0 mm through front wall, clearing the 66.3 x 52.3 deg +/- 3 deg FOV cone from Z = 19.75 mm)
    front_shell = front_shell - cad.hole(f1_x, f1_y, d=f1_d, depth=8.0, z0=z_max - 6.0)

    # Cut F2 power button bore (d = 4.5 mm through front wall Z = 17.05..20.5) and flange counterbore (d = 6.8 mm, Z = 13.50..17.05)
    front_shell = front_shell - cad.hole(f2_x, f2_y, d=f2_d, depth=6.0, z0=z_max - 2.95)
    front_shell = front_shell - cad.standoff(f2_x, f2_y, z_max - 6.50, z_max - 2.95, od=6.80, id_=0.0)

    # Cut F3 boot pinhole (d = 2.0 mm through front wall Z = 17.05..20.5) and flange counterbore (d = 4.6 mm, Z = 13.50..17.05)
    front_shell = front_shell - cad.hole(f3_x, f3_y, d=f3_d, depth=6.0, z0=z_max - 2.95)
    front_shell = front_shell - cad.standoff(f3_x, f3_y, z_max - 6.50, z_max - 2.95, od=4.60, id_=0.0)

    # Cut Side Port Openings centered on the 3D connector mouths:
    env_rect = (x_min, y_min, x_max, y_max)
    # J1 USB-C on right wall (board y = 11.5 -> world Y = -11.5, Z = 0.60..4.77 -> open through parting line z_split=0)
    j1_y = -float(bf["placement"]["J1"]["y_mm"])
    front_shell = front_shell - cad.edge_cut(
        "x", center=j1_y, z=2.65, w=10.0, h=5.5, side="max", envelope=env_rect, r=0.8, reach=5.0
    )
    # J4 HDMI on right wall (board y = 25.0 -> world Y = -25.0, Z = 1.60..7.90 -> center Z = 4.75)
    j4_y = -float(bf["placement"]["J4"]["y_mm"])
    front_shell = front_shell - cad.edge_cut(
        "x", center=j4_y, z=4.75, w=16.8, h=6.9, side="max", envelope=env_rect, r=0.8, reach=5.0
    )
    # Internal vertical relief behind right wall under HDMI (X = 54.5..55.80, Y = -33.4..-16.6, Z = -0.1..2.0)
    # so J4 mouth (X_max = 55.49) clears the lower HDMI bezel lip during Z-sweep while keeping a 1.20 mm outer wall
    hdmi_sweep_relief = cad.box(1.30, 16.8, 2.1, at=(54.50, j4_y - 8.4, -0.10))
    front_shell = front_shell - hdmi_sweep_relief
    # J2 USB-A 0 on bottom wall (board x = 16.0 -> world X = 16.0, Z = 1.6..7.3 -> center Z = 4.85)
    j2_x = float(bf["placement"]["J2"]["x_mm"])
    front_shell = front_shell - cad.edge_cut(
        "y", center=j2_x, z=4.85, w=15.0, h=7.3, side="min", envelope=env_rect, r=0.8, reach=5.0
    )
    # J3 USB-A 1 on bottom wall (board x = 35.5 -> world X = 35.5, Z = 1.6..7.3 -> center Z = 4.85)
    j3_x = float(bf["placement"]["J3"]["x_mm"])
    front_shell = front_shell - cad.edge_cut(
        "y", center=j3_x, z=4.85, w=15.0, h=7.3, side="min", envelope=env_rect, r=0.8, reach=5.0
    )

    # Add snap-fit hook on top wall (X in [22.0, 33.0], Y in [0.30, 1.13], Z in [-0.42, 0.20])
    # Stem Y in [0.30, 0.90], Z in [-0.42, 0.50] (clears snap_ridge at Y=0.95..1.25 and cavity wall at Y=0.25); Barb Y in [0.30, 1.13], Z in [-0.42, -0.22]
    snap_stem = cad.box(11.0, 0.60, 0.92, at=(22.0, 0.30, -0.42))
    snap_barb = cad.box(11.0, 0.83, 0.20, at=(22.0, 0.30, -0.42))
    front_shell = front_shell + snap_stem + snap_barb

    cad.export(front_shell, out_dir / "front_shell.stl")

    # -------------------------------------------------------------------------
    # 3. power_button (at (38.5, -27.6), actuating SW1 top at Z = 3.10..3.15 mm)
    # -------------------------------------------------------------------------
    # Cap top: OD = 4.00 mm (r = 2.00 mm < 2.25 mm bore), Z = 16.90 .. 19.85 mm
    # Flange: OD = 6.20 mm (r = 3.10 mm < 3.40 mm counterbore, > 2.25 mm bore), Z = 15.50 .. 16.95 mm
    # Plunger stem: OD = 2.80 mm (r = 1.40 mm), Z = 3.25 .. 15.55 mm
    pwr_cap = cad.standoff(f2_x, f2_y, z_max - 3.10, z_max - 0.15, od=4.00, id_=0.0)
    pwr_flange = cad.standoff(f2_x, f2_y, z_max - 4.50, z_max - 3.05, od=6.20, id_=0.0)
    pwr_stem = cad.standoff(f2_x, f2_y, 3.25, z_max - 4.45, od=2.80, id_=0.0)
    power_button = cad.union(pwr_cap, pwr_flange, pwr_stem)
    cad.export(power_button, out_dir / "power_button.stl")

    # -------------------------------------------------------------------------
    # 4. boot_pin (at (4.5, -10.5), actuating SW2 top at Z = 3.20 mm)
    # -------------------------------------------------------------------------
    # Pin top: OD = 1.60 mm (r = 0.80 mm < 1.00 mm pinhole), Z = 16.90 .. 19.30 mm
    # Flange: OD = 4.00 mm (r = 2.00 mm < 2.30 mm counterbore, > 1.00 mm pinhole), Z = 15.30 .. 16.95 mm
    # Plunger stem: OD = 2.40 mm (r = 1.20 mm), Z = 3.30 .. 15.35 mm
    boot_top = cad.standoff(f3_x, f3_y, z_max - 3.10, z_max - 0.70, od=1.60, id_=0.0)
    boot_flange = cad.standoff(f3_x, f3_y, z_max - 4.70, z_max - 3.05, od=4.00, id_=0.0)
    boot_stem = cad.standoff(f3_x, f3_y, 3.30, z_max - 4.65, od=2.40, id_=0.0)
    boot_pin = cad.union(boot_top, boot_flange, boot_stem)
    cad.export(boot_pin, out_dir / "boot_pin.stl")


def main() -> None:
    bf = cad.board_frame("rea/spec.yaml")
    build_purchased_models(bf, Path("case/purchased"))
    build_enclosure(bf, Path("case/out"))


if __name__ == "__main__":
    main()
