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

    nodes = set()
    for _, locs in antennas.items():
        for i, loc1 in enumerate(locs):
            for loc2 in locs[i+1:]:
                dx = loc2[0] - loc1[0]
                dy = loc2[1] - loc1[1]
                i = 0
                while True:
                    if in_range(loc1[0] - dx*i, loc1[1] - dy*i):
                        nodes.add((loc1[0] - dx*i, loc1[1] - dy*i))
                    else:
                        break
                    i += 1
                i = 0
                while True:
                    if in_range(loc2[0] + dx*i, loc2[1] + dy*i):
                        nodes.add((loc2[0] + dx*i, loc2[1] + dy*i))
                    else:
                        break
                    i += 1


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(1, len(nodes))
    print(2, None)

main()
