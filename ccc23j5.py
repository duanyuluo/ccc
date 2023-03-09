import ccc
params = ccc.load_std_input_file("ccc23j5_2.log")

want_word = params[0][0]
row_cnt = int(params[1][0])
col_cnt = int(params[2][0])
chs_table = params[3:]

hv_dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dg_dir = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

search_count = 0

def search(r, c, ch_idx, search_dir, search_path):
    global search_count
    for i in range(0, len(search_dir)):
        search_r = r + search_dir[i][0]
        search_c = c + search_dir[i][1]
        if search_r >= row_cnt or search_r < 0:
            continue
        if search_c >= col_cnt or search_c < 0:
            continue
        if (want_word[ch_idx] == chs_table[search_r][search_c]):
            new_path = list(search_path)
            new_path.append((search_r, search_c, want_word[ch_idx]))
            if ch_idx == len(want_word) - 1:
                search_count += 1
                print(new_path)
                continue
            search(search_r, search_c, ch_idx+1, search_dir, new_path)

for r in range(0, row_cnt):
    for c in range(0, col_cnt):
        ch = chs_table[r][c]
        if (ch == want_word[0]):
            search(r, c, 1, hv_dir + dg_dir, [(r, c, ch), ])
            #search(r, c, 1, hv_dir, [(r, c, ch), ])
            #search(r, c, 1, dg_dir, [(r, c, ch), ])

print(search_count)