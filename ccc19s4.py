"""CCC '19 S4 - Tourism
Canadian Computing Competition: 2019 Stage 1, Senior #4

You are planning a trip to visit I tourist attractions. The attractions are numbered from 1 to N and must be visited in this order. You can visit at most K attractions per day, and want to plan the trip to take the fewest number of days as possible.
Under these constraints, you want to find a schedule that has a nice balance between the attractions visited each day. To be precise, we assign a score a; to attraction i. Given a schedule, each day is given a score equal to the maximum score of all attractions visited that day. Finally, the scores of each day are summed to give the total score of the schedule. What is the maximum possible total score of the schedule, using the fewest days possible?

Input Specification
The first line contains two space-separated integers N and K (1 < K SN < 10%.
The next line contains N space separated integers a; (1 5 a; <10%.

Output Specification
Output a single integer, the maximum possible total score.
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + "_1.log")

view_cnt, max_per_day = tuple([int(p) for p in input().split(" ")])
views_score = [int(p) for p in input().split(" ")]
days_cnt = view_cnt // max_per_day + ((view_cnt % max_per_day) > 0 and 1 or 0)

# (start pos, flex cnt) -> max scores)
max_scores_pool = {}
def get_max_scores(start_idx, flex_cnt):
    if start_idx >= len(views_score):
        return 0
    if (start_idx, flex_cnt) in max_scores_pool:
        return max_scores_pool[(start_idx, flex_cnt)][0]
    if flex_cnt == 0:
        max_score = max(views_score[start_idx:start_idx+max_per_day-1])
        max_score += get_max_scores(start_idx + max_per_day, 0)
        max_scores_pool[(start_idx, flex_cnt)] = (max_score, max_per_day)
    else:
        the_max_score = 0
        the_max_len = 0
        for vc in range(max_per_day - flex_cnt, max_per_day + 1):
            max_score = max(views_score[start_idx:start_idx+vc])
            max_score += get_max_scores(start_idx+vc, flex_cnt-(max_per_day-vc))
            if max_score > the_max_score:
                the_max_score = max_score
                the_max_len = vc
        max_scores_pool[(start_idx, flex_cnt)] = (the_max_score, the_max_len)
    return max_scores_pool[(start_idx, flex_cnt)][0]

print(views_score)
print(get_max_scores(0, days_cnt * max_per_day - view_cnt))
print(max_scores_pool)

print(list(zip(max_scores_pool)))