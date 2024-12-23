import sys

def main():
    inp = sys.stdin.read().strip()

    def mix(secret, n):
        return secret ^ n
    def prune(secret):
        return secret % 16777216

    s = 0
    for n in inp.splitlines():
        n = int(n)
        n1 = n
        for _ in range(2000):
            n = prune(mix(n, n * 64))
            n = prune(mix(n, n // 32))
            n = prune(mix(n, n * 2048))
        s += n

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(1, s)

main()
