import math
import re

# 131633231355646 371683716481156 238674624073734 268 -197 68

f = open("inputs/day24.txt")
lines = [re.sub(r' +', ' ', line).split(' @ ') for line in f.read().split('\n')]
data = [(line[0].split(', '), line[1].split(', ')) for line in lines]
data = [([int(i) for i in pos], [int(i) for i in vel]) for pos, vel in data]


def is_whole(value):
    return abs(value - float(round(value))) < 1e-12


def round_if_close(value):
    if is_whole(value):
        return round(value)
    else:
        return value


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

    d1 = round_if_close((-b1_val - math.sqrt(D1)) / (2 * a1_val))
    d2 = round_if_close((-b7_val - math.sqrt(D2)) / (2 * a7_val))
    d3 = round_if_close((-b1_val + math.sqrt(D1)) / (2 * a1_val))
    d4 = round_if_close((-b7_val + math.sqrt(D2)) / (2 * a7_val))

    intersection = {d1, d3}.intersection({d2, d4})

    intersection = list(filter(is_whole, intersection))

    if len(intersection) == 0:
        continue

    for d in intersection:
        if ((k - e) * (p - d) - (q - e) * (j - d)) != 0:
            a = ((n - h) * (j - d) * (p - d) + g * (k - e) * (p - d) - m * (q - e) * (j - d)) / ((k - e) * (p - d) - (q - e) * (j - d))
        else:
            a = ((z - t) * (v - d) * (B - d) + s * (w - e) * (B - d) - y * (C - e) * (v - d)) / ((w - e) * (B - d) - (C - e) * (v - d))
        if j - d != 0:
            b = (k - e) * (a - g) / (j - d) + h
        else:
            b = (q - e) * (a - m) / (p - d) + n
        if ((b - n) * (k - e) - (b - h) * (q - e)) != 0:
            f = (r * (b - n) * (k - e) + (o - i) * (k - e) * (q - e) - l * (b - h) * (q - e)) / ((b - n) * (k - e) - (b - h) * (q - e))
        else:
            f = (D * (b - z) * (w - e) + (A - u) * (w - e) * (C - e) - x * (b - t) * (C - e)) / ((b - z) * (w - e) - (b - t) * (C - e))
        if k - e != 0:
            c = (l - f) * (b - h) / (k - e) + i
        else:
            c = (r - f) * (b - n) / (q - e) + o

        direction = [round_if_close(d), round_if_close(e), round_if_close(f)]

        if len(list(filter(is_whole, direction))) != len(direction) or direction in [[j, k, l], [p, q, r], [v, w, x], [B, C, D]]:
            continue

        print(round(a) + round(b) + round(c))
