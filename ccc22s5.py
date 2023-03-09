"""CCC '22 S5 - Good Influencers
Canadian Computing Competition: 2022 Stage 1, Senior #5
"""

def output(s):
    pass

# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc2")
# ***************************************************************************

students_cnt = int(input())
relationships = {k:[] for k in range(1, students_cnt+1)}
for i in range(1, students_cnt):
    l, r = tuple([int(p) for p in input().split(" ")])
    relationships[l].append(r)
    relationships[r].append(l)
output(relationships)

codes = list(input())
output(codes)

costs = [int(p) for p in input().split(" ")]
output(costs)

while True:
    per_cost = max(costs) + 1
    stu_idx = -1
    friends = set()
    for idx, code in enumerate(codes):
        if code == "Y":
            n_list = [n for n in relationships[idx+1] if codes[n-1] == "N"]
            if len(n_list) == 0:
                continue
            pc = costs[idx] / len(n_list)
            output("...[%d] -> %s" % (pc, str(n_list)))
            if pc < per_cost or friends.issubset(set(n_list)):
                per_cost = pc
                stu_idx = idx
                friends = set(n_list)

    if stu_idx >= 0:
        codes[stu_idx] = "P"
        for id in friends:
            codes[id-1] = "Y"
        output("P+ {%s}\nN- %s" % (stu_idx+1, friends))

    output(codes, index="scan")
    if all([code in "YP" for code in codes]):
        break

output(sum([costs[i] for i in range(0, students_cnt) if codes[i] == "P"]), end=True)