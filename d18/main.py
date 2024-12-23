import sys
from collections import deque

def main():
    inp = sys.stdin.read().strip().splitlines()
    h = w = 71

    bb = list(tuple(map(int, xy.split(","))) for xy in inp)

    start = (0,0)
    end = (h-1,w-1)

    for i in range(len(bb)):
        print(i, len(bb))
        bbs = set(bb[:i])
        q = deque([start])
        dist = dict()
        dist[start] = 0
        while q:
            x,y = q.popleft()
            for nx,ny in [(-1,0),(1,0),(0,1),(0,-1)]:
                pn = (x+nx,y+ny)
                if 0 <= x+nx < w and 0 <= y+ny < h:
                    if pn not in dist and pn not in bbs:
                        dist[pn] = dist[(x,y)] + 1
                        q.append(pn)
        if end not in dist:
            print(bb[i-1])
            return

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    # print(dist[end])

main()
