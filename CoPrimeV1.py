"""Ejudge"""
def main():
    """CoPrimeV1"""
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        for i in range(num2, 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                if i == 1:
                    print("YES")
                else:
                    print("NO")
                print(i)
                break
    else:
        for i in range(num1, 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                if i == 1:
                    print("YES")
                else:
                    print("NO")
                print(i)
                break
main()
