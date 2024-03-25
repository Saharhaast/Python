"""Robot I"""
def robot():
    """Robot I"""
    in_1 = str(input())
    in_2 = float(input())
    if in_2 < 18:
        print("%s, you can pass."%in_1)
    else:
        print("%s, you shall not pass."%in_1)
robot()
