"""CCC '16 S3 - Phonomenal Reviews
Canadian Computing Competition: 2016 Stage 1, Senior #3
"""

def output(s, end = False, highlight=False, index=""):
    pass
# ************************ MUST REMOVE BEFORE SUMMIT ************************
from ccc import make_io
input, output = make_io(__file__, "tc2")
# ***************************************************************************

all_resto_cnt, pho_resto_cnt = tuple([int(p) for p in input().split(" ")])
pho_restos = {int(p) for p in input().split(" ")}
paths = [[int(p) for p in input().split(" ")] for q in range(0, all_resto_cnt-1)]

path_dir = {k:[] for k in range(0, all_resto_cnt)}
for path in paths:
    path_dir[path[0]].append(path[1])
    path_dir[path[1]].append(path[0])

output("all resto count : %d\npho resto count : %d" % (all_resto_cnt, pho_resto_cnt))
output(pho_restos)
output(paths)
output(path_dir)

# -> sub searched path, new to restos
def search_path(from_resto, to_restos, passed_stack):
    global pho_restos
    if len(to_restos) == 0:
        return []
    
    passed_stack.append(from_resto)
    sub_path = [from_resto, ]
    output(" + %s %20s / %20s" % (from_resto, to_restos, passed_stack))

    sub_path_list = []
    for sub_tree in path_dir[from_resto]:
        if sub_tree in passed_stack:
            continue
        sub_tree_path = search_path(sub_tree, to_restos, passed_stack)
        if set(sub_tree_path).intersection(pho_restos):
            sub_path_list.append(sub_tree_path)
            to_restos -= set(sub_tree_path)
    
    sub_path_list.sort(key=lambda x: len(x))

    for sub_tree in sub_path_list:
        if sub_path[-1] != from_resto:
            sub_path.append(from_resto)
        sub_path.extend(sub_tree)
        output(" > %s %20s / %20s -> %s" % (from_resto, to_restos, passed_stack, sub_path))

    passed_stack.pop()
    if sub_path[-1] != from_resto and len(to_restos) > 0:
        sub_path.append(from_resto)

    output(" - %s %20s / %20s -> %s" % (from_resto, to_restos, passed_stack, sub_path))
    return sub_path

start_prepare = [len(v) == 1 and k in pho_restos for (k, v) in path_dir.items()]
start_resto = start_prepare.index(True)
search_full_path = search_path(start_resto, pho_restos.copy(), [])
for idx, resto in enumerate(search_full_path):
    if resto in pho_restos:
        pho_restos.remove(resto)
    if len(pho_restos) == 0:
        output(search_full_path[:idx+1], highlight=True)
        print(idx)
        break