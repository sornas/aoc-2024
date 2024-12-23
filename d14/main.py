import math
import re
import sys

def main():
    inp = sys.stdin.read().strip()
    digit = re.compile(r"-?\d+")
    robots = []
    for line in inp.splitlines():
        px, py, vx, vy = list(map(int, digit.findall(line)))
        robots.append(((px, py), (vx, vy)))

    w = 101
    h = 103

    def step():
        nonlocal robots
        new_robots = []
        while robots:
            (px, py), (vx, vy) = robots.pop(0)
            px = (px + vx) % w
            py = (py + vy) % h
            new_robots.append(((px, py), (vx, vy)))
        robots = new_robots

    xmid = w // 2
    ymid = h // 2

    def dngr():
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0

        for robot in robots:
            (px, py), _ = robot
            if px < xmid and py < ymid: q1 += 1
            elif px > xmid and py < ymid: q2 += 1
            elif px < xmid and py > ymid: q3 += 1
            elif px > xmid and py > ymid: q4 += 1
        return math.prod([q1, q2, q3, q4])

    for i in range(15000):
        step()
        if (d := dngr()) < 200000000:
            print(i+1, dngr())


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(dngr())

main()
