"""CCC '20 S5 - Josh's Double Bacon Deluxe
Canadian Computing Competition: 2020 Stage 1, Senior #5

On their way to the contest grounds, Josh, his coach, and his N−2 teammates decide to stop at a burger joint that offers M distinct burger menu items. After ordering their favourite burgers, the team members line up, with the coach in the first position and Josh last, to pick up their burgers. Unfortunately, the coach forgot what he ordered. He picks a burger at random and walks away. The other team members, in sequence, pick up their favourite burger if available, or a random remaining burger if there are no more of their favourite burger. What is the probability that Josh, being last in line, will get to eat his favourite burger?

"""

from ccc import input, replace_input
replace_input(__file__[-10:-3] + ".log")

mates_cnt = int(input())
favourites = [int(p) for p in input().split(" ")]

def get_rest_burgers(burgers, except_idx) -> list:
    if except_idx == 0:
        return burgers[1:]
    elif except_idx == len(burgers) - 1:
        return burgers[:-1]
    else:
        return burgers[:except_idx] + burgers[except_idx+1:]
    
def calc_probability(favs, burgers) -> float:
    print("%15s %15s -> %-15s" % (str(favs), str(burgers), "?"))
    self_fav = favs[0]
    probability = 0.0
    if len(burgers) == 1:
        probability = favs[0] == burgers[0] and 1.0 or 0.0
    else:
        if self_fav in burgers:
            self_idx = burgers.index(self_fav)
            probability = 1.0 * calc_probability(favs[1:], get_rest_burgers(burgers, self_idx))
        else:
            p_of_onecase = 1.0 / float(len(burgers))        
            probability = sum(
                [p_of_onecase * calc_probability(favs[1:], get_rest_burgers(burgers, idx)) \
                for idx in range(0, len(burgers))])
    print("%15s %15s -> %-15s" % (str(favs), str(burgers), str(probability)))
    return probability

burgers = favourites.copy()
p_of_onecase = 1.0 / float(len(burgers))
total_probability = sum( \
    [p_of_onecase * calc_probability(favourites[1:], get_rest_burgers(burgers, idx)) \
    for idx in range(0, len(burgers))])
print(total_probability)