"""Sequence IX"""
def main():
    """Sequence"""
    rows = int(input())
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print("  ", end=" ")
        for j in range(1, i + 1):
            print("%02d"%j, end=" ")
        for j in range(i - 1, 0, -1):
            print("%02d"%j, end=" ")
        print()
main()
