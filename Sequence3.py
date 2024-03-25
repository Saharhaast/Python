"""Sequence III"""
def main():
    """Sequence"""
    num = int(input())
    for i in range(2, num + 2):
        for j in range(i, i + num):
            print(j, end=' ')
        print()
main()
