"""MyMath"""
def main():
    """MyMath"""
    import math
    sin = math.sin
    cos = math.cos
    rad = math.radians
    sqrt = math.sqrt
    fac = math.factorial
    log = math.log
    log10 = math.log10
    sin90 = sin(rad(90))
    sin60 = ((sin(rad(60)))**2)
    cos245 = cos(rad(245**2))
    cos180 = cos(rad(145+35))
    hard_1 = log(4234, 5) + log(8191, 2) + (71 * log10(156154))
    hard_2 = log(777, 7) - log(888, 8) - log(999, 9)
    answer = ((sin90) + (sin60)) / ((cos245) + (cos180))
    print(answer)
    print((fac(16) * fac(4)) / fac(8))
    print((40) / (sqrt(178)))
    print(log10(1234 ** 4))
    print(hard_1 / hard_2)
main()
