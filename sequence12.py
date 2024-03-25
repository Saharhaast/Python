"""Sequence XII"""
def main():
    """Sequence"""
    box = int(input())
    for i in range(-box + 1, box, 1):
        for j in range(-box + 1, box, 1):
            if abs(i) > abs(j) - 1:
                print("%02d" %(box - abs(i)), end=" ")
            else:
                print("%02d" %(box - abs(j)), end=" ")
        print()
main()
