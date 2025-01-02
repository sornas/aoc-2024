import re
import sys


def main():
    r = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    r_enable = re.compile(r"do(n't)?\(\)")
    s1 = 0
    s2 = 0

    inp = sys.stdin.read()
    def enabled_at(p):
        enabled = True
        for m in r_enable.finditer(inp[:p]):
            enabled = m.group(1) is None
        return enabled

    for m in r.finditer(inp):
        s1 += int(m.group(1)) * int(m.group(2))
        if enabled_at(m.start(0)):
            s2 += int(m.group(1)) * int(m.group(2))
    print(1, s1)
    print(2, s2)

main()

