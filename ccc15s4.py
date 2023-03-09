"""CCC '15 S4 - Convex Hull
Canadian Computing Competition: 2015 Stage 1, Senior #4
You are travelling on a ship in an archipelago. The ship has a convex hull which is K centimetres thick. The archipelago has N islands, numbered from 1 to N. There are M sea routes amongst them, where the ith route runs directly between two different islands a; and b;; (1 < a;; b; < M, takes tr minutes to travel along in either direction, and has rocks that wear down the ship's hull by hi centimetres. There may be multiple routes running between a pair of islands.
You would like to travel from island A to a different island B (1 < A, B < I) along a sequence of sea routes, such that your ship's hull remains intact
- in other words, such that the sum of the routes' h; values is strictly less than K.
Additionally, you are in a hurry, so you would like to minimize the amount of time necessary to reach island B from island A. It may not be possible to reach island B from island A, however, either due to insufficient sea routes or the having the ship's hull wear out.
Input Specification
The first line of input contains three integers K, N and M (1 < K < 200,2 < N < 2000, 1 < M < 10000), each separated by one space.
The next M lines each contain 4 integers a;, b;, t; and h; (1 S a;, b; S N, I St; < 105, 0 < hi < 200), each separated by one space. The ith line in this set of M lines describes the ith sea route (which runs from island a; to island b;, takes t; minutes and wears down the ship's hull by h; centimetres).
Notice that a; + b; (that is, the ends of a sea route are distinct islands).
The last line of input contains two integers A and B (1 < A, B < N; A + B), the islands between which we want to travel.
For 20% of marks for this question, K = 1 and I S 200. For another 20% of the marks for this problem, K = 1 and I < 2000.
Output Specification
Output a single integer: the integer representing the minimal time required to travel from A to B without wearing out the ship's hull, or -1 to indicate that there is no way to travel from A to B without wearing out the ship's hull.
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

hull_thick, islands_cnt, sea_route_cnt = tuple([int(p) for p in input().split(" ")])

# key:island1, value: [(island2, travel_time, wears down the ship's hull)]
sea_routes = {}
for i in range(0, sea_route_cnt):
    i1, i2, tm, h = tuple([int(p) for p in input().split(" ")])
    if not i1 in sea_routes:
        sea_routes[i1] = [(i2, tm, h)]
    else:
        sea_routes[i1].append((i2, tm, h))
    if not i2 in sea_routes:
        sea_routes[i2] = [(i1, tm, h)]
    else:
        sea_routes[i2].append((i1, tm, h))

island_from, island_to = tuple([int(p) for p in input().split(" ")])

def schedule_time(from_island, target_island, rest_hull, stoped_islands):
    global sea_routes
    if not from_island in sea_routes:
        return -1
    
    min_time = -1
    for stop_island, travel_time, hull_need in sea_routes[from_island]:
        if stop_island in stoped_islands:
            continue
        if hull_need >= rest_hull:
            continue
        #print("[rh:%d] #%d -> #%d t:%d h:%d" % (rest_hull, from_island, stop_island, travel_time, hull_need))
        if stop_island == target_island:
            if min_time < 0 or travel_time < min_time:
                min_time = travel_time
        else:
            t = schedule_time(stop_island, target_island, rest_hull - hull_need, stoped_islands + [stop_island])
            if t >= 0:
                if min_time < 0 or travel_time + t < min_time:
                    min_time = travel_time + t
    return min_time

print(schedule_time(island_from, island_to, hull_thick, []))