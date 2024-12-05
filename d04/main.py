import itertools
import sys

def main():
    i = sys.stdin.readlines()
    h = len(i)
    w = len(i[0])

    def in_range(x, y):
        return 0 <= x < w and 0 <= y < h

    def starts_xmas(x, y):
        s = 0
        for dx, dy in itertools.product([-1,0,1],[-1,0,1]):
            if (dx, dy) == (0,0):
                continue
            if all(in_range(x+dx*ii, y+dy*ii) and i[y+dy*ii][x+dx*ii] == c for ii, c in enumerate("xmas")):
                s += 1
        return s

    def starts_x_mas(x, y):
        return (
            i[y][x] == "A"
            and in_range(x-1,y-1)
            and in_range(x+1, y+1)
            and (
                (i[y-1][x-1] == "M" and i[y+1][x+1] == "S")
                or (i[y-1][x-1] == "S" and i[y+1][x+1] == "M")
            )
            and (
                (i[y-1][x+1] == "M" and i[y+1][x-1] == "S")
                or (i[y-1][x+1] == "S" and i[y+1][x-1] == "M")
            )
        )

    s = 0
    for y in range(h):
        for x in range(w):
            s += starts_xmas(x,y)
    print(1, s)

    s = 0
    for y in range(h):
        for x in range(w):
            if starts_x_mas(x, y):
                s += 1
    print(2, s)


main()
