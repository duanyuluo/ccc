"""CCC '15 S5 - Greedy For Pies
Canadian Computing Competition: 2015 Stage 1, Senior #5
The local pie shop is offering a promotion - all-you-can-eat pies! Obviously, you can't pass up this offer.
The shop lines up N pies from left to right - the ith pie contains A; grams of sugar. Additionally, another M pies are provided - the ith of these contains B; grams of sugar.
You are first allowed to insert each of the M pies from the second group anywhere into the first list of I pies, such as at its start or end, or in between any two pies already in the list. The result will be a list of N + M pies with the constraint that the initial N pies are still in their original relative order.
Following this, you are allowed to take one walk along the new line of pies from left to right, to pick up your selection of all-you-can-eat pies! When you arrive at a pie, you may choose to add it to your pile, or skip it. However, because you're required to keep moving, if you pick up a certain pie, you will not be able to also pick up the pie immediately after it (if any). In other words, you cannot eat consecutive pies in this combined list.
Being a pie connoisseur, your goal is to maximize the total amount of sugar in the pies you pick up from the line. How many grams can you get?
Input Specification
The first line of input contains the integer N (1 < N < 3000). The next N lines contain one integer A; (1 < A; < 105, describing the integer number
of grams of sugar in pie i in the group of N pies.
The next line contains M (0 < M < 100), the number of pies in the second list. The next M lines contain one integer B; (1 S B; < 10%, describing the integer number of grams of sugar in pie ¿ in the group of M pies.
For 20% of the marks for this question, M = 0. For another 20% of the marks for this question M = 1. For another 20% of the marks for this
question M < 10.
Output Specification
Output the maximum number of grams of sugar in all the pies that you are able to pick up.
"""

from ccc import input, replace_input

# 0.log 1.log OK 
# TODO 2.log 
replace_input(__file__[-10:-3] + "_2.log")

n_pies_cnt = int(input())
n_pies_sugar = [int(input()) for i in range(0, n_pies_cnt)]
m_pies_cnt = int(input())
m_pies_sugar = [int(input()) for i in range(0, m_pies_cnt)]
m_pies_sugar.sort()

print(n_pies_sugar)
print(m_pies_sugar)

# ceil()
eat_cnt = round((n_pies_cnt + m_pies_cnt + 1) / 2)

def resort_pies():
    # must eat list by asc sorting
    must_eat_pies = m_pies_sugar + n_pies_sugar
    must_eat_pies.sort(reverse=True)
    must_eat_pies = must_eat_pies[:eat_cnt]

    eat_pies_list = []
    while len(n_pies_sugar) > 0 or len(m_pies_sugar) > 0:
        if len(n_pies_sugar) > 0 and len(m_pies_sugar) > 0:
            pie = n_pies_sugar.pop(0)
            if (len(n_pies_sugar) == 0):
                eat_pies_list.append(pie in must_eat_pies and pie or -pie)
                continue
            if pie in must_eat_pies:
                if len(eat_pies_list) == 0:
                    if m_pies_sugar[-1] in must_eat_pies and m_pies_sugar[-1] > pie:
                        eat_pies_list.append(m_pies_sugar.pop(-1))
                        n_pies_sugar.insert(0, pie)
                    else:
                        eat_pies_list.append(pie)
                else:
                    if m_pies_sugar[0] in must_eat_pies and m_pies_sugar[0] > pie:
                        eat_pies_list.append(-pie)
                        eat_pies_list.append(m_pies_sugar.pop(0))
                    else:
                        eat_pies_list.append(-m_pies_sugar.pop(0))
                        eat_pies_list.append(pie)
            else:
                if n_pies_sugar[0] in must_eat_pies:
                    eat_pies_list.append(-pie)
                    eat_pies_list.append(n_pies_sugar.pop(0))
                elif len(m_pies_sugar) > 0 and (m_pies_sugar[-1] in must_eat_pies):
                    eat_pies_list.append(-pie)
                    eat_pies_list.append(m_pies_sugar.pop(-1))
                else:
                    eat_pies_list.append(-pie)
                    if len(n_pies_sugar) > 0:
                        eat_pies_list.append(n_pies_sugar.pop(0))
        elif len(m_pies_sugar) == 0:
            eat_pies_list.append(-n_pies_sugar.pop(0))
            if len(n_pies_sugar) > 0:
                eat_pies_list.append(n_pies_sugar.pop(0))
        else:
            pie = m_pies_sugar.pop(0)
            eat_pies_list.append(-pie)
            if len(m_pies_sugar) > 0:
                eat_pies_list.append(m_pies_sugar.pop(-1))

    return eat_pies_list

def resort_pies2():
    global n_pies_sugar, m_pies_sugar

    m_pies_sugar.sort(reverse=True)

    # must eat list by asc sorting
    must_eat_pies = m_pies_sugar + n_pies_sugar
    must_eat_pies.sort(reverse=True)
    must_eat_pies = must_eat_pies[:eat_cnt]

    for i, pie in enumerate(n_pies_sugar):
        if not pie in must_eat_pies:
            n_pies_sugar[i] = -pie
    for i, pie in enumerate(m_pies_sugar):
        if not pie in must_eat_pies:
            m_pies_sugar[i] = -pie

    pend_pies = [p for p in m_pies_sugar if p < 0]
    prepare_pies = [p for p in m_pies_sugar if p > 0]

    print(n_pies_sugar)
    print(m_pies_sugar)
    print(pend_pies)
    print(prepare_pies)

    eat_pies_list = n_pies_sugar
    for pie in must_eat_pies:
        if pie in n_pies_sugar:
            idx_pie = eat_pies_list.index(pie)
            if idx_pie == 0:
                continue
            elif eat_pies_list[idx_pie - 1] < 0:
                continue
            else:
                if len(pend_pies) > 0:
                    eat_pies_list.insert(idx_pie, pend_pies.pop(0))
                else:
                    pass
        else:
            idx_pie = m_pies_sugar.index(pie)
            if eat_pies_list[0] < 0:
                eat_pies_list.insert(0, prepare_pies.pop(0))
            elif eat_pies_list[-1] < 0:
                eat_pies_list.append(prepare_pies.pop(0))
            else:
                for i in range(0, len(eat_pies_list)-1):
                    if eat_pies_list[i] < 0 and eat_pies_list[i+1] < 0:
                        eat_pies_list.insert(i, prepare_pies.pop(0))

    for pie in pend_pies:
        eat_pies_list.append(pie)
        if (len(prepare_pies)):
            eat_pies_list.append(prepare_pies.pop(0))
    for pie in prepare_pies:
        eat_pies_list.extend(prepare_pies)

    return eat_pies_list

eat_pies = resort_pies2()

print(eat_pies)
print(sum([pie for pie in eat_pies if pie > 0]))
