# CCC '23 S5 - The Filter

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_o
#output = make_o()
# ***************************************************************************

import numpy

n = 12

def filter(level, num : numpy.double):
    if num == 1/3 or num == 2/3 or num == 0 or num == 1.0:
        return 0
    if level == 100:
        return 0
    if num <= 1 / 3:
        return filter(level + 1, num * 3.0)
    elif num >= 2 / 3:
        return filter(level + 1, (num * 3.0 - 2.0))
    else:
        return level
    
unfilter = []
for i in range(0, n+1):
    lvl = filter(1, i / n)
    if lvl == 0:
        unfilter.append(i)
        output("%d/%d unfilter" % (i, n))
    else:
        output("%d/%d filter by %2dth level" % (i, n, lvl))

print(unfilter)