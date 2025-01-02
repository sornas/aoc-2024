import sys

def safe(ns):
    if ns[0] == ns[1]:
        return False
    incr = ns[0] < ns[1]
    if incr:
        return all(1 <= b-a <= 3 for a,b in zip(ns[:-1], ns[1:]))
    else:
        return all(1 <= a-b <= 3 for a,b in zip(ns[:-1], ns[1:]))

def damp_safe(ns):
    if safe(ns):
        return True
    for i in range(len(ns)):
        nn = ns.copy()
        del(nn[i])
        if safe(nn):
            return True
    return False


def main():
    s1 = s2 = 0
    for line in sys.stdin.readlines():
        nums = list(map(int, line.split()))
        if safe(nums):
            s1 += 1
        if damp_safe(nums):
            s2 += 1

    print(1, s1)
    print(2, s2)

main()
