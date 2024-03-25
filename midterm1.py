"""midterm"""
def main():
    """midterm"""
    import math
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a + b + c) / 2
    if (s - a) >= 0 and (s - b) >= 0 and (s - c) >= 0:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("%.3f"%area)
    else:
        print("0.000")
main()
