# CCC '20 S3 - Searching for Strings

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc1")
# ***************************************************************************

needle_string = input()
haystack_string = input()

permutations = set()

def make_permutations(num_set):
    if len(num_set) == 1:
        yield num_set.pop(), 
    for i in num_set:
        for p in make_permutations(num_set - {i}):
            yield i, *p

for p in make_permutations(set(range(0, len(needle_string)))):
    permutations.add("".join([needle_string[i] for i in p]))

output(permutations)
cnt = 0
for p in permutations:
    pos = haystack_string.find(p)
    if pos >= 0:
        cnt += 1
        output("%s<[%s]>%s" % (haystack_string[:pos], haystack_string[pos:pos+len(p)], haystack_string[pos+len(p):]))

print(cnt)