import itertools
import sys

def main():
    inp = input()

    filemap = []
    i = 0
    n = 0
    while True:
        for _ in range(int(inp[i])):
            filemap += [str(n)]
        i += 1
        n += 1
        if i == len(inp): break
        for _ in range(int(inp[i])):
            filemap += ["."]
        i += 1
        if i == len(inp): break
    # print(filemap)
    filemap2 = filemap.copy()


    i = len(filemap) - 1
    j = 0

    def visualize():
        return
        print("".join(filemap))
        print(" " * j + "j" + " " * (i - j - 1) + "i")
        input()

    visualize()
    while i >= 0 and i != j + 1:
        if filemap[i] != ".":
            while True:
                if i == j + 1: break
                if filemap[j] == ".":
                    filemap[i], filemap[j] = filemap[j], filemap[i]
                    visualize()
                    break
                else:
                    j += 1
                    visualize()
        if i == j + 1: break
        i -= 1
        visualize()

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(1, sum(a * int(b) for a,b in enumerate(filemap) if b != "."))
    print(2, None)

main()
