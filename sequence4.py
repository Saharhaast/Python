"""Sequence IV"""
def main():
    """Sequence"""
    num = int(input())
    start = 1
    for _ in range(num):
        for _ in range(num):
            print(start, end=' ')
            start += 1
        print()
main()
