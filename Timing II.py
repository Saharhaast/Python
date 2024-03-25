"""time"""
def time(sec1):
    """time"""
    days1 = sec1 // (24 * 60 * 60)
    sec1 %= 24 * 60 * 60
    hours1 = sec1 // (60 * 60)
    sec1 %= 60 * 60
    minutes1 = sec1 // 60
    sec1 %= 60
    if days1 > 9999 or hours1 > 99 or minutes1 > 59 or sec1 > 59:
        return "ERR_:__:__:__"
    time = "%04d:%02d:%02d:%02d" % (days1, hours1, minutes1, sec1)
    return time
sec2 = int(input())
num = time(sec2)

print(num)
