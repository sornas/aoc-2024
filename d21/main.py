import functools
import sys

def main():
    inp = sys.stdin.read().strip().splitlines()

    numeric_pos_to_num = {
        (0,0): 7,
        (1,0): 8,
        (2,0): 9,
        (0,1): 4,
        (1,1): 5,
        (2,1): 6,
        (0,2): 1,
        (1,2): 2,
        (2,2): 3,
        (1,3): 0,
        (2,3): 10 # A
    }
    numeric_num_to_pos = {kv[1]:kv[0] for kv in numeric_pos_to_num.items()}

    dir_pos_to_dir = {
        (1,0): 1,  # up
        (2,0): 10, # A
        (0,1): 2,  # left
        (1,1): 3,  # down
        (2,1): 4,  # right
    }

    @functools.cache
    def moves_to_input(num_cur, num_target, dir1_cur, dir1_target):
        nx, ny = numeric
        tx, ty = numeric_num_to_pos[target]
        return abs(nx-tx) + abs(ny-ty) + 1

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")

    print(moves_to_input(numeric_num_to_pos[10], 5))

main()
