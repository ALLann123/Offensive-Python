#!/usr/bin/python3

def unshuffle(s):
    chars = list(s)
    for i in range(0, len(chars) - 2, 3):
        chars[i], chars[i + 1], chars[i + 2] = chars[i + 1], chars[i + 2], chars[i]
    return ''.join(chars)

# Given shuffled string
shuffled_flag = "3d}122d44gv_f_ldetbmlrc8{FsCoTipc"

# Step 1: Reverse the string
reversed_flag = shuffled_flag[::-1]

# Step 2: Undo the shuffle
original_flag = unshuffle(reversed_flag)

print(original_flag)
