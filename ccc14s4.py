"""CCC '14 S4 - Tinted Glass Window
Canadian Computing Competition: 2014 Stage 1, Senior #4
You are laying N rectangular pieces of grey-tinted glass to make a stained glass window. Each piece of glass adds an integer value "tint-factor".
Where two pieces of glass overlap, the tint-factor is the sum of their tint-factors.
You know the desired position for each piece of glass and these pieces of glass are placed such that the sides of each rectangle are parallel to either the x-axis or the y-axis (that is, there are no "diagonal" pieces of glass).
You would like to know the total area of the finished stained glass window with a tint-factor of at least T.
"""

import ccc
params = ccc.load_std_input_file("ccc14s4.log", ccc.tc_int)
ccc.start_ccc()

glass_cnt = params[0][0]
threshold_tintf = params[1][0]

glasses = []    # ( (x1, y1), (x2, y2), tf)
for i in range(2, 2 + glass_cnt):
    rect = [(params[i][0], params[i][1]), (params[i][2], params[i][3])]
    glasses.append((rect, params[i][4]))

def in_rect(pt, rect):
    return pt[0] <= rect[1][0] and pt[0] >= rect[0][0] and \
    pt[1] <= rect[1][1] and pt[1] >= rect[0][1]

def size_rect(rect):
    return (rect[1][0] - rect[0][0]) * (rect[1][1] - rect[0][1])

def get_center(rect):
    return ((rect[0][0] + rect[1][0]) / 2, (rect[0][1] + rect[1][1]) / 2)

# split two rect to 3x3 rects
# then can scan every piece to check coverage or calc it.
def split_pieces(rects):
    all_pt = [pt for rect in rects for pt in rect]
    all_x, all_y = zip(*all_pt)
    all_x = list(set(all_x))
    all_y = list(set(all_y))
    all_x.sort()
    all_y.sort()
    return [[(all_x[ix], all_y[iy]), (all_x[ix+1], all_y[iy+1])] for ix in range(0, len(all_x)-1) for iy in range(0, len(all_y)-1)]

def get_tf(pt):
    tf = 0
    for g in glasses:
        if in_rect(pt, g[0]):
            tf += g[1]
    return tf

glass_rects = [glass[0] for glass in glasses]
piece_rects = split_pieces(glass_rects)

threshold_tintf_sum = 0
for piece in piece_rects:
    if (get_tf(get_center(piece)) >= threshold_tintf):
        threshold_tintf_sum += size_rect(piece)
print(threshold_tintf_sum)
ccc.end_ccc()