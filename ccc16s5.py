"""CCC '16 S5 - Circle of Life
Canadian Computing Competition: 2016 Stage 1, Senior #5
You may have heard of Conway's Game of Life, which is a simple set of rules for cells on a grid that can produce incredibly complex configurations.
In this problem we will deal with a simplified version of the game.
There is a one-dimensional circular strip of I cells. The cells are numbered from 1 to N in the order you would expect: that is, cell 1 and cell 2 are adjacent, cell 2 and cell 3 are adjacent, and so on up to cell I - 1, which is adjacent to cell I. Since the trip is circular, cell 1 is also adjacent to cell N.
Each cell is either alive (represented by a 1) or dead (represented by a ©). The cells change over a number of generations. If exactly one of the cell's neighbours is alive in the current generation, then the cell will be alive in the next generation. Otherwise, the cell will be dead in the next generation.
Given the initial state of the strip, find the state after T generations.
Input Specification
The first line will contain two space-separated integers N and T (3 < I < 100000; 1 < I < 1015). The second line will contain a string consisting of exactly N characters, representing the initial configuration of the N cells. Each character in the string will be either © or 1). The initial state of cell I is given by the ith character of the string. The character (1) represents an alive cell and the character © represents a dead cell.
• For 1 of the 15 available marks, I < 15 and T ≤ 15.
• For an additional 6 of the 15 available marks, N < 15.
• For an additional 4 of the 15 available marks, I < 4000 and T < 10 000 000.
Note that for full marks, solutions will need to handle 64-bit integers. For example:
• in C/C++, the type long long should be used;
• in Java, the type long should be used;
• in Pascal, the type (int64 should be used.

Input Specification
The first line will contain two space-separated integers N and T3 < N < 100000; 1 S I < 1015. The second line will contain a string consisting of exactly I characters, representing the initial configuration of the I cells. Each character in the string will be either 0 or (1). The initial state of cell I is given by the ith character of the string. The character 1 represents an alive cell and the character o represents a dead cell.
• For 1 of the 15 available marks, I < 15 and T < 15.
• For an additional 6 of the 15 available marks, I < 15.
• For an additional 4 of the 15 available marks, N < 4000 and T ≤ 10 000 000.
Note that for full marks, solutions will need to handle 64-bit integers. For example:
• in C/C++, the type long long should be used;
• in Java, the type long should be used;
• in Pascal, the type int64 should be used.

Output Specification
Output the string of N characters representing the final state of the cells, in the same format and order as the input.
"""

from ccc import input, replace_input

replace_input(__file__[-10:-3] + ".log")

cells_cnt, gen_cnt = tuple([int(s) for s in input().split(" ")])
cells_status = input()


def get_status(idx, delta=0):
    return int(cells_status[(idx + delta + cells_cnt) % cells_cnt])


for gen in range(0, gen_cnt):
    new_gen = ""
    for idx in range(cells_cnt):
        new_gen += (get_status(idx, -1) ^ get_status(idx, 1)) and "1" or "0"
    cells_status = new_gen

print(cells_status)
