import collections
import heapq
import sys

def main():
    inp = sys.stdin.read().strip().splitlines()

    walls = set()
    start = None
    end = None
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if c == "#":
                walls.add((x,y))
            if c == "S":
                start = (x,y)
            if c == "E":
                end = (x,y)

    q = [(0, (start, (1, 0)))]

    dist = collections.defaultdict(lambda: float("Inf"))
    prev = collections.defaultdict(set)

    while q:
        cost, (pos, dir) = heapq.heappop(q)

        px, py = pos
        dx, dy = dir

        if pos == end:
            break

        def alt(cost, pos2, dir2):
            if cost <= dist[(pos2, dir2)]:
                prev[(pos2, dir2)].add((pos, dir))
                dist[(pos2, dir2)] = cost
                heapq.heappush(q, (cost, (pos2, dir2)))

        if (px+dx, py+dy) not in walls:
            alt(cost + 1, (px+dx, py+dy), (dx, dy))
        alt(cost + 1000, (px, py), (-dy, dx))
        alt(cost + 1000, (px, py), (dy, -dx))

    s = set()
    seen = set()

    def bingbong(p, d):
        if (p, d) in seen:
            return

        seen.add((p, d))
        s.add(p)
        for p2, d2 in prev[(p, d)]:
            bingbong(p2, d2)

    mindir = None
    mincost = float("Inf")
    for dir in [(-1,0),(1,0),(0,1),(0,-1)]:
        if (cost := dist[(end, dir)]) < mincost:
            mincost = cost
            mindir = dir

    bingbong(end, mindir)


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(1, min(dist[(end, dir)] for dir in [(-1,0),(1,0),(0,1),(0,-1)]))
    print(2, len(s))

main()
