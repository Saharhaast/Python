"""Katana"""
def main():
    """Kabata"""
    numword = int(input())
    for _ in range(numword):
        word = input().replace("baka", "no").replace("bakka", "")\
.replace("ka", "").replace("ta", "").replace("ba", "")
        if word == "":
            print("yes")
        else:
            print("no")
main()
