import sys
import networkx as nx

def main():
    inp = sys.stdin.read().strip()

    g = nx.Graph()
    for line in inp.splitlines():
        g.add_edge(*line.split("-"))

    s = 0
    ccs = list(nx.algorithms.clique.enumerate_all_cliques(g))
    for clq in ccs:
        if len(clq) < 3:
            continue
        if len(clq) > 3:
            break
        assert len(clq) == 3
        if any(c.startswith("t") for c in clq):
               s += 1

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(1, s)
    print(2, ",".join(sorted(ccs[-1])))

main()
