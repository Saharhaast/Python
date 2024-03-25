"""Medium"""
def main():
    """Median"""
    num = int(input())
    scorelist = []
    for _ in range(num):
        tmp = int(input())
        scorelist.append(tmp)
    scorelist.sort()
    if num % 2 != 0:
        print("%.1f" % scorelist[(num//2)])
    else:
        print("%.1f" % ((scorelist[(num//2)-1]+scorelist[(num//2)])/2))
main()
