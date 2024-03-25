"""The_Matrix"""
def main():
    """Matrix_MN"""
    sizem = int(input())
    sizen = int(input())
    tmp = ""
    for _ in range(sizem):
        for _ in range(sizen):
            tmp += input()+" "
        print(tmp)
        tmp = ""
main()
