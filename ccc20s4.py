"""CCC '20 S4 - Swapping Seats
Canadian Computing Competition: 2020 Stage 1, Senior #4
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

seats = list(input())
def get_seats(fr, cnt):
    fr = fr % len(seats)
    return (seats+seats[:cnt])[fr:fr+cnt]

groups = {"A":[-1, -1, 0], "B":[-1, -1, 0], "C":[-1, -1, 0]}
for c in "ABC":
    groups[c][2] = seats.count(c)

def search_group_pos(group_name):
    global groups
    if groups[group_name][1] == groups[group_name][2]:
        return
    groups[group_name][0] = -1
    groups[group_name][1] = -1
    for i in range(0, len(seats)):
        cnt = get_seats(i, groups[group_name][2]).count(group_name)
        if cnt == groups[group_name][1]:
            groups[group_name][0] = -1
        elif cnt > groups[group_name][1]:
            groups[group_name][0] = i
            groups[group_name][1] = cnt

def in_group(i, group_name):
    if groups[group_name][0] + groups[group_name][1] > len(seats):
        return i >= groups[group_name][0] or i < (groups[group_name][0] + groups[group_name][2]) % len(seats)
    else:
        return i >= groups[group_name][0] and i < groups[group_name][0] + groups[group_name][2]
    
def swap_pair(group_name):
    global seats
    inner_pos, outter_pos = -1, -1
    for i in range(0, len(seats)):
        if in_group(i, group_name):
            if seats[i] != group_name:
                inner_pos = i
        else:
            if seats[i] == group_name:
                outter_pos = i
        if inner_pos > 0 and outter_pos > 0:
            break
    seats[inner_pos], seats[outter_pos] = seats[outter_pos], seats[inner_pos]


swap_idx = 0
[search_group_pos(c) for c in "ABC"]
print(seats)
print(groups)

while True:
    if all([groups[c][1] == groups[c][2] for c in "ABC"]):
        break

    group_name = ""
    for gn in "ABC":
        if groups[gn][1] == groups[gn][2] or groups[gn][0] < 0:
            continue
        group_name = gn
        break

    swap_pair(group_name)
    swap_idx += 1

    [search_group_pos(c) for c in "ABC"]
    print(seats)
    print(groups)

print(swap_idx)