import re


def main():
    with open("input") as f:
        gates = f.read().strip().split("\n\n")[1].splitlines()

    map_ = {}
    swap = {
        "z05": "jst",
        "jst": "z05",

        "z30": "gwc",
        "gwc": "z30",

        "z15": "dnt",
        "dnt": "z15",

        "mcm": "gdf",
        "gdf": "mcm",
    }

    def subs(s):
        return map_.get(s) or s

    def subswap(s):
        return swap.get(s) or subs(s)

    r = re.compile(r"[xy](\d\d) (AND|OR|XOR) [xy](\d\d) -> (...)")

    for line in gates:
        a1, op, a2, _arrow, b = line.split()
        if m := r.match(line):
            if b.startswith("z"): continue
            d1, op, d2, b = m.groups()
            assert d1 == d2
            b2 = f"{d1}{op}"
            map_[b] = b2
            b = b2

    inter = []
    zs = []
    for line in gates:
        a1, op, a2, _arrow, b = line.split()
        a1, a2 = list(sorted((subs(a1), subs(a2))))
        b = subswap(b)
        if b.startswith("z"):
            l = zs
        else:
            l = inter
        l.append((a1, op, a2, "->", b))
    inter.sort(key=lambda x: x[1])
    inter.sort(key=lambda x: x[0])
    zs.sort(key=lambda x: x[-1])

    with open("input2", mode="w") as f:
        for line in inter + zs:
            f.write(" ".join(line))
            f.write("\n")

main()
