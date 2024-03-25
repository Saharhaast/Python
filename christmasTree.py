"""Chris"""
def main():
    """ChristmasTree"""
    leaf = int(input())
    tree = int(input())
    for i in range(1, leaf + 1):
        print(" "*(leaf - i) + "*"*(2*i - 1))
    for i in range(tree):
        print(" "*(leaf-2) + "-"*3)
main()
