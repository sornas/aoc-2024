import re
import sys
import numpy as np

def is_almost_integer(f, eps):
    return abs(round(f) - f) < eps

def solve(inp, part):
    regex = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
    eps = 0.001

    s = 0
    for claw in inp.split("\n\n"):
        x1, y1, x2, y2, x, y = list(map(int, regex.match(claw).groups()))
        if part == 2:
            x += 10000000000000
            y += 10000000000000
        a = np.array([[x1, x2], [y1, y2]])
        b = np.array([x, y])
        tx, ty = np.linalg.solve(a, b)
        if is_almost_integer(tx, eps) and is_almost_integer(ty, eps):
            tx = int(round(tx))
            ty = int(round(ty))
            s += tx * 3 + ty

    return s

def main():
    inp = sys.stdin.read().strip()
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(1, solve(inp, 1))
    print(2, solve(inp, 2))

main()
