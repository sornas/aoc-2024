import collections
import itertools
import sys

def main():
    inp = sys.stdin.read()
    inp = list(map(int, inp.split()))
    inp = {k: inp.count(k) for k in inp}
    inp = collections.defaultdict(lambda: 0, inp)


    def step(stones):
        new = collections.defaultdict(lambda: 0)
        for stone, amount in stones.items():
            sstone = str(stone)
            if stone == 0:
                new[1] += amount
            elif len(sstone) % 2 ==0:
                new[int(sstone[:len(sstone)//2])] += amount
                new[int(sstone[len(sstone)//2:])] += amount
            else:
                new[stone * 2024] += amount
        return new

    p1 = 0
    for i in range(75):
        print(i, len(inp), sum(inp.values()))
        if i == 25:
            p1 = sum(inp.values())
        inp = step(inp)

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(1, p1)
    print(2, sum(inp.values()))

main()
