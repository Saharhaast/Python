"""Wat??"""
def main():
    """PickThemAgain"""
    num = input().split()
    anslist = []
    for i in num:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            anslist.append(int(i))
    if anslist == []:
        print("Nope")
    for i in anslist[::-1]:
        print(i)
main()
