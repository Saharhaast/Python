"""Point and Click"""
def is_inside_circle(xxx, yyy, rrr, xnn, ynn):
    """Easy Gameplay"""
    xxx = float(input())
    yyy = float(input())
    rrr = float(input())
    xnn = float(input())
    ynn = float(input())
    rst = is_inside_circle(xxx, yyy, rrr, xnn, ynn)
    print(rst)
    distance_squared = (xnn - xxx)**2 + (ynn - yyy)**2
    return distance_squared <= rrr**2
