# CCC '23 S3 - Palindromic Poster

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc1")
# ***************************************************************************

row_size, column_size, row_pal_cnt, col_pal_cnt = 5, 5, 2, 5
need_trans = False
if row_pal_cnt < col_pal_cnt:
    row_pal_cnt, col_pal_cnt = col_pal_cnt, row_pal_cnt
    need_trans = True
poster = []

for r in range(0, row_size):
    poster.append([])
    for c in range(0, column_size):
        poster[-1].append("a")

cur_char = "a"

def next_char():
    global cur_char
    cur_char = chr(ord(cur_char) + 1)
    return cur_char

for r in range(row_pal_cnt, row_size):
    poster[r][-1] = next_char()

if row_pal_cnt < row_size:
    for c in range(col_pal_cnt, column_size):
        poster[-1][c] = next_char()
else:
    unpal_cnt = column_size - col_pal_cnt
    unpan_cols = []
    if unpal_cnt % 2 == 1:
        if column_size % 2 == 0:
            print("IMPOSSIBLE")
        unpan_cols.append(column_size // 2)
        unpal_cnt -= 1
    for i in range(0, unpal_cnt // 2):
        unpan_cols.append(i)
        unpan_cols.append(-(i+1))
    ch = next_char()
    for p in unpan_cols:
        poster[-1][p] = ch

if need_trans:
    for i in range(0, row_size):
        for j in range(i, column_size):
            poster[i][j], poster[j][i] = poster[j][i], poster[i][j]

output("\n".join([str(c) for c in poster]))
