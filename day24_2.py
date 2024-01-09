import math
import re
import numpy as np
from scipy.optimize import least_squares

# 100000 too low

f = open("inputs/day24.txt")
lines = [re.sub(r' +', ' ', line).split(' @ ') for line in f.read().split('\n')]
data = [(line[0].split(', '), line[1].split(', ')) for line in lines]
data = [([int(i) for i in pos], [int(i) for i in vel]) for pos, vel in data]

intersections_in_test_area = 0
# pos = [24, 13, 10]
# vel = [-3, 1, 2]

# x_data = {(d[0][0], d[1][0]) for d in data}
# y_data = {(d[0][1], d[1][1]) for d in data}
# z_data = {(d[0][2], d[1][2]) for d in data}
# x_velocities = [vel for pos, vel in x_data]
# y_velocities = [vel for pos, vel in y_data]
# z_velocities = [vel for pos, vel in z_data]
# excluded_x_vel = {vel for vel in x_velocities if x_velocities.count(vel) > 1}
# excluded_y_vel = {vel for vel in y_velocities if y_velocities.count(vel) > 1}
# excluded_z_vel = {vel for vel in z_velocities if z_velocities.count(vel) > 1}
#
# print(excluded_x_vel, excluded_y_vel, excluded_z_vel)

# for d in data:
#     (x1, y1, z1), (vx1, vy1, vz1) = (pos, vel)
#     (x2, y2, z2), (vx2, vy2, vz2) = d
#
#     if ((x2 - x1) * (vy1 - vy2) * (vz1 - vz2)) == ((y2 - y1) * (vx1 - vx2) * (vz1 - vz2)) == ((z2 - z1) * (vy1 - vy2) * (vx1 - vx2)) and (x2 - x1) * (vx1 - vx2) >= 0:
#         intersections_in_test_area += 1

# px = 24
# py = 13
# pz = 10
# pvx = -3
# pvy = 1
# pvz = 2
#
# a = px
# b = py
# c = pz
# d = pvx
# e = pvy
# f = pvz

((g, h, i), (j, k, l)) = data[0]
((m, n, o), (p, q, r)) = data[1]
((s, t, u), (v, w, x)) = data[2]
((y, z, A), (B, C, D)) = data[3]

mg = m - g
ys = y - s
nh = n - h
zt = z - t
oi = o - i
Au = A - u

for e in range(-1000, 1000):
    qe = q - e
    Ce = C - e
    ke = k - e
    we = w - e

    a1_val = (
            h * (qe) * (Ce)
            - n * (ke) * (Ce)
            - h * (qe) * (we)
            + n * (ke) * (we)
            - t * (Ce) * (qe)
            + z * (we) * (qe)
            + t * (Ce) * (ke)
            - z * (we) * (ke)
    )

    b1_val = (
            - h * (qe) * v * (Ce)
            + n * (ke) * v * (Ce)
            + h * (qe) * B * (we)
            - n * (ke) * B * (we)
            - h * j * (qe) * (Ce)
            + n * p * (ke) * (Ce)
            + h * j * (qe) * (we)
            - n * p * (ke) * (we)
            + (mg) * (ke) * (qe) * (we)
            - (mg) * (ke) * (qe) * (Ce)
            + (ys) * (we) * (Ce) * (qe)
            + t * (Ce) * j * (qe)
            - z * (we) * j * (qe)
            - (ys) * (we) * (Ce) * (ke)
            - t * (Ce) * p * (ke)
            + z * (we) * p * (ke)
            + t * v * (Ce) * (qe)
            - z * B * (we) * (qe)
            - t * v * (Ce) * (ke)
            + z * B * (we) * (ke)
    )

    c1_val = (
            (mg) * (ke) * (qe) * v * (Ce)
            + h * j * (qe) * v * (Ce)
            - n * p * (ke) * v * (Ce)
            - (mg) * (ke) * (qe) * B * (we)
            - h * j * (qe) * B * (we)
            + n * p * (ke) * B * (we)
            - (ys) * (we) * (Ce) * j * (qe)
            - t * v * (Ce) * j * (qe)
            + z * B * (we) * j * (qe)
            + (ys) * (we) * (Ce) * p * (ke)
            + t * v * (Ce) * p * (ke)
            - z * B * (we) * p * (ke)
    )

    a7_val = (
        + h * (w - e) * (C - e)
        - t * (k - e) * (C - e)
        - h * (w - e) * (q - e)
        + t * (k - e) * (q - e)
        - n * (C - e) * (w - e)
        + z * (q - e) * (w - e)
        + n * (C - e) * (k - e)
        - z * (q - e) * (k - e)
    )

    b7_val = (
        - (s - g) * (w - e) * (k - e) * (C - e)
        + (s - g) * (w - e) * (k - e) * (q - e)
        - j * h * (w - e) * (C - e)
        + v * t * (k - e) * (C - e)
        + j * h * (w - e) * (q - e)
        - v * t * (k - e) * (q - e)
        - h * (w - e) * p * (C - e)
        + t * (k - e) * p * (C - e)
        + h * (w - e) * B * (q - e)
        - t * (k - e) * B * (q - e)
        + (y - m) * (C - e) * (q - e) * (w - e)
        - (y - m) * (C - e) * (q - e) * (k - e)
        + p * n * (C - e) * (w - e)
        - B * z * (q - e) * (w - e)
        - p * n * (C - e) * (k - e)
        + B * z * (q - e) * (k - e)
        + n * (C - e) * j * (w - e)
        - z * (q - e) * j * (w - e)
        - n * (C - e) * v * (k - e)
        + z * (q - e) * v * (k - e)
    )

    c7_val = (
        + (s - g) * (w - e) * (k - e) * p * (C - e)
        - (s - g) * (w - e) * (k - e) * B * (q - e)
        + j * h * (w - e) * p * (C - e)
        - v * t * (k - e) * p * (C - e)
        - j * h * (w - e) * B * (q - e)
        + v * t * (k - e) * B * (q - e)
        - (y - m) * (C - e) * (q - e) * j * (w - e)
        + (y - m) * (C - e) * (q - e) * v * (k - e)
        - p * n * (C - e) * j * (w - e)
        + B * z * (q - e) * j * (w - e)
        + p * n * (C - e) * v * (k - e)
        - B * z * (q - e) * v * (k - e)
    )

    if a1_val == 0 or a7_val == 0:
        continue

    D1 = b1_val**2 - 4 * a1_val * c1_val
    D2 = b7_val**2 - 4 * a7_val * c7_val

    if D1 < 0 or D2 < 0:
        continue

    d1 = (-b1_val - math.sqrt(D1)) / (2 * a1_val)
    d2 = (-b7_val - math.sqrt(D2)) / (2 * a7_val)

    if abs(d1 - d2) < 0.0000001:
        d = round(d1)
        a = ((n - h) * (j - d) * (p - d) + g * (k - e) * (p - d) - m * (q - e) * (j - d)) / ((k - e) * (p - d) - (q - e) * (j - d))
        b = (k - e) * (a - g) / (j - d) + h
        f = (r * (b - n) * (k - e) + (o - i) * (k - e) * (q - e) - l * (b - h) * (q - e)) / ((b - n) * (k - e) - (b - h) * (q - e))
        c = (l - f) * (b - h) / (k - e) + i
        print(round(a + b + c))

# for d in range(-100, 100):
#     for e in range(-100, 100):
#         for f in range(-100, 100):
#             qe = q - e
#             Ce = C - e
#             ke = k - e
#             we = w - e
#
#             a1_val = (
#                 h * (qe) * (Ce)
#                 - n * (ke) * (Ce)
#                 - h * (qe) * (we)
#                 + n * (ke) * (we)
#                 - t * (Ce) * (qe)
#                 + z * (we) * (qe)
#                 + t * (Ce) * (ke)
#                 - z * (we) * (ke)
#             )
#
#             b1_val = (
#                 - h * (qe) * v * (Ce)
#                 + n * (ke) * v * (Ce)
#                 + h * (qe) * B * (we)
#                 - n * (ke) * B * (we)
#                 - h * j * (qe) * (Ce)
#                 + n * p * (ke) * (Ce)
#                 + h * j * (qe) * (we)
#                 - n * p * (ke) * (we)
#                 + (mg) * (ke) * (qe) * (we)
#                 - (mg) * (ke) * (qe) * (Ce)
#                 + (ys) * (we) * (Ce) * (qe)
#                 + t * (Ce) * j * (qe)
#                 - z * (we) * j * (qe)
#                 - (ys) * (we) * (Ce) * (ke)
#                 - t * (Ce) * p * (ke)
#                 + z * (we) * p * (ke)
#                 + t * v * (Ce) * (qe)
#                 - z * B * (we) * (qe)
#                 - t * v * (Ce) * (ke)
#                 + z * B * (we) * (ke)
#             )
#
#             c1_val = (
#                 (mg) * (ke) * (qe) * v * (Ce)
#                 + h * j * (qe) * v * (Ce)
#                 - n * p * (ke) * v * (Ce)
#                 - (mg) * (ke) * (qe) * B * (we)
#                 - h * j * (qe) * B * (we)
#                 + n * p * (ke) * B * (we)
#                 - (ys) * (we) * (Ce) * j * (qe)
#                 - t * v * (Ce) * j * (qe)
#                 + z * B * (we) * j * (qe)
#                 + (ys) * (we) * (Ce) * p * (ke)
#                 + t * v * (Ce) * p * (ke)
#                 - z * B * (we) * p * (ke)
#             )
#
#             rf = r - f
#             Df = D - f
#             lf = l - f
#             xf = x - f
#
#             a2_val = (
#                 i * (rf) * (Df)
#                 - o * (lf) * (Df)
#                 - i * (rf) * (xf)
#                 + o * (lf) * (xf)
#                 - u * (Df) * (rf)
#                 + A * (xf) * (rf)
#                 + u * (Df) * (lf)
#                 - A * (xf) * (lf)
#             )
#
#             b2_val = (
#                 - i * (rf) * v * (Df)
#                 + o * (lf) * v * (Df)
#                 + i * (rf) * B * (xf)
#                 - o * (lf) * B * (xf)
#
#                 - i * j * (rf) * (Df)
#                 + o * p * (lf) * (Df)
#                 + i * j * (rf) * (xf)
#                 - o * p * (lf) * (xf)
#                 + (mg) * (lf) * (rf) * (xf)
#                 - (mg) * (lf) * (rf) * (Df)
#                 + (ys) * (xf) * (Df) * (rf)
#                 + u * (Df) * j * (rf)
#                 - A * (xf) * j * (rf)
#                 - (ys) * (xf) * (Df) * (lf)
#                 - u * (Df) * p * (lf)
#                 + A * (xf) * p * (lf)
#
#                 + u * v * (Df) * (rf)
#                 - A * B * (xf) * (rf)
#                 - u * v * (Df) * (lf)
#                 + A * B * (xf) * (lf)
#             )
#
#             c2_val = (
#                 (mg) * (lf) * (rf) * v * (Df)
#                 + i * j * (rf) * v * (Df)
#                 - o * p * (lf) * v * (Df)
#                 - (mg) * (lf) * (rf) * B * (xf)
#                 - i * j * (rf) * B * (xf)
#                 + o * p * (lf) * B * (xf)
#                 - (ys) * (xf) * (Df) * j * (rf)
#                 - u * v * (Df) * j * (rf)
#                 + A * B * (xf) * j * (rf)
#                 + (ys) * (xf) * (Df) * p * (lf)
#                 + u * v * (Df) * p * (lf)
#                 - A * B * (xf) * p * (lf)
#             )
#
#             jd = j - d
#             vd = v - d
#             Bd = B - d
#             pd = p - d
#
#             a3_val = (
#                 m * (jd) * (vd)
#                 - m * (jd) * (Bd)
#                 - g * (pd) * (vd)
#                 + g * (pd) * (Bd)
#                 - s * (Bd) * (pd)
#                 + s * (Bd) * (jd)
#                 + y * (vd) * (pd)
#                 - y * (vd) * (jd)
#             )
#
#             b3_val = (
#                 - g * k * (pd) * (Bd)
#                 + g * k * (pd) * (vd)
#                 - g * w * (pd) * (Bd)
#                 + g * C * (pd) * (vd)
#                 + m * q * (jd) * (Bd)
#                 - m * q * (jd) * (vd)
#                 + m * w * (jd) * (Bd)
#                 - m * C * (jd) * (vd)
#                 + s * k * (Bd) * (pd)
#                 + s * w * (Bd) * (pd)
#                 - s * q * (Bd) * (jd)
#                 - s * w * (Bd) * (jd)
#                 - y * k * (vd) * (pd)
#                 - y * C * (vd) * (pd)
#                 + y * q * (vd) * (jd)
#                 + y * C * (vd) * (jd)
#                 - (nh) * (jd) * (pd) * (Bd)
#                 + (nh) * (jd) * (pd) * (vd)
#                 + (zt) * (vd) * (Bd) * (pd)
#                 - (zt) * (vd) * (Bd) * (jd)
#             )
#
#             c3_val = (
#                 g * k * w * (pd) * (Bd)
#                 - g * k * C * (pd) * (vd)
#                 - m * q * w * (jd) * (Bd)
#                 + m * q * C * (jd) * (vd)
#                 - s * w * k * (Bd) * (pd)
#                 + s * w * q * (Bd) * (jd)
#                 + y * C * k * (vd) * (pd)
#                 - y * C * q * (vd) * (jd)
#                 - k * (zt) * (vd) * (Bd) * (pd)
#                 + q * (zt) * (vd) * (Bd) * (jd)
#                 + w * (nh) * (jd) * (pd) * (Bd)
#                 - C * (nh) * (jd) * (pd) * (vd)
#             )
#
#             a4_val = (
#                 o * (lf) * (xf)
#                 - o * (lf) * (Df)
#                 - i * (rf) * (xf)
#                 + i * (rf) * (Df)
#                 - u * (Df) * (rf)
#                 + u * (Df) * (lf)
#                 + A * (xf) * (rf)
#                 - A * (xf) * (lf)
#             )
#
#             b4_val = (
#                 - i * k * (rf) * (Df)
#                 + i * k * (rf) * (xf)
#                 - i * w * (rf) * (Df)
#                 + i * C * (rf) * (xf)
#                 + o * q * (lf) * (Df)
#                 - o * q * (lf) * (xf)
#                 + o * w * (lf) * (Df)
#                 - o * C * (lf) * (xf)
#                 + u * k * (Df) * (rf)
#                 + u * w * (Df) * (rf)
#                 - u * q * (Df) * (lf)
#                 - u * w * (Df) * (lf)
#                 - A * k * (xf) * (rf)
#                 - A * C * (xf) * (rf)
#                 + A * q * (xf) * (lf)
#                 + A * C * (xf) * (lf)
#                 - (nh) * (lf) * (rf) * (Df)
#                 + (nh) * (lf) * (rf) * (xf)
#                 + (zt) * (xf) * (Df) * (rf)
#                 - (zt) * (xf) * (Df) * (lf)
#             )
#
#             c4_val = (
#                 i * k * w * (rf) * (Df)
#                 - i * k * C * (rf) * (xf)
#                 - o * q * w * (lf) * (Df)
#                 + o * q * C * (lf) * (xf)
#                 - u * w * k * (Df) * (rf)
#                 + u * w * q * (Df) * (lf)
#                 + A * C * k * (xf) * (rf)
#                 - A * C * q * (xf) * (lf)
#                 - k * (zt) * (xf) * (Df) * (rf)
#                 + q * (zt) * (xf) * (Df) * (lf)
#                 + w * (nh) * (lf) * (rf) * (Df)
#                 - C * (nh) * (lf) * (rf) * (xf)
#             )
#
#             a5_val = (
#                 h * (qe) * (Ce)
#                 - n * (ke) * (Ce)
#                 - h * (qe) * (we)
#                 + n * (ke) * (we)
#                 - t * (Ce) * (qe)
#                 + z * (we) * (qe)
#                 + t * (Ce) * (ke)
#                 - z * (we) * (ke)
#             )
#
#             b5_val = (
#                 - (oi) * (ke) * (qe) * (Ce)
#                 + (oi) * (ke) * (qe) * (we)
#                 - h * l * (qe) * (Ce)
#                 + n * r * (ke) * (Ce)
#                 + h * l * (qe) * (we)
#                 - n * r * (ke) * (we)
#                 - h * (qe) * x * (Ce)
#                 + n * (ke) * x * (Ce)
#                 + h * (qe) * D * (we)
#                 - n * (ke) * D * (we)
#                 + (Au) * (we) * (Ce) * (qe)
#                 - (Au) * (we) * (Ce) * (ke)
#                 + t * x * (Ce) * (qe)
#                 - z * D * (we) * (qe)
#                 - t * x * (Ce) * (ke)
#                 + z * D * (we) * (ke)
#                 + t * (Ce) * l * (qe)
#                 - z * (we) * l * (qe)
#                 - t * (Ce) * r * (ke)
#                 + z * (we) * r * (ke)
#             )
#
#             c5_val = (
#                 (oi) * (ke) * (qe) * x * (Ce)
#                 - (oi) * (ke) * (qe) * D * (we)
#                 + h * l * (qe) * x * (Ce)
#                 - n * r * (ke) * x * (Ce)
#                 - h * l * (qe) * D * (we)
#                 + n * r * (ke) * D * (we)
#                 - (Au) * (we) * (Ce) * l * (qe)
#                 + (Au) * (we) * (Ce) * r * (ke)
#                 - t * x * (Ce) * l * (qe)
#                 + z * D * (we) * l * (qe)
#                 + t * x * (Ce) * r * (ke)
#                 - z * D * (we) * r * (ke)
#             )
#
#             a6_val = (
#                 g * (pd) * (Bd)
#                 - m * (jd) * (Bd)
#                 - g * (pd) * (vd)
#                 + m * (jd) * (vd)
#                 - s * (Bd) * (pd)
#                 + y * (vd) * (pd)
#                 + s * (Bd) * (jd)
#                 - y * (vd) * (jd)
#             )
#
#             b6_val = (
#                 - (oi) * (jd) * (pd) * (Bd)
#                 + (oi) * (jd) * (pd) * (vd)
#                 - g * l * (pd) * (Bd)
#                 + m * r * (jd) * (Bd)
#                 + g * l * (pd) * (vd)
#                 - m * r * (jd) * (vd)
#                 - g * (pd) * x * (Bd)
#                 + m * (jd) * x * (Bd)
#                 + g * (pd) * D * (vd)
#                 - m * (jd) * D * (vd)
#                 + (Au) * (vd) * (Bd) * (pd)
#                 - (Au) * (vd) * (Bd) * (jd)
#                 + s * x * (Bd) * (pd)
#                 - y * D * (vd) * (pd)
#                 - s * x * (Bd) * (jd)
#                 + y * D * (vd) * (jd)
#                 + s * (Bd) * l * (pd)
#                 - y * (vd) * l * (pd)
#                 - s * (Bd) * r * (jd)
#                 + y * (vd) * r * (jd)
#             )
#
#             c6_val = (
#                 (oi) * (jd) * (pd) * x * (Bd)
#                 - (oi) * (jd) * (pd) * D * (vd)
#                 + g * l * (pd) * x * (Bd)
#                 - m * r * (jd) * x * (Bd)
#                 - g * l * (pd) * D * (vd)
#                 + m * r * (jd) * D * (vd)
#                 - (Au) * (vd) * (Bd) * l * (pd)
#                 + (Au) * (vd) * (Bd) * r * (jd)
#                 - s * x * (Bd) * l * (pd)
#                 + y * D * (vd) * l * (pd)
#                 + s * x * (Bd) * r * (jd)
#                 - y * D * (vd) * r * (jd)
#             )
#
#             D1 = b1_val**2 - 4 * a1_val * c1_val
#             D2 = b2_val**2 - 4 * a2_val * c2_val
#             D3 = b3_val**2 - 4 * a3_val * c3_val
#             D4 = b4_val**2 - 4 * a4_val * c4_val
#             D5 = b5_val**2 - 4 * a5_val * c5_val
#             D6 = b6_val**2 - 4 * a6_val * c6_val
#
#             if D1 < 0 or D2 < 0 or D3 < 0 or D4 < 0 or D5 < 0 or D6 < 0:
#                 continue
#
#             if a1_val == 0 or a2_val == 0 or a3_val == 0 or a4_val == 0 or a5_val == 0 or a6_val == 0:
#                 continue
#
#             d1_val = (-b1_val + math.sqrt(D1)) / (2 * a1_val)
#             d2_val = (-b1_val - math.sqrt(D1)) / (2 * a1_val)
#             d3_val = (-b2_val + math.sqrt(D2)) / (2 * a2_val)
#             d4_val = (-b2_val - math.sqrt(D2)) / (2 * a2_val)
#
#             e1_val = (-b3_val + math.sqrt(D3)) / (2 * a3_val)
#             e2_val = (-b3_val - math.sqrt(D3)) / (2 * a3_val)
#             e3_val = (-b4_val + math.sqrt(D4)) / (2 * a4_val)
#             e4_val = (-b4_val - math.sqrt(D4)) / (2 * a4_val)
#
#             f1_val = (-b5_val + math.sqrt(D5)) / (2 * a5_val)
#             f2_val = (-b5_val - math.sqrt(D5)) / (2 * a5_val)
#             f3_val = (-b6_val + math.sqrt(D6)) / (2 * a6_val)
#             f4_val = (-b6_val - math.sqrt(D6)) / (2 * a6_val)
#
#             d_intersection = {d1_val, d2_val}.intersection({d3_val, d4_val})
#             e_intersection = {e1_val, e2_val}.intersection({e3_val, e4_val})
#             f_intersection = {f1_val, f2_val}.intersection({f3_val, f4_val})
#
#             if len(d_intersection) > 0 and len(e_intersection) > 0 and len(f_intersection) > 0:
#                 print(d_intersection, e_intersection, f_intersection)