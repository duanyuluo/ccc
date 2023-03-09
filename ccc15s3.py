"""CCC '15 S3 - Gates
Canadian Computing Competition: 2015 Stage 1, Senior #3
For your birthday, you were given an airport.
The airport has G gates, numbered from 1 to G. P planes arrive at the airport, one after another. You are to assign the ith plane to permanentl dock at any gate 1, ..., 9; (1 S 9; ≤ G), at which no previous plane has docked. As soon as a plane cannot dock at any gate, the airport is shut down and no future planes are allowed to arrive.
In order to keep the person who gave you the airport happy, you would like to maximize the number of planes starting from the beginning that can all dock at different gates.
Input Specification
The first line of input contains G (1 < G < 10%, the number of gates at the airport.
The second line of input contains P(1 < P < 105), the number of planes which will land.
The next P lines contain one integer 9;, (1 < g; < G), such that the ith plane must dock at some gate from 1 to g, inclusive.
Note that for at least 20% of the marks for this question, P< 2000 and G < 2 000.
Output Specification
Output the maximum number of planes that can land starting from the beginning.
"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

gates_cnt = int(input())
planes_cnt = int(input())
planes_prefer = []
for i in range(0, planes_cnt):
    planes_prefer.append(int(input()))

gates_status = [False] * gates_cnt

def enter_gate(prefer_gate):
    for i in range(prefer_gate, 0, -1):
        if gates_status[i]:
            continue
        gates_status[i] = True
        return True
    return False

for plane in planes_prefer:
    if (not enter_gate(plane)):
        break
    
print(len([g for g in gates_status if g]))
