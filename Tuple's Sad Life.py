"""Life is Always Sad"""
def main():
    """Tuple's Sad life"""
    tup = tuple(input().split())
    tmp = input()
    num = tup.count(tmp)
    point = tup.index(tmp)
    for _ in range(num):
        for _ in range(num):
            print(point, end=" ")
        print()
main()
