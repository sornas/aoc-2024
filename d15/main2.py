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

    grid = [["." for _ in range(len(inp1[0]) * 2)] for _ in range(len(inp1))]
    robot = None
    for y, line in enumerate(inp1):
        for x, c in enumerate(line):
            if c == "@":
                robot = (2*x, y)
                grid[y][2*x] = "."
                grid[y][2*x+1] = "."
            elif c == "O":
                grid[y][2*x] = "["
                grid[y][2*x+1] = "]"
            else:
                grid[y][2*x] = c
                grid[y][2*x+1] = c


    draw(grid, robot)

    for move in moves:
        x, y = robot
        print(move, x, y)
        if move == "^": dx, dy =  0, -1
        if move == "v": dx, dy =  0,  1
        if move == "<": dx, dy = -1,  0
        if move == ">": dx, dy =  1,  0

        if dy == 0:
            print("L/R")
            steps = 1
            found_wall = False
            while True:
                p = grid[y + dy * steps][x + dx * steps]
                if p == "#":
                    found_wall = True
                    break
                elif p == ".":
                    break
                elif p == "[" or p == "]":
                    steps += 1
                else:
                    assert False
            if not found_wall:
                for i in range(steps)[::-1]:
                    grid[y + dy * (i+1)][x + dx * (i+1)] = grid[y + dy * i][x + dx * i]
                robot = (x + dx, y + dy)
        else:
            print("U/D")
            steps = 1
            front = set([0])
            found_wall = False
            to_push = []
            while True:
                print("steps", steps, front)
                new_front = set()
                found_box = False
                for f in front:
                    px, py = x + dx * steps + f, y + dy * steps
                    p = grid[y + dy * steps][x + dx * steps + f]
                    print("f", f, px, py, p)
                    if p == "#":
                        found_wall = True
                        break
                    elif p == ".":
                        # check next in front
                        continue
                    elif p == "[":
                        to_push.append((px, py))
                        to_push.append((px+1, py))
                        new_front.add(f)
                        new_front.add(f + 1)
                        found_box = True
                    elif p == "]":
                        to_push.append((px, py))
                        to_push.append((px-1, py))
                        new_front.add(f)
                        new_front.add(f - 1)
                        found_box = True
                    else:
                        assert False
                front = new_front
                if found_wall or not found_box:
                    break
                steps += 1
            if not found_wall:
                print("pushing", to_push)
                for px, py in to_push[::-1]:
                    grid[py + dy][px + dx] = grid[py][px]
                    grid[py][px] = "."
                robot = (x + dx, y + dy)
        draw(grid, robot)

    s = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "[":
                s += 100 * y + x


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(s)

main()
