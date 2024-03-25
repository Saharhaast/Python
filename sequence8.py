"""Sequence VIII"""
def main():
    """Sequence"""
    num = int(input())
    for i in range(1, num+1):
        row = ""
        for j in range(1, i+1):
            row += "{:02d} ".format(j)
        row = row.rjust(num*3)
        print(row)
main()
