# encoding = utf-8
"""CCC '13 S5 - Factor Solitaire
Canadian Computing Competition: 2013 Stage 1, Senior #5
In the game of Factor Solitaire, you start with the number 1, and try to
change it to some given target number n by repeatedly using the following
operation. In each step, if c is your current number, you split it into
two positive factors a, b of your choice such that c = a x b. You then add a to
your current number c to get new current number. Doing this costs you b points.
You continue doing this until your current number is n, and you try to achieve
this at the cost of a minimum total number of points.
For example, here is one way to get to 15:
• start with 1
• change 1 to 1 + 1 = 2 - cost so far is 1
• change 2 to 2 + 1 = 3 - cost so far is 1 + 2
• change 3 to 3 + 3 = 6 - cost so far is 1 + 2 + 1
• change 6 to 6 + 6 = 12 - cost so far is 1 + 2 + 1 + 1
• change 12 to 12 + 3 = 15 - done, total cost is 1 + 2 + 1 + 1 + 4 = 9.
In fact, this is the minimum possible total cost to get 15. You want to compute
the minimum total cost for other target end numbers.
"""

import ccc
target_num = 2013

ccc.start_ccc()

# cache all factors of a number for speeding
factors_pool = {}


def get_factors(n):
    factors_pool[n] = list(factor for i in range(
        1, int(n**0.5) + 1) if n % i == 0 for factor in (i, n//i))
    return factors_pool[n]


# cache all search results of one number
# key is number, value is the min cost path of key
# a XXXX number have tens factors. if a length of path is 10,
# the try times maybe too huge.
# So cache every lowest cost path of any number to target_num,
# can save many searching.
search_lowcost_pool = {}


# from current integer, try every factor of current integer until equel target
# try path is current try history
# return the lowest cost search path
def search_lowcost_path(from_num, to_num):

    if (from_num in search_lowcost_pool):
        return search_lowcost_pool[from_num]

    sub_min_score = 500000
    sub_min_path = []

    # get all factors of from_num and reverse sorting for speed
    # because try small factor to cause long path and big score
    factors = get_factors(from_num)
    factors.sort(reverse=True)

    for factor in factors:

        sub_num = factor
        sub_score = from_num // factor

        # search bingo!
        if from_num + sub_num == to_num:
            # update the lowest cost search path
            if sub_score < sub_min_score:
                sub_min_score = sub_score
                sub_min_path = [(sub_num, sub_score)]

        # search failed.
        elif from_num + factor > to_num:
            continue

        # try a sub path
        else:
            sub_path = search_lowcost_path(from_num + sub_num, to_num)
            if (sub_path is not None and len(sub_path) > 0):
                # can cache too from optimized
                sub_path_score = sum(list(zip(*sub_path))[1])

                # if sub path is a lower path, then replace min_path
                if (sub_score + sub_path_score < sub_min_score):
                    sub_min_score = sub_score + sub_path_score
                    sub_min_path = [(sub_num, sub_score)] + sub_path

    # if the lowest cost path which from from_num to to_num,
    # cache the lowest cost path of [from_num]
    if (len(sub_min_path) > 0):
        search_lowcost_pool[from_num] = sub_min_path

    return sub_min_path


the_lowest_path = search_lowcost_path(1, target_num)
print(sum(list(zip(*the_lowest_path))[1]))
print(the_lowest_path)
print(len(search_lowcost_pool))
ccc.end_ccc()
