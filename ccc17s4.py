"""CCC '17 S4 - Minimum Cost Flow
Canadian Computing Competition: 2017 Stage 1, Senior #4
The city of Watermoo has buildings numbered 1, 2, ...
,I. The city has M pipes that connect pairs of buildings. Due to urban planning oversights,
building 1 is the only sewage treatment plant in the city. Each pipe can be either active or inactive. The set of active pipes forms a valid plan if building 1 is directly or indirectly connected to each other building using active pipes. (Pipes directly connect pairs of buildings. Buildings X and Z are indirectly connected if X is directly or indirectly connected to Y, and Y is directly or indirectly connected to Z.)
The municipal government of Watermoo is currently operating a valid plan of I - 1 pipes today, but they think it is too expensive! Each pipe has a monthly maintenance fee that the city must pay when it is active, and the total cost of a valid plan is the sum of the maintenance fees of its active pipes. (Inactive pipes cost nothing.)
Additionally, researchers at the University of Watermoo have developed an experimental pipe enhancer which you can use on one pipe of your choice.
It will reduce that pipe's cost from C down to max (0, C- D), where D is the enhancer's strength.
The city wants you to minimize the cost of the plan, and they want you to do it quickly. Every day, the city will allow you to activate one pipe, and deactivate another pipe. How many davs do you need to make the set of active pipes form a valid plan, whose cost is minimum among all valid plans and all choices of enhanced pipe?
Note that it is possible that the plan becomes invalid while you are working, but by the end it should be a valid plan.

Input Specification
The first line will contain the integers N, M, and D (1 < I < 100000, IN - 1 < M < 200000, 0 < D < 109. Each of the next M lines contain three integers A;; Bi, and C;, which means that there is a pipe from building A; to building B; that costs C; per month when activated (1 S A;, B; S N, 1 5 C; 5 109. The first I - 1 of these lines represent the valid plan the city is currently using.
It is guaranteed that there is at most one pipe connecting any two buildings and no pipe connects a building to itself.
For 3 of the 17 available marks, N < 8, M < 28 and D = 0.
For an additional 5 of the 17 available marks, I < 1000 and M < 5000 and D = 0.
For an additional 3 of the 17 available marks, D = 0.
For an additional 2 of the 17 available marks, N < 1000 and M ≤ 5000.
Note: The final 2 of the 17 available marks consists of test cases made by and r3mark and were not present on the CCC. These test cases were made in response to the initial incorrect official solution presented.

Output Specification
Output one integer on a single line, the minimum number of days to complete this task. If the initial valid plan is already an optimal plan, then output 0.
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

builds_cnt, pipes_cnt, d_pipe_enhancer = tuple([int(p) for p in input().split(" ")])

# build#1 #2 fee active?
pipes_sortby_build = []
pipes_sortby_fee = []
for idx, p in enumerate(range(0, pipes_cnt)):
    pipes_sortby_build.append(list([int(p) for p in input().split(" ")] + [idx < builds_cnt-1 and 1 or 0]))
    pipes_sortby_build.sort(key=lambda p: p[0])

pipes_sortby_fee = pipes_sortby_build.copy()
pipes_sortby_fee.sort(key=lambda p: p[2], reverse=True)

def plan_fee(pipes):
    return sum(p[2] for p in pipes if p[3])

def is_valid_plan(pipes):
    valid_builds = {1}
    for p in [p for p in pipes if p[3]]:
        if p[0] in valid_builds or p[1] in valid_builds:
            valid_builds.add(p[0])
            valid_builds.add(p[1])
    return len(valid_builds) == builds_cnt

def optimal_plan(pipes):
    cur_plan_fee = plan_fee(pipes_sortby_build)

    optimal_cnt = 0
    for invalid_idx, invalid_pipe in enumerate(pipes):
        if invalid_pipe[3] == 1:
            continue
        for valid_pipe in pipes_sortby_fee:
            if valid_pipe[3] == 0:
                continue
            valid_idx = pipes.index(valid_pipe)
            pipes[invalid_idx][3] = 1
            pipes[valid_idx][3] = 0
            if is_valid_plan(pipes) and plan_fee(pipes) < cur_plan_fee:
                optimal_cnt += 1
                print("step : " + str(pipes))
                break
            pipes[invalid_idx][3] = 0
            pipes[valid_idx][3] = 1
    if d_pipe_enhancer > 0:
        max_idx = max(enumerate(pipes), key=lambda pp: pp[1][3] == 1 and pp[1][2] or -1)[0]
        pipes[max_idx][2] -= d_pipe_enhancer
        pipes[max_idx][2] = max(pipes[max_idx][2], 0)
    return optimal_cnt, pipes

print("orgn : " + str(pipes_sortby_build))
print("orign fee : " + str(plan_fee(pipes_sortby_build)))
optimal_cnt, pipes_sortby_build = optimal_plan(pipes_sortby_build)
print("optimal cnt : " + str(optimal_cnt))
print("after : " + str(pipes_sortby_build))
print("after fee : " + str(plan_fee(pipes_sortby_build)))
