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
        peri = set()
        for px, py in region:
            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                p = (px+dx, py+dy)
                if p not in region:
                    peri.add((p, (dx,dy)))
        return peri


    def perimiter2(region):
        peri = set()
        for px, py in region:
            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                p = (px+dx, py+dy)
                if p not in region:
                    peri.add((p, (dx,dy)))
        merged_peri = []
        while peri:
            # take one out
            p, n = peri.pop()
            line = [p]
            px, py = p
            t1 = (n[1], n[0])
            t2 = (-n[1], -n[0])
            # go both ways
            for tx, ty in [t1,t2]:
                i = 1
                while True:
                    if (other := ((px+tx*i, py+ty*i), n)) in peri:
                        peri.remove(other)
                        line.append(other[0])
                    else:
                        break
                    i += 1
            merged_peri.append(line)
        return merged_peri

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")


    print(1, sum(len(area(r)) * len(perimiter(r)) for r in split_regions))
    print(2, sum(len(area(r)) * len(perimiter2(r)) for r in split_regions))

main()
