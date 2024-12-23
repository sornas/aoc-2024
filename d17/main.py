import sys
from collections import deque

def main():
    inp = sys.stdin.read().strip().splitlines()

    ra = int(inp[0].split(": ")[1])
    rb = int(inp[1].split(": ")[1])
    rc = int(inp[2].split(": ")[1])

    program = list(map(int, inp[4].split(": ")[1].split(",")))

    print(ra,rb,rc, program)

    pc = 0

    out = []
    while pc < len(program):
        inst = program[pc]
        operand = program[pc+1]
        pc += 2
        print(inst, operand, ra, rb, rc)

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

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(",".join(map(str, out)))

main()
