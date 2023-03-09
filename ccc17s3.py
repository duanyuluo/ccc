"""CCC '17 S3 - Nailed It!
Canadian Computing Competition: 2017 Stage 1, Junior #5, Senior #3
"""

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc2")
# ***************************************************************************

wood_cnt = int(input())
wood_lens = [int(p) for p in input().split(" ")]

boards_lens = dict()
for i in range(0, wood_cnt-1):
    for j in range(i+1, wood_cnt):
        l = wood_lens[i] + wood_lens[j]
        if not l in boards_lens:
            boards_lens[l] = []
        boards_lens[l].append((i, j))

max_fence_len = max([len(v) for (k, v) in boards_lens.items()])
fences = {k:v for (k, v) in boards_lens.items() if len(v) == max_fence_len}

output(boards_lens)
output(fences)
print("%d %d" % (max_fence_len, len(fences)))