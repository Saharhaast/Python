"""hamberger"""
def main():
    """hamburger"""
    num1 = int(input())
    num2 = int(input())
    meat = ((num1+num2)*2)*"*"
    print("|"*num1, meat, "|"*num2, sep="")
main()
