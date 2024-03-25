"""Key"""
def key():
    """Klee"""
    num = input()
    list_num = [int(i) for i in list(num)]
    last_num = int(num[-3:])
    result = last_num * 10
    sam = (sum(list_num))
    kaleid = (sam+result)
    if kaleid < 1000:
        kaleid += 1000
    elif kaleid >= 10000:
        kaleid %= 10000
    print("%04d"%kaleid)
key()
