from collections import deque, defaultdict
import sys

def main():
    inp = sys.stdin.read().strip()

    best_change = None
    best_banana = 0

    changes = defaultdict(lambda: 0)
    inp = inp.splitlines()
    for i, n in enumerate(inp):
        n = int(n)
        dns = deque()
        seen = set()
        changes_and_price = dict()
        for _ in range(2000):
            n1 = n
            n = (n ^ (n * 64)) % 16777216
            n = (n ^ (n // 32)) % 16777216
            n = (n ^ (n * 2048)) % 16777216
            dn = (n % 10) - (n1 % 10)
            dns.append(dn)
            if len(dns) == 5:
                dns.popleft()
            if len(dns) == 4:
                change = tuple(dns)
                banana = n % 10
                if change in seen:
                    continue
                seen.add(change)
                changes[change] += banana
                if changes[change] > best_banana:
                    best_banana = changes[change]
                    best_change = change


    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(2, best_banana, best_change)
main()
