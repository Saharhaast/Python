"""LastMan"""
import json
def main():
    """LastStand"""
    numlist = json.loads(input())
    for i in numlist:
        print(str(i)[-1])
main()
