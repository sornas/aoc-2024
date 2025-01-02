def main(inp):

    filemap = []
    i = 0
    n = 0
    while True:
        for _ in range(int(inp[i])):
            filemap += [str(n)]
        i += 1
        n += 1
        if i == len(inp): break
        for _ in range(int(inp[i])):
            filemap += ["."]
        i += 1
        if i == len(inp): break
    # print(filemap)
    filemap2 = filemap.copy()


    i = len(filemap) - 1
    j = 0

    def visualize():
        return
        print("".join(filemap))
        print(" " * j + "j" + " " * (i - j - 1) + "i")
        input()

    visualize()
    while i >= 0 and i != j + 1:
        if filemap[i] != ".":
            while True:
                if i == j + 1: break
                if filemap[j] == ".":
                    filemap[i], filemap[j] = filemap[j], filemap[i]
                    visualize()
                    break
                else:
                    j += 1
                    visualize()
        if i == j + 1: break
        i -= 1
        visualize()

    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(1, sum(a * int(b) for a,b in enumerate(filemap) if b != "."))

def main2(inp):

    files = {} # {index: (start, len)}
    holes = [] # (start, len)
    i = 0
    p = 0
    n = 0
    while True:
        files[n] = (p, int(inp[i]))
        p += int(inp[i])
        i += 1 # next char in input
        n += 1 # next file
        if i == len(inp): break
        holes.append((p, int(inp[i])))
        p += int(inp[i])
        i += 1
        if i == len(inp): break
    files = [[k, v] for k, v in sorted(files.items())]
    # print(files, holes)


    filemap_len = max(files[-1][1][0] + files[-1][1][1], holes[-1][0] + holes[-1][1])
    def visualize():
        return
        fmap = ["."] * filemap_len
        for n, (start, len) in files:
            for i in range(start, start+len):
                fmap[i] = str(n)
        print("".join(fmap))


    visualize()
    for i in range(len(files))[::-1]:
        #print(files, holes)
        n, (file_start, file_len) = files[i]
        #print("file", n, file_start, file_len)
        for j in range(len(holes)):
            hole_start, hole_len = holes[j]
            #print("hole", j, hole_start, hole_len)
            if hole_len >= file_len and hole_start < file_start:
                # move to start of hole
                files[i][1] = (hole_start, file_len)

                # make the hole we moved into smaller
                if hole_len == file_len:
                    holes.pop(j)
                else:
                    holes[j] = (hole_start + file_len, hole_len - file_len)

                # create a hole where the file was
                holes.append((file_start, file_len))
                holes.sort()

                # merge holes
                j = 0
                while j < len(holes)-1:
                    # if start+len of this is equal to start of next, remove the next and expand the current
                    if holes[j][0] + holes[j][1] == holes[j+1][0]:
                        holes[j] = (holes[j][0], holes[j][1] + holes[j+1][1])
                        holes.pop(j+1)
                    else:
                        j += 1

                # done with this file
                visualize()
                break

    fmap = ["."] * filemap_len
    for n, (start, len_) in files:
        for i in range(start, start+len_):
            fmap[i] = str(n)

    print(2, sum(a * int(b) for a,b in enumerate(fmap) if b != "."))

inp = input()
main(inp)
main2(inp)
