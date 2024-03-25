"""TooHard"""
def main():
    """cant-undstd"""
    num1 = input()
    num2 = input()
    num3 = input()
    biggest = largest(num1+num2+num3, num1+num3+num2)
    biggest = largest(biggest, num2+num1+num3)
    biggest = largest(biggest, num2+num3+num1)
    biggest = largest(biggest, num3+num1+num2)
    biggest = largest(biggest, num3+num2+num1)
    print(int(biggest))
def largest(grp1, grp2):
    """GG-MidTerm"""
    if grp1 > grp2:
        return grp1
    return grp2
main()
