import sys
import itertools

def main():
    inp = sys.stdin.read().strip()

    ks = []
    ls = []
    for kl in inp.split("\n\n"):
        kl = kl.splitlines()
        h = []
        for x in range(5):
            s = 0
            for y in range(5):
                if kl[y+1][x] == "#":
                    s += 1
            h.append(s)
        if kl[0][0] == ".":
            ks.append(h)
        else:
            ls.append(h)
    s = 0
    for k, l in itertools.product(ks, ls):
        for a, b in zip(k, l):
            if a + b > 5:
                break
        else:
            s += 1

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(s)

main()
