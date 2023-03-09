"""CCC '14 S5 - Lazy Fox
Canadian Computing Competition: 2014 Stage 1, Senior #5
You have a pet Fox who loves treats. You have I neighbours at distinct locations (described as points on the Cartesian plane) which hand out treats to your pet Fox, and each neighbour has an unlimited number of treats to give out. The origin (which is where the Fox starts) will not be one of these N locations.
What does the Fox say, in order to get these treats? That is a good question, but not our concern. The Fox moves from location to location to gather exactly one treat from each location on each visit. He can revisit any previous location, but cannot visit the same location on two consecutive visits.
Your Fox is very lazy. The distance your Fox is willing to travel after each treat will strictly decrease. Specifically, the distance from the origin to his first treat location must be larger than the distance from his first treat location to his second treat location, which in turn is larger than the distance between his second treat location and his third treat location, and so on.
What is the largest number of treats your Fox gathers?
"""

from ccc import input, replace_input, start_ccc, end_ccc
replace_input("ccc14s5.log")
start_ccc()

neighbours_cnt = int(input())
positions = []

for i in range(1, neighbours_cnt+1):
    positions.append(tuple([int(p) for p in input().split(" ")]))

def dist_of(pt1, pt2):
    return (abs(pt1[0] - pt2[0]))^2 * (abs(pt1[1] - pt2[1]))^2

def walk_to_neig(from_pt, last_dist):
    global positions
    max_treats_cnt = 0

    for pt in positions:
        dist = dist_of(from_pt, pt)
        if (dist == 0):
            continue
        if (last_dist >= 0 and dist >= last_dist):
            continue
        
        print("%9s %3d -> %9s %3d" %(from_pt, last_dist, pt, dist))
        #print(str(from_pt) + str(last_dist) + " -> " + str(pt) + str(dist))

        if (max_treats_cnt == 0):
            max_treats_cnt = 1

        cnt = walk_to_neig(pt, dist) + 1
        if (cnt > max_treats_cnt):
            max_treats_cnt = cnt

    return max_treats_cnt

print(walk_to_neig((0, 0), -1))
end_ccc()