"""CCC '18 S4 - Balanced Trees
Canadian Computing Competition: 2018 Stage 1, Senior #4
Trees have many fascinating properties. While this is primarily true for trees in nature, the concept of trees in math and computer science is also interesting. A particular kind of tree, a perfectly balanced tree, is defined as follows.
Every perfectly balanced tree has a positive integer weight. A perfectly balanced tree of weight 1 always consists of a single node. Otherwise, if the weight of a perfectly balanced tree is w and w > 2, then the tree consists of a root node with branches to k subtrees, such that 2 < k < w. In this case, all k subtrees must be completely identical, and be perfectly balanced themselves.
In particular, all k subtrees must have the same weight. This common weight must be the maximum integer value such that the sum of the weights of all k subtrees does not exceed w, the weight of the overall tree. For example, if a perfectly balanced tree of weight 8 has 3 subtrees, then each subtree would have weight 2, since 2 + 2 + 2 = 6 ≤ 8.
Given N, find the number of perfectly balanced trees with weight I.
"""

weight = [4, 10]

def gen_pbtree(weight):
    tree_cnt = 0
    if weight == 1:
        tree_cnt = 1
    else:
        for sub_cnt in range(2, weight+1):
            tree_cnt += gen_pbtree(weight // sub_cnt)
    return tree_cnt

for w in weight:
    print("N = %d -> PB Trees = %d" % (w, gen_pbtree(w)))