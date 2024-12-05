import sys


def main():
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    inp = sys.stdin.read().strip()
    rules, updates = inp.split("\n\n")

    print(repr(rules), repr(updates))

    rules_order = {}
    rules_order_inv = {}
    for rule in rules.split("\n"):
        a, b = map(int, rule.split("|"))
        if a not in rules_order:
            rules_order[a] = []
        rules_order[a].append(b)
        if b not in rules_order_inv:
            rules_order_inv[b] = []
        rules_order_inv[b].append(a)

    def valid_order(a, b):
        if a in rules_order and b in rules_order[a]:
            return True
        elif b not in rules_order_inv or a not in rules_order_inv[b]:
            return False
        return True

    s = 0
    wrong = []
    for update in updates.split("\n"):
        update = list(map(int, update.split(",")))
        valid = True
        for i, a in enumerate(update):
            for b in update[i+1:]:
                if a == b: continue
                if not valid_order(a, b):
                    valid = False
        if valid:
            s += update[len(update)//2]
        else:
            wrong.append(update)

    s2 = 0
    for update in wrong:
        correct = []
        left = set(update)
        while left:
            added_anything = False
            for a in left:
                valid_to_add = True
                for b in left:
                    if not valid_order(a,b):
                        valid_to_add = False
                        break
                if valid_to_add:
                    correct.append(a)
                    left.remove(a)
                    added_anything = True
                    break
            assert added_anything
        print(wrong, correct)

    print(1, s)
    print(2, s2)



main()
