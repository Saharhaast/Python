"""Primus"""
import math
def main():
    """isPrime_large"""
    num = int(input())
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
main()
