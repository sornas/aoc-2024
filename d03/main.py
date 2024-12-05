import re
import sys


def main():
    r = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    r_enable = re.compile(r"do(n't)?\(\)")
    s = 0

    inp = sys.stdin.read()
    def enabled_at(p):
        enabled = True
        for m in r_enable.finditer(inp[:p]):
            enabled = m.group(1) is None
        return enabled

    for m in r.finditer(inp):
        if enabled_at(m.start(0)):
            s += int(m.group(1)) * int(m.group(2))
    print(2, s)

main()

