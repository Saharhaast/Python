"""SumOfNum"""
def main():
    """ScytheOfVyse"""
    goal = int(input())
    number = int(input())
    sumt = number
    while number != -1 and sumt != goal:
        number = int(input())
        if number != -1:
            sumt += number
    print(sumt)
main()
