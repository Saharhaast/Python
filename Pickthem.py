"""PickThey"""
import json
def main():
    """PickThem"""
    num = json.loads(input())
    numeven = 0
    for i in num:
        if i % 2 == 0:
            print(i)
            numeven += 1
    if numeven == 0:
        print("Nope")
main()
