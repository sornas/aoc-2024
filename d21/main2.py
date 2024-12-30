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

# @cache
def move_dir(fr, to, pad):
    if pad == 0:
        return 1

    x1, y1 = dirpad_inv[fr]
    x2, y2 = dirpad_inv[to]
    dx = x2 - x1
    dy = y2 - y1
    dirx = "<" if dx < 0 else ">"
    diry = "^" if dy < 0 else "v"

    x_first_valid = dirpad[(x2, y1)] is not None
    y_first_valid = dirpad[(x1, y2)] is not None

    def xy():
        seq = dirx * dx + diry * dy + "A"
        return sum(move_dir(a, b, pad - 1) for a, b in zip("A" + seq, seq))

    def yx():
        seq = dirx * dx + diry * dy + "A"
        return sum(move_dir(a, b, pad - 1) for a, b in zip("A" + seq, seq))

    if not x_first_valid:
        return yx()
    elif not y_first_valid:
        return xy()
    else:
        tx = xy()
        ty = yx()
        return min(tx, ty)

# TODO: same move_num + move_dir?
# TODO: return (presses, string) for debug

# @cache
def move_num(fr, to, pad):
    print("num", fr, to)
    x1, y1 = numpad_inv[fr]
    x2, y2 = numpad_inv[to]
    dx = x2 - x1
    dy = y2 - y1
    dirx = "<" if dx < 0 else ">"
    diry = "^" if dy < 0 else "v"

    x_first_valid = numpad[(x2, y1)] is not None
    y_first_valid = numpad[(x1, y2)] is not None

    def xy():
        seq = dirx * dx + diry * dy + "A"
        return sum(move_dir(a, b, pad) for a, b in zip("A" + seq, seq))

    def yx():
        seq = dirx * dx + diry * dy + "A"
        return sum(move_dir(a, b, pad) for a, b in zip("A" + seq, seq))

    if not x_first_valid:
        return yx()
    elif not y_first_valid:
        return xy()
    else:
        tx = xy()
        ty = yx()
        return min(tx, ty)


def main():
    inp = sys.stdin.read().strip()

    t = 0
    for code in inp.splitlines():
        print(code)
        s = 0
        for a, b in zip("A" + code, code):
            s += move_num(a, b, 2) + 1
        t += s
    print(t)

main()
