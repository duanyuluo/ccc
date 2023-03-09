"""CCC '21 S4 - Daily Commute
Canadian Computing Competition: 2021 Stage 1, Senior #4
"""

def output(s):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__)
# ***************************************************************************

stations_cnt, walkways_cnt, days_cnt = tuple([int(p) for p in input().split(" ")])
output("stations = %d \nwalkways = %d \ndays = %d" % (stations_cnt, walkways_cnt, days_cnt))

walkways = {int(k):int(v) for (k, v) in [tuple(input().split(" ")) for i in range(walkways_cnt)]}
output("Walkways : " + str(walkways))

metro_line = [int(p) for p in input().split(" ")]
output("stop stations : " + str(metro_line))

day_swap_plans = [[int(p) for p in input().split(" ")] for q in range(days_cnt)]
output("swap plan : " + str(day_swap_plans))

def find_shortcut(metro_line):
    if len(metro_line) == 1 and metro_line[0] == 4:
        return 0
    cur_station = metro_line[0]
    after = metro_line[1:]
    if cur_station in walkways and walkways[cur_station] in after:
        skip_idx = metro_line.index(walkways[cur_station])
        if skip_idx > 1 and 4 in metro_line[skip_idx:]:   
            output("skip %d -> %d" % (cur_station, metro_line[skip_idx]))         
            return 1 + find_shortcut(metro_line[skip_idx:])
    return 1 + find_shortcut(metro_line[1:])
    
for s1, s2 in day_swap_plans:
    metro_line[s1-1], metro_line[s2-1] = metro_line[s2-1], metro_line[s1-1]
    output(metro_line)
    print(find_shortcut(metro_line[:metro_line.index(4)+1]))