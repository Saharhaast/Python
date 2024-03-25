"""Sequence V"""
def main():
    """Sequence"""
    num = int(input())
    for i in range(num, 0, -1):
        print(i, end=' ')
        if (num - i + 1) % 7 == 0:
            print()
main()
