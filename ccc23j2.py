import ccc

in_params = ccc.load_std_input_file("ccc23j2_1.log", ccc.tc_int)

SHU_table = {"Poblano":1500, "Mirasol":6000, "Serrano":15500, "Cayenne":40000, "Thai":75000, "Habanero":125000}

print(in_params)

SHU = 0

cnt = in_params[0][0]
for i in range(1, cnt+1):
    name = in_params[i][0]
    a_shu = SHU_table[name]
    SHU += a_shu

print(SHU)