# CCC '23 S4 - Minimum Cost Roads

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc1")
# ***************************************************************************

section_cnt, road_cnt = tuple([int(p) for p in input().split(" ")])
roads = [tuple([int(p) for p in input().split(" ")]) for ln in range(0, road_cnt)]

output(roads)

sections = {i:[] for i in range(1, section_cnt+1)}
for frm, to, length, cost in roads:
    sections[frm].append((to, length, cost))
    sections[to].append((frm, length, cost))

output(sections)

def get_shortest_path(frm, target, top_len):
    shortest_lenght = 0
    shortest_path = []
    for to, length, cost in sections[frm]:
        if length > top_len:
            continue
        if to == target:
            if shortest_lenght == 0 or length < shortest_lenght:
                shortest_lenght = length
                shortest_path = [frm, to]
        else:
            sub_path, sub_length = get_shortest_path(to, target, top_len - length)
            if len(sub_path) == 0:
                continue            
            if shortest_lenght < 0 or sub_length + length <= shortest_lenght:
                shortest_lenght = sub_length + length
                shortest_path = [frm, ] + sub_path
    return shortest_path, shortest_lenght

selected_roads = []
for frm, to, length, cost in roads:
    shortest_path, shortest_lenght = get_shortest_path(frm, to, length)
    selected = length == shortest_lenght and len(shortest_path) == 2
    if selected:
        selected_roads.append((frm, to, length, cost))
    output("(%2d <-> %2d) %2d meters, %d dollars" % (frm, to, length, cost), highlight=selected)

print(sum([road[3] for road in selected_roads]))