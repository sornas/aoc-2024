import itertools
import sys

def main():
    inp = sys.stdin.read().strip().splitlines()

    dd = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    w = len(inp[0])
    h = len(inp)
    start = None
    end = None
    walls = set()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if c == "S":
                start = (x,y)
            if c == "E":
                end = (x,y)
            if c == "#":
                walls.add((x,y))

    dist = dict()
    p = end
    cost = 0
    while p != start:
        dist[p] = cost
        x,y = p
        cost += 1
        for dx, dy in dd:
            if (x+dx, y+dy) not in walls and (x+dx, y+dy) not in dist:
                p = (x+dx, y+dy)
    dist[p] = cost

    path = [p for p, _ in reversed(sorted(dist.items(), key=lambda kv: kv[1]))]

    s = 0
    for (px, py) in path:
        # hur många paths inom 20 steg har kortare dist
        before = dist[(px, py)]
        for dx in range(-20, 21):
            for dy in range(-20, 21):
                if abs(dx) + abs(dy) <= 20:
                    if (px+dx, py+dy) in dist:
                        after = dist[(px+dx, py+dy)]
                        if after + abs(dx) + abs(dy) + 100 <= before:
                            s += 1

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(s)

main()
