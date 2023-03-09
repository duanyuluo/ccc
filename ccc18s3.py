"""CCC '18 S3 - RoboThieves
Canadian Computing Competition: 2018 Stage 1, Senior #3
"""
def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc2")
# ***************************************************************************

row_cnt, col_cnt = tuple([int(p) for p in input().split(" ")])
map = [[c for c in list(input())] for i in range(0, row_cnt)]

def output_map(_map, row = -1, col = -1):
    fmt = lambda i: (i == col and "<[%2d]>" or "%2d") % i
    output("   " + " ".join([fmt(i) for i in range(0, col_cnt)]))
    for idx, r in enumerate(_map):
        cell_fmt = lambda i, c: ((i == col and idx == row) and "<{%2s}>" or "%2s") % c
        output((idx == row and "<[%2d]> " or "%2d ") % idx + " ".join([cell_fmt(i, c) for (i, c) in enumerate(r)]))

foot_marks = [[0 for c in range(0, col_cnt)] for i in range(0, row_cnt)]

def walk_step(row, col, steps_cnt):
    if foot_marks[row][col] and map[row][col] in "SWCUDLR":
        return
    
    foot_marks[row][col] = 1
    tip = ""
    if type(map[row][col]) == int:
        if map[row][col] > 0 and map[row][col] > steps_cnt:
            map[row][col] = steps_cnt
            tip = "LESS STEPS"
        else:
            tip = "DEAD"
    elif map[row][col] in ".S":
        if map[row][col] == ".":
            map[row][col] = steps_cnt
            tip = "WALK AT"
        else:
            tip = "START"
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for off in dirs:
            output("<[STEP #%d]>[%d, %d] : %s" % (steps_cnt, row + off[0], col + off[1], "START NEXT..."))
            walk_step(row + off[0], col + off[1], steps_cnt+1)
    elif map[row][col] == "W":
        tip = "TOUCH WALL"
    elif map[row][col] == "C":
        map[row][col] = -1
        tip = "DEAD"
    elif map[row][col] in "UDLR":
        conveyor_dir = {"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)}
        off = conveyor_dir[map[row][col]]
        output("<[STEP #%d]>[%d, %d] : %s" % (steps_cnt, row + off[0], col + off[1], "START CONVEYOR..."))
        walk_step(row + off[0], col + off[1], steps_cnt)
        tip = "CONVEYOR TO"
    output("STEP #%d[%d, %d] : %s" % (steps_cnt, row, col, tip), highlight=True)
    output_map(map, row, col)

def make_camera_scope(row, col, off):
    global map
    if map[row][col] == ".":
        map[row][col] = -1
    elif map[row][col] in "WCS":
        return
    make_camera_scope(row + off[0], col + off[1], off)

def scan_camera_scope(row, col):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for off in dirs:
        make_camera_scope(row + off[0], col + off[1], off)

start_cell = (0, 0)
for i in range(0, row_cnt):
    for j in range(0, col_cnt):
        if map[i][j] == "S":
            start_cell = (i, j)
            foot_marks[i][j] == 1
        elif map[i][j] == "C":
            output("<[STEP #%d]>[%d, %d] : %s" % (0, i, j, "SCAN CAMERA"), highlight=True)
            scan_camera_scope(i, j)
            output_map(map, i, j)

output("START...")
output_map(map, start_cell[0], start_cell[1])
walk_step(start_cell[0], start_cell[1], 0)

for i in range(0, row_cnt):
    for j in range(0, col_cnt):
        if type(map[i][j]) == int:
            print(map[i][j])