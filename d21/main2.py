from functools import cache
import sys

numpad = {
    (0,0): "7",
    (0,1): "4",
    (0,2): "1",
    (0,3): None,
    (1,0): "8",
    (1,1): "5",
    (1,2): "2",
    (1,3): "0",
    (2,0): "9",
    (2,1): "6",
    (2,2): "3",
    (2,3): "A",
}
numpad_inv = {v:k for k, v in numpad.items()}

dirpad = {
    (0,0): None,
    (0,1): "<",
    (1,0): "^",
    (1,1): "v",
    (2,0): "A",
    (2,1): ">",
}
dirpad_inv = {v:k for k, v in dirpad.items()}

def _move(x1, y1, x2, y2, invalid, dirpads):
    dx = x2 - x1
    dy = y2 - y1
    dirx = "-" if dx == 0 else "<" if dx < 0 else ">"
    diry = "-" if dy == 0 else "^" if dy < 0 else "v"

    x_first_valid = (x2, y1) != invalid
    y_first_valid = (x1, y2) != invalid

    def move_seq(seq):
        return sum(move_dir(a, b, dirpads - 1) for a, b in zip("A" + seq, seq))

    # lazy evaluation

    # x first
    def xy():
        return move_seq(dirx * abs(dx) + diry * abs(dy) + "A")

    # y first
    def yx():
        return move_seq(diry * abs(dy) + dirx * abs(dx) + "A")

    if not x_first_valid:
        return yx()
    elif not y_first_valid:
        return xy()
    else:
        return min(xy(), yx())

@cache
def move_dir(fr, to, dirpads):
    if dirpads == 0:
        return 1
    return _move(*dirpad_inv[fr], *dirpad_inv[to], dirpad_inv[None], dirpads)

@cache
def move_num(fr, to, dirpads):
    return _move(*numpad_inv[fr], *numpad_inv[to], numpad_inv[None], dirpads)


def main():
    inp = sys.stdin.read().strip()
    print(sum(int(code[:-1]) * sum(move_num(a, b, 26) for a, b in zip("A" + code, code)) for code in inp.splitlines()))

main()
