"""CCC '16 S4 - Combining Riceballs
Canadian Computing Competition: 2016 Stage 1, Senior #4
Alphonse has N rice balls of various sizes in a row. He wants to form the largest rice ball possible for his friend to eat. Alphonse can perform the following operations:
If two adjacent rice balls have the same size, Alphonse can combine them to make a new rice ball. The new rice ball's size is the sum of the two old rice balls' sizes. It occupies the position in the row previously occupied by the two old rice balls.
If two rice balls have the same size, and there is exactly one rice ball between them, Alphonse can combine all three rice balls to make a new rice ball. (The middle rice ball does not need to have the same size as the other two.) The new rice ball's size is the sum of the three old rice balls' sizes. It occupies the position in the row previously occupied by the three old rice balls.
Alphonse can perform each operation as many times as he wants.
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

riceball_cnt = int(input())
riceballs = [int(rb) for rb in input().split(" ")]

combined_rbs = []

while len(riceballs) > 0:
    idx = 0
    while idx < len(riceballs):
        if idx < len(riceballs)-1 and riceballs[idx] == riceballs[idx+1]:
            combined_rbs.append(riceballs[idx] * 2)
            idx += 2
            continue
        if idx < len(riceballs)-2 and riceballs[idx] == riceballs[idx+2]:
            combined_rbs.append(riceballs[idx] * 2 + riceballs[idx+1])
            idx += 3
            continue
        combined_rbs.append(riceballs[idx])
        idx += 1

    if len(riceballs) == len(combined_rbs):
        break
    riceballs = combined_rbs.copy()
    combined_rbs.clear()

print(riceballs)
print(max(riceballs))