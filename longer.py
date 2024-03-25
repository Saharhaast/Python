"""longer"""
def main():
    """Nolonger"""
    import math
    rrr = abs(float(input()))
    aaa = abs(float(input()))
    bbb = abs(float(input()))
    circle = 2 * math.pi * rrr
    square = (aaa+bbb)*2
    the_diff = abs(square - circle)
    if circle > square:
        print("Circle is longer")
        print("%.5f"%the_diff)
    elif circle < square:
        print("Rectangle is longer")
        print("%.5f"%the_diff)
    else:
        print("Equal")
        print("%.5f"%the_diff)
main()
