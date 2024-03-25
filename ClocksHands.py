"""CH"""
def main():
    """ClockHands"""
    hour = int(input())
    minutes = int(input())
    hour *= 5
    hour += minutes / 12
    hour %= 60
    print(minutes <= hour < minutes+1)
main()
