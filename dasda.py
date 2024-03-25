"""How"""
def main():
    """Long"""
    num = int(input())
    if num < 10:
        print(1)
    elif 10 < num < 100:
        print(2)
    elif 100 < num < 1000:
        print(3)
    elif 1000 < num < 10000:
        print(4)
    elif 10000 < num < 100000:
        print(5)
    elif 100000 < num < 1000000:
        print(6)
    elif 1000000 < num < 10000000:
        print(7)
    elif 10000000 < num < 100000000:
        print(8)
    elif 100000000 < num < 1000000000:
        print(9)
    elif 1000000000 < num < 10000000000:
        print(10)
    else:
        print(11)
main()
