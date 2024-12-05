import sys

def main():
    ll = []
    rr = []
    for line in sys.stdin.readlines():
        ll.append(int(line.split()[0]))
        rr.append(int(line.split()[1]))
    ll.sort()
    rr.sort()
    s = sum(abs(a-b) for a,b in zip(ll,rr))
    print(1, s)

    s = 0
    for n in ll:
        s += rr.count(n) * n
    print(2,s)


main()
