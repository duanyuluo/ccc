#encoding = utf-8
"""CCC '13 S5 - Factor Solitaire
Canadian Computing Competition: 2013 Stage 1, Senior #5
For example, here is one way to get to 15:
• start with 1
• change 1 to 1 + 1 = 2 - cost so far is 1
• change 2 to 2 + 1 = 3 - cost so far is 1 + 2
• change 3 to 3 + 3 = 6 - cost so far is 1 + 2 + 1
• change 6 to 6 + 6 = 12 - cost so far is 1 + 2 + 1 + 1
• change 12 to 12 + 3 = 15 - done, total cost is 1 + 2 + 1 + 1 + 4 = 9.
"""

import ccc
target_num = 2013

ccc.start_ccc()

# cache all factors of a number for speeding

def get_factors(n):
    return factors_pool[n]

# cache all search results of one number
# key is number, value is the min cost path of key
search_lowcost_pool = {}

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
            sub_path = search_lowcost_path(from_num + sub_num, to_num)

                # if sub path is a lower path, then replace min_path
                if (sub_score + sub_path_score < sub_min_score):
                    sub_min_score = sub_score + sub_path_score
                    sub_min_path = [(sub_num, sub_score)] + sub_path

    if (len(sub_min_path) > 0):
        search_lowcost_pool[from_num] = sub_min_path

    return sub_min_path

the_lowest_path = search_lowcost_path(1, target_num)
print(sum(list(zip(*the_lowest_path))[1]))
print(the_lowest_path)
print(len(search_lowcost_pool))
<<<<<<< Updated upstream
ccc.end_ccc()
=======
ccc.end_ccc()
>>>>>>> Stashed changes
