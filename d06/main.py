from multiprocessing import Process, Queue
import sys

def main():
    inp = sys.stdin.readlines()

    def add(x,y,dx,dy):
        return (x + dx, y + dy)

    map = {}
    start_pos = None
    for y, line in enumerate(inp):
        for x, c in enumerate(line.strip()):
            if c == "^":
                start_pos = (x,y)
            map[(x, y)] = c if c != "^" else "."

    w = len(inp[0])-1
    h = len(inp)
    def in_range(x,y):
        return 0 <= x < w and 0 <= y < h

    pos = start_pos
    look = (0, -1)
    visited = set([pos])
    while True:
        walk_p = add(*pos, *look)
        if not in_range(*walk_p):
            break
        if map[walk_p] == ".":
            pos = walk_p
            visited.add(pos)
        else:
            while map[add(*pos, *look)] == "#":
                look = (-look[1], look[0])

    q = Queue()

    def do_line(y):
        for x in range(w):
            pos = start_pos
            look = (0, -1)
            visited = set([pos])
            seen_pos_look = set()
            while True:
                if (pos, look) in seen_pos_look:
                    q.put(1)
                    break
                seen_pos_look.add((pos, look))
                walk_p = add(*pos, *look)
                if not in_range(*walk_p):
                    break
                if map[walk_p] == "." and walk_p != (x, y):
                    pos = walk_p
                    visited.add(pos)
                else:
                    while map[walk_p] == "#" or walk_p == (x,y):
                        look = (-look[1], look[0])
                        walk_p = add(*pos, *look)

    s = 0
    ps = [Process(target=do_line, args=[y]) for y in range(h)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    while not q.empty():
        s += q.get()



    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(1, len(visited))
    print(2, s)



main()
