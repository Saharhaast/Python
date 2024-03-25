"""HELPME"""
def get_num_ct(number):
    """FRFR"""
    if number == 0:
        return 1
    num_ct = 0
    while number > 0:
        num_ct += 1
        number //= 10
    return num_ct
num = abs(int(input()))
num_ct = get_num_ct(num)
print(num_ct)
