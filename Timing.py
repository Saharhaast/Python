"""Timing"""
def main():
    """Timing"""
    in_1 = int(input())
    secs = in_1
    mins = secs // 60
    hours = mins // 60
    day = hours // 24
    print(hours)
    secs = secs % 60
    mins = mins % 60
    hours = hours % 24
    print(day, hours, mins, secs)


main()
