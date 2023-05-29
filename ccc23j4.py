import ccc

params = ccc.load_std_input_file("ccc23j4.log")

row_cnt = int(params[0][0])

first_row = params[1][0]
second_row = params[2][0]

tape_len = 0

# first row
for i in range(0, row_cnt):
    if first_row[i] == "0":  # dry
        continue
    else:  # wet
        # left
        if i == 0:
            tape_len += 1
        else:
            if first_row[i - 1] == "0":
                tape_len += 1
        # right
        if i == row_cnt - 1:
            tape_len += 1
        else:
            if first_row[i + 1] == "0":
                tape_len += 1
        if i + 1 % 2 == 0:  # top
            tape_len += 1  # top
        else:  # bottom
            if second_row[i] == "0":
                tape_len += 1

# second row
for i in range(0, row_cnt):
    if second_row[i] == "0":
        continue
    else:  # wet
        # left
        if i == 0:
            tape_len += 1
        else:
            if second_row[i - 1] == "0":
                tape_len += 1
        # right
        if i == row_cnt - 1:
            tape_len += 1
        else:
            if second_row[i + 1] == "0":
                tape_len += 1
        if (i + 1) % 2 == 0:  # bottom
            tape_len += 1
        else:
            if first_row[i] == "0":
                tape_len += 1
print(tape_len)
