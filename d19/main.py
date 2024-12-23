import functools
import sys

def main():
    inp = sys.stdin.read().strip().splitlines()
    avail = inp[0].split(", ")
    pats = inp[2:]

    print(avail, pats)

    @functools.cache
    def can_make(pat: str):
        n = 0
        for a in avail:
            if a == pat:
                n += 1
            elif pat.startswith(a):
                n += can_make(pat[len(a):])
        return n


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(sum(can_make(p) for p in pats))

main()
