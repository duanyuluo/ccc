"""CCC '22 S3 - Good Samples
Canadian Computing Competition: 2022 Stage 1, Senior #3
"""

def output(s):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc2")
# ***************************************************************************

notes_cnt, max_pitch, good_cnt = tuple([int(p) for p in input().split(" ")])

def is_good(notes):
    return len(set(notes)) == len(notes)

def get_all_pieces(sample):
    pieces = [sample[:i+1] for i in range(0, len(sample))]
    if len(sample) > 1:
        pieces.extend(get_all_pieces(sample[1:]))
    return pieces

good_samples = []

from itertools import product
ps = [[i+1 for i in range(0, notes_cnt)] for i in range(0, notes_cnt)]
for t in product(*ps):
    pieces = get_all_pieces(t)
    good_of_pieces = [is_good(p) and 1 or 0 for p in pieces]
    good_pieces_cnt = sum(good_of_pieces)
    output("%s -> [%2d] : %s" % (t, good_pieces_cnt, good_of_pieces), highlight=good_pieces_cnt == good_cnt)
    if good_pieces_cnt == good_cnt:
        good_samples.append(t)

print(len(good_samples) > 0 and good_samples[0] or -1)
output("", end=True)