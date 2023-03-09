"""CCC '22 S4 - Good Triplets
Canadian Computing Competition: 2022 Stage 1, Senior #4
"""

# ************************ MUST REMOVE BEFORE SUMMIT ************************
def output(s):
    pass
from ccc import make_io
input, output = make_io(__file__)
# ***************************************************************************

points_cnt, circumference = tuple([int(p) for p in input().split(" ")])
half_cir = circumference / 2.0
points_list = [int(p) for p in input().split(" ")]
points_set = list(set(points_list))
points_dict = {k:[i for i, v in enumerate(points_list) if v == k] for k in points_set}

output(points_list)
output(points_set)
output(points_dict)

"""判断方法：
三角形的三个顶点分割圆的三段弧的长度中，任何一条弧长均不允许长过圆周的一半。
因为这个长弧对应的边，将其他两个边推到了原点对应直径的一侧，从而没有把圆心包含在内。
"""
def is_good_triplet(tri):
    min_pt = min(tri)
    points = sorted([n-min_pt for n in tri])
    return points[1] < half_cir and \
        points[2] - points[1] < half_cir and \
        circumference - points[2] < half_cir

all_triplets = []
for i in range(0, len(points_set)):
    for j in range(i+1, len(points_set)):
        for k in range(j+1, len(points_set)):
            tri = (points_set[i], points_set[j], points_set[k])
            if is_good_triplet(tri):
                all_triplets.append(tri)

expand_triplets = []
for p1, p2, p3 in all_triplets:
    for i in points_dict[p1]:
        for j in points_dict[p2]:
            for k in points_dict[p3]:
                expand_triplets.append((i+1, j+1, k+1))

output(all_triplets)
output(expand_triplets, True)
print(len(expand_triplets))