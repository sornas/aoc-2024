import sys

def main():
    inp = sys.stdin.read().strip().splitlines()
    antennas = {}
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            if c != ".":
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append((x,y))

    def in_range(x, y):
        return 0 <= x < len(inp[0]) and 0 <= y < len(inp)

    nodes1 = set()
    nodes2 = set()
    for _, locs in antennas.items():
        for i, loc1 in enumerate(locs):
            for loc2 in locs[i+1:]:
                dx = loc2[0] - loc1[0]
                dy = loc2[1] - loc1[1]

                # part 1
                if in_range(loc1[0] - dx, loc1[1] - dy):
                    nodes1.add((loc1[0] - dx, loc1[1] - dy))
                if in_range(loc2[0] + dx, loc2[1] + dy):
                    nodes1.add((loc2[0] + dx, loc2[1] + dy))

                # part 2
                j = 0
                while True:
                    if in_range(loc1[0] - dx*j, loc1[1] - dy*j):
                        nodes2.add((loc1[0] - dx*j, loc1[1] - dy*j))
                    else:
                        break
                    j += 1
                j = 0
                while True:
                    if in_range(loc2[0] + dx*j, loc2[1] + dy*j):
                        nodes2.add((loc2[0] + dx*j, loc2[1] + dy*j))
                    else:
                        break
                    j += 1


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(1, len(nodes1))
    print(2, len(nodes2))

main()
