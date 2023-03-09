import ccc
in_params = ccc.load_std_input_file("ccc23j3.log", ccc.tc_int)

person_cnt = in_params[0][0]
mark_of_day = [0] * 5

for i in range(0, person_cnt):
    for j in range(0, 5):
        if (in_params[i+1][0][j] == "Y"):
            mark_of_day[j] += 1

max_cnt = max(mark_of_day)

days = [day+1 for day in range(0, 5) if mark_of_day[day] == max_cnt]

print(days)