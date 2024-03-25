"""Quadrant"""
def main(pt1, pt2):
    """Quadance"""
    if pt1 > 0 and pt2 > 0:
        return "Q1"
    elif pt1 < 0 and pt2 > 0:
        return "Q2"
    elif pt1 < 0 and pt2 < 0:
        return "Q3"
    elif pt1 > 0 and pt2 < 0:
        return "Q4"
    elif pt1 == 0 and pt2 != 0:
        return "Y"
    elif pt1 != 0 and pt2 == 0:
        return "X"
    else:
        return "O"
pt1 = int(input())
pt2 = int(input())
result = main(pt1, pt2)
print(result)
