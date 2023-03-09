"""CCC '19 S5 - Triangle: The Data Structure
Canadian Computing Competition: 2019 Stage 1, Senior #5
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

triangle_size, sub_size = tuple([int(p) for p in input().split(" ")])
triangles = []
for i in range(triangle_size):
    triangles.append([int(p) for p in input().split(" ")])

def get_sub(row_start, col_start, tri_size):
    sub_triangle = []
    for row_idx in range(0, tri_size):
        sub_triangle.extend(triangles[row_start + row_idx][col_start : col_start + row_idx + 1])
    return sub_triangle

max_sub_triangles = []
for r in range(0, triangle_size - sub_size + 1):
    for c in range(0, r + 1):
        max_sub_triangles.append(max(get_sub(r, c, sub_size)))

print(max_sub_triangles)
print(sum(max_sub_triangles))