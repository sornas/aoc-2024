import sys

def prefix_ok(prog, prefix):
    if len(prefix) > 2:
        return prefix[:-1] and prog[:len(prefix)-1] == prefix
    return prefix and prog[:len(prefix)] == prefix


def print_inst(inst, operand):
    i = None
    o = None

    combo = True
    inv_operands = False
    op = None
    if inst == 0:
        inst = "adv"
        i = "A"
        o = "A"
        op = ">"
    if inst == 1:
        inst = "bxl"
        combo = False
        i = "B"
        o = "B"
        op = "^"
    if inst == 2:
        inst = "bst"
        o = "B"
        i = "111"
        op = "&"
        inv_operands = True
    if inst == 3:
        inst = "jnz"
        combo = False
    if inst == 4:
        inst = "bxc"
        i = "B"
        o = "B"
        op = "^"
        operand = 6
    if inst == 5:
        inst = "out"
    if inst == 6:
        inst = "bdv"
        i = "A"
        o = "B"
        op = ">"
    if inst == 7:
        inst = "cdv"
        i = "A"
        o = "C"
        op = ">"

    if combo:
        if operand < 4: pass
        if operand == 4: operand = "A"
        if operand == 5: operand = "B"
        if operand == 6: operand = "C"

    if type(operand) is int:
        operand = f"{operand:03b}"
    if op:
        if inv_operands:
            return f"{inst}: {o} <- {operand} {op} {i}"
        else:
            return f"{inst}: {o} <- {i} {op} {operand}"
    else:
        return f"{inst} {operand}\t\t"


def run_until_halt(program, ra, rb, rc):
    pc = 0
    out = []
    while pc < len(program):
        inst = program[pc]
        operand = program[pc+1]
        pc += 2

        if operand < 4:
            combo = operand
        elif operand == 4:
            combo = ra
        elif operand == 5:
            combo = rb
        elif operand == 6:
            combo = rc
        else:
            assert False

        if inst == 0:
            ra = ra // (2 ** combo)
        elif inst == 1:
            rb = rb ^ operand
        elif inst == 2:
            rb = combo % 8
        elif inst == 3:
            if ra != 0:
                pc = operand
        elif inst == 4:
            rb = rb ^ rc
        elif inst == 5:
            out.append(combo % 8)
        elif inst == 6:
            rb = ra // (2 ** combo)
        elif inst == 7:
            rc = ra // (2 ** combo)

        # print(print_inst(inst, operand), f"\t({ra}, {ra:03b})\t({rb}, {rb:03b})\t({rc}, {rc:03b})")

    return out

def next_out(a: int) -> tuple[int, int]:
    return a >> 3, (((a & 0b111) ^ 0b101) ^ (a >> ((a & 0b111) ^ 0b001))) % 8

def all_out(a: int) -> list[int]:
    r = []
    while a:
        a, o = next_out(a)
        r.append(o)
    return r

def to_num(ts: list[int]) -> int:
    return sum(t << (i * 3) for i, t in enumerate(ts))

def main():
    with open("input") as f:
        inp = f.read().strip().splitlines()

    ra = int(inp[0].split(": ")[1])
    rb = int(inp[1].split(": ")[1])
    rc = int(inp[2].split(": ")[1])

    program = list(map(int, inp[4].split(": ")[1].split(",")))

    max_depend = 2**10 - 1

    q = [(0, 0)]
    seen = set()

    n = float("Inf")
    while q:
        x, l = q.pop()
        if (x, l) in seen:
            continue
        seen.add((x, l))
        for a in range(1, max_depend):
            a1 = a
            a = (a << (3 * l)) + x
            o = all_out(a)
            # print(x, l, a, a & (2**(3*l)-1), o, o[:l], program[:l])
            if o == program:
                n = min(n, a)
            if len(o) > len(program):
                continue
            if o[:l+1] == program[:l+1]:
                q.append((a & (2**(3*(l+1))-1), l + 1))

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(n)

    # ra = int(sys.argv[1])
    # print(run_until_halt(program, ra, rb, rc))
    # print(program)


main()
