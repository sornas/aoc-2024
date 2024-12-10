import itertools
import sys

def main():
    inp = sys.stdin.read().strip().splitlines()

    m = [list(map(int, line)) for line in inp]
    w = len(m[0])
    h = len(m)
    starts = []
    for x, y in itertools.product(range(h), range(w)):
        if m[y][x] == 0:
            starts.append((x,y))

    def in_range(x,y):
        return 0 <= x < w and 0 <= y < h

    r = 0
    for s in starts:
        # find reachable nines from this zero
        q = [s]
        seen = set([s])
        while q:
            x, y = q.pop()
            if m[y][x] == 9:
                r += 1
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if in_range(x+dx,y+dy) and m[y+dy][x+dx] == m[y][x] + 1:
                    q.append((x+dx,y+dy))


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(1, r)
    print(2, None)

main()
