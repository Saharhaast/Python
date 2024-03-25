"""Harshad"""
def main():
    """Number"""
    for _ in range(10):
        num = int(input())
        if num == 0:
            print("No")
        elif len(str(num)) == 1:
            if num % num == 0:
                print("Yes")
            else:
                print("No")
        else:
            if num % sum_of_num(num) == 0:
                print("Yes")
            else:
                print("No")
def sum_of_num(num):
    """Gwrrrr"""
    sumn = 0
    if num < 0:
        for i in str(num)[1:]:
            sumn += int(i)
        sumn *= -1
    else:
        for i in str(num):
            sumn += int(i)
    return sumn
main()
