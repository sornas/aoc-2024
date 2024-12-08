import itertools
import sys

def main():
    inp = sys.stdin.readlines()
    s = 0
    for i, line in enumerate(inp):
        print(i, len(inp))
        ans, nums = line.split(": ")
        ans = int(ans)
        nums = list(map(int, nums.split()))
        num_ops = len(nums)-1
        for ops in itertools.product(["+", "*", "||"], repeat=num_ops):
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
            if rhs == ans:
                s += ans
                break

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(1, None)
    print(2, s)

main()
