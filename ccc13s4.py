#encoding = utf-8
"""CCC '13 S4 - Who is Taller?
Canadian Computing Competition: 2013 Stage 1, Senior #4
You have a few minutes before your class starts, and you decide to compare the heights of your classmates. You don't have an accurate measuring device, so you just compare relative heights between two people: you stand two people back-to-back, and determine which one of the two is taller. Conveniently, none of your classmates are the same height, and you always compare correctly (i.e., you never make a mistake in your comparisons).
After you have done all of your comparisons, you would like to determine who the tallest person is between two particular classmates.
"""

import ccc
in_params = ccc.load_std_input_file("ccc13s4_1.log", ccc.tc_int)

total_stud_cnt = in_params[0][0]
records_cnt = in_params[0][1]

lower_list = [[] for i in range(total_stud_cnt)]

for i in range(1, 1+records_cnt):
    taller_id = in_params[i][0]
    lower_id = in_params[i][1]
    lower_list[taller_id-1].append(lower_id)

def find_lower(taller_id, lower_id):
    lower_ids = lower_list[taller_id-1]
    if lower_id in lower_ids:
        return True
    for id in lower_ids:
        if (find_lower(id, lower_id)):
            return True
    return False

fake_taller_id = in_params[-1][0]
fake_lower_id = in_params[-1][1]

if (find_lower(fake_taller_id, fake_lower_id)):
    print("yes")
elif (find_lower(fake_lower_id, fake_taller_id)):
    print("no")
else:
    print("unknown")
