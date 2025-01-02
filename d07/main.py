import itertools
import sys

def solve(inp, part):
    s = 0
    for i, line in enumerate(inp):
        print(f"progress (part {part}): {i}/{len(inp)}")
        ans, nums = line.split(": ")
        ans = int(ans)
        nums = list(map(int, nums.split()))
        num_ops = len(nums)-1
        for ops in itertools.product(["+", "*"] if part == 1 else ["+", "*", "||"], repeat=num_ops):
            # initial
            if ops[0] == "+":
                rhs = nums[0] + nums[1]
            elif ops[0] == "*":
                rhs = nums[0] * nums[1]
            elif ops[0] == "||":
                rhs = int(str(nums[0]) + str(nums[1]))
            # accumulate
            for num, op in zip(nums[2:], ops[1:]):
                if op == "+":
                    rhs += num
                elif op == "*":
                    rhs *= num
                elif op == "||":
                    rhs = int(str(rhs) + str(num))
                else:
                    assert False, f"unknown op: '{op}'"
            if rhs == ans:
                s += ans
                break
    return s

def main():
    inp = sys.stdin.readlines()

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    s1 = solve(inp, 1)
    s2 = solve(inp, 2)
    print(1, s1)
    print(2, s2)

main()
