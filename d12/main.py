import collections
import itertools
import sys

def main():
    inp = sys.stdin.read().strip().splitlines()
    h = len(inp)
    w = len(inp[0])

    def in_range(x,y):
        return 0<=x<w and 0<=y<h

    regions = collections.defaultdict(list)
    for x,y in itertools.product(range(w), range(h)):
        regions[inp[y][x]].append((x,y))

    def connects(p1, p2):
        p1x, p1y = p1
        start_region = inp[p1y][p1x]
        s = [p1]
        seen = set()
        # print(p1, p2, start_region)
        while s:
            # print(s)
            p = s.pop()
            seen.add(p)
            if p == p2:
                # print("yes")
                return True
            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                px, py = p
                pp = (px + dx, py + dy)
                # print(p, (dx, dy), pp, in_range(*pp), pp not in seen, inp[py+dy][px+dx] if in_range(*pp) else None)
                if in_range(*pp) and pp not in seen and inp[py+dy][px+dx] == start_region:
                    s.append(pp)
        # print("no")
        return False

    split_regions = []
    for c, region in regions.items():
        while True:
            if not region:
                break
            first = region.pop()
            new_region = [first]
            i = 0
            while i < len(region):
                if connects(first, region[i]):
                    new_region.append(region.pop(i))
                else:
                    i += 1
            split_regions.append(new_region)

    def area(region):
        return region

    def perimiter(region):
        peri = []
        for px, py in region:
            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                p = (px+dx, py+dy)
                if p not in region:
                    peri.append(p)
        return peri

    # for r in split_regions:
    #     a = area(r)
    #     p = perimiter(r)
    #     print(inp[r[0][1]][r[0][0]], r, len(a), len(p), len(a) * len(p))
    #     for y in range(h):
    #         for x in range(w):
    #             xy = (x, y)
    #             if xy in a:
    #                 print("#", end="")
    #             elif xy in p:
    #                 print("+", end="")
    #             else:
    #                 print(".", end="")
    #         print()

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(sum(len(area(r)) * len(perimiter(r)) for r in split_regions))

main()