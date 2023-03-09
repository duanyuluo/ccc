"""CCC '17 S5 - RMT
Canadian Computing Competition: 2017 Stage 1, Senior #5
The Rail Metro Transit (RMT) operates a very unusual subway system. There are I subway stations numbered from 1 to N. There are M subway lines numbered from 1 to M, with each station belonging to exactly one line and at least one station per line. The subway lines are circular. That is, if a station is numbered S, the next station after S is the station on the same line with the next largest number, unless S is the greatest number of a station in the line, in which case the next station after S is the station on the same line with the least number.
RMT is conducting a load test of their system using volunteer passengers to ride the subway trains. The test begins with one subway train in each station and for every ¿, there are A; passengers in the train at station i. The volunteers do not leave their assigned trains throughout the entire duration of the load test.
Throughout the test, RMT will perform Q actions. Each of the W actions is one of two types: either they will survey the total number of passengers in the trains at the stations numbered from I to r; or they will operate all the trains on some line x. When a train on line x is operated, it goes to the next station in that line.
You are RMT's biggest fan, so you have generously volunteered to keep track of MT's actions and report the answers to their surveys.

Input Specification
The first line will contain three space-separated integers N, M, and Q (1 < M < N <150000; 1 < Q < 150000). The second line will contain the subway line numbers that each station from 1 to N belongs to: L1, [2, .., Ly. The third line will contain I integers A1, A2, ..., An (1 < A; <7000) representing the initial number of passengers at each station from 1 to N.
The next Q lines will each have one of the following forms:
• 1 l r, which represents a survey (1 < I Sr < I).
• 2 x, which represents RMT operating line * (1 < x < M).
For 2 of the 15 available marks, I < 1000 and Q < 1000.
For an additional 2 of the 15 available marks, I; < I; +1 (1 Si < I).
For an additional 3 of the 15 available marks, M < 200.
For an additional 3 of the 15 available marks, there will be no more than 200 trains on any single line.

Output Specification
For every survey, output the answer to the survey on a separate line.
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

stations_cnt, lines_cnt, actions_cnt = tuple([int(p) for p in input().split(" ")])
stations = [int(p) for p in input().split(" ")]
passengers = [int(p) for p in input().split(" ")]

stations_group = []
for line in range(1, lines_cnt+1):
    stations_group.append([i for i, s in enumerate(stations) if s == line])

actions = []
for i in range(0, actions_cnt):
    actions.append([int(p) for p in input().split(" ")])

print(stations)
print(passengers)
print(actions)
print(stations_group)

def op_metro(metro_line):
    last_station_cnt = 0
    pre_station_idx = -1
    station_indexes = stations_group[metro_line-1]
    for station_idx in reversed(station_indexes):
        if pre_station_idx < 0:
            last_station_cnt = passengers[station_idx]
        else:
            passengers[pre_station_idx] = passengers[station_idx]
        pre_station_idx = station_idx
    passengers[station_indexes[0]] = last_station_cnt
            
for act in actions:
    if act[0] == 2:
        op_metro(act[1])
        print(passengers)
    elif act[0] == 1:
        p_cnt = 0
        for s in range(act[1], act[2]+1):
            p_cnt += passengers[s-1]
        print(p_cnt)