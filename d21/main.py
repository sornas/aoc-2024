from copy import copy
from dataclasses import dataclass
from typing import Any, ClassVar
import heapq
import sys

UP = 1
LEFT = 2
DOWN = 3
RIGHT = 4
PRESS = 10



class Arm:
    keys: ClassVar[dict[tuple[int, int], Any]]

    def __init__(self, pos):
        self.pos = pos

    def move(self, d):
        test = copy(self)
        dx = dy = 0
        if d == UP:
            dy = -1
        elif d == DOWN:
            dy = 1
        elif d == RIGHT:
            dx = 1
        elif d == LEFT:
            dx = -1
        x, y = test.pos
        x += dx
        y += dy
        if (x, y) in test.keys:
            test.pos = (x, y)
            return test
        return None

    def __lt__(self, other):
        return self.pos.__lt__(other.pos)

class Numeric(Arm):
    keys = {
        (0,0): "7",
        (1,0): "8",
        (2,0): "9",
        (0,1): "4",
        (1,1): "5",
        (2,1): "6",
        (0,2): "1",
        (1,2): "2",
        (2,2): "3",
        (1,3): "0",
        (2,3): "A"
    }

    def __init__(self):
        super().__init__((2, 3))

class Directional(Arm):
    keys = {
        (1,0): UP,  # up
        (2,0): PRESS, # A
        (0,1): LEFT,  # left
        (1,1): DOWN,  # down
        (2,1): RIGHT,  # right
    }

    def __init__(self):
        super().__init__((2, 0))

def main():
    inp = sys.stdin.read().strip().splitlines()

    s = 0
    for target in inp:
        q = [(0, "", Directional(), Directional(), Numeric(), "")]
        seen = set()
        while q:
            cost, code, d1, d2, n, hist = heapq.heappop(q)
            if len(code) > len(target):
                continue
            if code == target:
                print(target, cost, hist)
                s += int(target[:-1]) * cost
                break
            if (code, d1.pos, d2.pos, n.pos) in seen:
                continue
            seen.add((code, d1.pos, d2.pos, n.pos))

            def try_move(arm: Arm, d, s):
                if (new_d := arm.move(d)) is not None:
                    heapq.heappush(q, (cost + 1, code, new_d, copy(d2), copy(n), hist + s))

            # try to move
            try_move(d1, UP, "^")
            try_move(d1, DOWN, "v")
            try_move(d1, LEFT, "<")
            try_move(d1, RIGHT, ">")

            # if the first dir is looking at "A"
            if (d1_press := Directional.keys[d1.pos]) == PRESS:
                # if the next dir is also looking at "A"
                if (d2_press := Directional.keys[d2.pos]) == PRESS:
                    # press inner
                    if (code_press := Numeric.keys[n.pos]) == target[len(code)]:
                        heapq.heappush(q, (cost + 1, code + code_press, copy(d1), copy(d2), copy(n), hist + "A"))
                else:
                    # move n
                    if (new_n := n.move(d2_press)) is not None:
                        heapq.heappush(q, (cost + 1, code, copy(d1), copy(d2), new_n, hist + "A"))
            else:
                # move d2
                if (new_d2 := d2.move(d1_press)) is not None:
                    heapq.heappush(q, (cost + 1, code, copy(d1), new_d2, copy(n), hist + "A"))


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(s)

main()
