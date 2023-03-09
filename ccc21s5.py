"""CCC '21 S5 - Math Homework
Canadian Computing Competition: 2021 Stage 1, Senior #5
"""
# ************************ MUST REMOVE BEFORE SUMMIT ************************
def output(s):
    pass
from ccc import make_io
input, output = make_io(__file__, "Test case 2")
# ***************************************************************************

sequence_len, requirements_cnt = tuple([int(p) for p in input().split(" ")])
requirements = [tuple([int(p) for p in input().split(" ")]) for i in range(0, requirements_cnt)]
requirements.sort(key=lambda p: p[1] - p[0])
output(requirements)

def calc_GCD(numbers):
    max_num = max(numbers)
    for divisor in range(max_num, 0, -1):
        if all([n % divisor == 0 for n in numbers]):
            return divisor
    return 0

numbers = [0] * sequence_len
for i1, i2, gcd in requirements:
    if i1 == i2:
        numbers[i1-1] = gcd;
    else:
        max_num = max(numbers) * gcd
        for i in range(i1-1, i2):
            if numbers[i] == 0:
                try_numbers = [n for n in range(gcd, max_num, gcd)]
                try_numbers.sort(reverse=True)
                for n in try_numbers:
                    if not n in numbers:
                        numbers[i] = n
                        break
            elif numbers[i] % gcd != 0:
                numbers[i] = 0
                continue

if all([n > 0 for n in numbers]):
    print(numbers)
else:
    print("Impossible")