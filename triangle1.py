"""Triangle1"""
def main1(a, b, c):
    """tryhard"""
    diff_1 = abs(c ** 2 - (a ** 2 + b ** 2))
    diff_2 = abs(b ** 2 - (a ** 2 + c ** 2))
    diff_3 = abs(a ** 2 - (b ** 2 + c ** 2))
    if diff_1 <= 0.01 or diff_2 <= 0.01 or diff_3 <= 0.01:
        return "Yes"
    else:
        return "No"
a = float(input())
b = float(input())
c = float(input())
result = main1(a, b, c)
print(result)
main1(a, b, c)

