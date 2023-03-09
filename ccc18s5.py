"""CCC '18 S5 - Maximum Strategic Savings
Canadian Computing Competition: 2018 Stage 1, Senior #5
A long time ago in a galaxy far, far away, there are I planets numbered from 1 to I. Each planet has M cities numbered from 1 to M. Let city f of planet e be denoted as (e, f).
There are N× Ptwo-way flights in the galaxy. For every planet e (1 ≤ e < I), there are Pflights numbered from 1 to P. Flight i connects cities (e, ai) and (e,b;) and costs c; energy daily to maintain.
There are M X Q two-way portals in the galaxy. For all cities with number f (1 ≤ f < M), there are Q two-way portals numbered from 1 to Q. Portal j connects cities (I;›f) and (3; f) and costs ›; energy daily to maintain.
It is possible to travel between any two cities in the galaxy using only flights and/or portals.
Hard times have fallen on the galaxy. It was decided that some flights and /or portals should be shut down to save as much energy as possible, but it should remain possible to travel between any two cities afterwards.
What is the maximum sum of energy that can be saved daily?

Input Specification
The first line contains four space-separated integers N, M, P, Q (1 < N, M, P, Q < 10°).
Then Plines follow; the i-th one contains three space-separated integers aj, b;, c (1 5 aj, b; ≤ M, 1 5 Ci < 108).
Then Q lines follow; the j-th one contains three space-separated integers I jU, 2; (1 5 IjU; ≤ N, 1 5 2; 510%.
It is guaranteed that it will be possible to travel between any two cities using flights and /or portals. There may be multiple flights /portals between the same pair of cities or a flight/portal between a city and itself.

Output Specification
Output a single integer, the maximum sum of energy that can be saved daily.
"""

"""
城市之间全联通，只需要Flight和Portal的总数是城市总数-1即可。所以，只需要：
1、罗列所有星球的Flight和Portal，并将两者合并
2、将航线（Flight+Portal）的成本降序，从高到低遍历，逐个只要排出后依旧全联通即可，直至满足N-1
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

planets_cnt, cities_cnt, flights_cnt, portals_cnt = tuple([int(p) for p in input().split(" ")])

flights = []
for i in range(0, flights_cnt):
    flights.append([int(p) for p in input().split(" ")] + [1])
    if flights[-1][0] > flights[-1][1]:
        flights[-1][0], flights[-1][1] = flights[-1][1], flights[-1][0]

portals = []
for i in range(0, portals_cnt):
    portals.append([int(p) for p in input().split(" ")] + [1])

min_lines_cnt = planets_cnt * cities_cnt - 1
cur_lines_cnt = len(flights) * planets_cnt + len(portals) * planets_cnt

lines = []
lines.extend([p+1, f[0], p+1, f[1], f[2], f[3]] for p in range(0, planets_cnt) for f in flights)
lines.extend([p[0], c, p[1], c, p[2], p[3]] for p in portals for c in range(0, cities_cnt))
lines.sort(key=lambda l:l[4], reverse=True)

print(*lines, sep="\n", end="\n" + "*"*20 + "\n")

def is_valid_plan():
    global lines
    cities = {(2, 1)}
    cur_found_cities_cnt = len(cities)
    while True:
        for line in [l for l in lines if l[5]]:
            if (line[0], line[1]) in cities or (line[2], line[3]) in cities:
                cities.add((line[0], line[1]))
                cities.add((line[2], line[3]))
            if len(cities) == cities_cnt * planets_cnt:
                return True
        if len(cities) == cur_found_cities_cnt:
            break
        else:
            cur_found_cities_cnt = len(cities)
    return False

for idx, line in enumerate(lines):
    lines[idx][5] = 0
    if not is_valid_plan():
        lines[idx][5] = 1
    if len([l for l in lines if l[5]]) == min_lines_cnt:
        break

print(*lines, sep="\n", end="\n" + "*"*20 + "\n")
print(sum([l[4] for l in lines]) - sum([l[4] for l in lines if l[5]]))