# CCC '21 S3 - Lunch Concert

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc2")
# ***************************************************************************

persons_cnt = int(input())
persons = [tuple([int(p) for p in input().split(" ")]) for i in range(0, persons_cnt)]

min_pos = min(persons, key=lambda p: p[0])[0]
max_pos = max(persons, key=lambda p: p[0])[0]

min_time = 0
opti_concert_pos = -1
for concert_pos in range(min_pos, max_pos):
    concert_time = 0
    for pos, speed, scope in persons:
        concert_time += speed * (abs(pos - concert_pos) - scope)
    output("%d -> %d" % (concert_pos, concert_time))
    if min_time == 0 or concert_time < min_time:
        min_time = concert_time
        opti_concert_pos = concert_pos

print(min_time)