"""Idol"""
def main():
    """Fully pair"""
    word = input().lower()
    tmp = ""
    nopair = ""
    count = 0
    for app in word:
        if tmp.count(app) <= 0:
            tmp += app
    for app in tmp:
        if word.count(app) % 2 != 0:
            nopair += app
            count += 1
    if count == 0:
        print("fully paired")
    else:
        print(nopair)
main()
