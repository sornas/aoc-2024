from collections import defaultdict
import sys

AND = 1
OR = 2
XOR = 3

def eval_gate(a1, gate, a2):
    if gate == AND:
        return a1 * a2 == 1
    elif gate == OR:
        return a1 + a2 >= 1
    elif gate == XOR:
        return a1 + a2 == 1

def main():
    inp = sys.stdin.read().strip()
    init, gates_ = inp.split("\n\n")

    wires = {}
    q = []
    for line in init.splitlines():
        wire, value = line.split(": ")
        wires[wire] = int(value)
        q.append(wire)


    gates = []
    outs = defaultdict(list)
    for i, line in enumerate(gates_.splitlines()):
        a1, gate, a2, _arrow, b = line.split()
        if gate == "AND":
            gate = AND
        elif gate == "OR":
            gate = OR
        elif gate == "XOR":
            gate = XOR
        gates.append((a1, gate, a2, b))
        outs[a1].append(i)
        outs[a2].append(i)

    # replace wires with their values
    while q:
        wire = q.pop()
        value = wires[wire]
        for gate_idx in outs[wire]:
            a1, gate, a2, b = gates[gate_idx]
            if wire == a1:
                a1 = value
            if wire == a2:
                a2 = value
            if type(a1) == int and type(a2) == int:
                # set output
                val = int(eval_gate(a1, gate, a2))
                wires[b] = val
                q.append(b)
            gates[gate_idx] = (a1, gate, a2, b)

    bs = [v for k,v in reversed(sorted(wires.items())) if k.startswith("z")]

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(int("".join(map(str, bs)), 2))




main()
