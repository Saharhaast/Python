"""Ejudge"""
def add(month):
    """add"""
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = 0
    for i in range(month-1):
        ans += year[i]
    return ans

def main():
    """NumDays"""
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day1 = int(input())
    month1 = int(input())
    day2 = int(input())
    month2 = int(input())
    if day1 > year[month1-1] or day2 > year[month2-1]:
        print("Impossible")
    else:
        dayans1 = add(month1)+day1
        dayans2 = add(month2)+day2
        print(abs(dayans1-dayans2))
main()
