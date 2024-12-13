import re
import sys
import numpy as np

def is_almost_integer(f):
    return abs(round(f) - f) < 0.001

def main():
    inp = sys.stdin.read().strip()
    regex = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")

    s = 0
    for claw in inp.split("\n\n"):
        x1, y1, x2, y2, x, y = list(map(int, regex.match(claw).groups()))
        x += 10000000000000
        y += 10000000000000
        a = np.array([[x1, x2], [y1, y2]])
        b = np.array([x, y])
        tx, ty = np.linalg.solve(a, b)
        print(tx, ty)
        if is_almost_integer(tx) and is_almost_integer(ty):
            tx = int(round(tx))
            ty = int(round(ty))
            s += tx * 3 + ty

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(s)

main()
