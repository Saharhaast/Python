"""Histogranum"""
def main():
    """VerticalHistogram"""
    text = input()

    alpa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = {}
    for alpha in alpa:
        result[alpha] = 0
        for char in text:
            if char == alpha:
                result[alpha] += 1

    maximum = result[max(result, key=result.get)]
    for count in range(maximum, 0, -1):
        print("%03d" %count, end='')
        for alpha in alpa:
            if result[alpha] >= count and result[alpha] != 0:
                print(" *", end='')
            elif result[alpha] == 0:
                continue
            else:
                print("  ", end='')
        print()
    print(" " * 3, end='')
    for alpha in alpa:
        if result[alpha] != 0:
            print(" %s" %alpha, end='')
main()
