import sys

def draw(grid, robot):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if (x,y) == robot:
                print("@", end="")
            else:
                print(c, end="")
        print()
    print()

def main():
    inp1, inp2 = sys.stdin.read().strip().split("\n\n")
    inp1 = inp1.splitlines()
    moves = inp2.replace("\n", "")

    grid = [["." for _ in range(len(inp1[0]))] for _ in range(len(inp1))]
    robot = None
    for y, line in enumerate(inp1):
        for x, c in enumerate(line):
            if c == "@":
                robot = (x, y)
                grid[y][x] = "."
            else:
                grid[y][x] = c
    draw(grid, robot)

    for move in moves:
        if move == "^": dx, dy =  0, -1
        if move == "v": dx, dy =  0,  1
        if move == "<": dx, dy = -1,  0
        if move == ">": dx, dy =  1,  0

        steps = 1
        can_push = True
        while True:
            x, y = robot
            p = grid[y + dy * steps][x + dx * steps]
            if p == "#":
                can_push = False
                break
            elif p == ".":
                break
            elif p == "O":
                steps += 1
            else:
                assert False
        if can_push:
            for i in range(steps)[::-1]:
                grid[y + dy * (i+1)][x + dx * (i+1)] = grid[y + dy * i][x + dx * i]
            robot = (x + dx, y + dy)

    s = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "O":
                s += 100 * y + x


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(s)

main()
