"""CIRCULAR"""
def circle1():
    """Circle1"""
    my_x = float(input())
    my_y = float(input())
    radius = float(input())
    mosquito_x = float(input())
    mosquito_y = float(input())
    distance = ((my_x - mosquito_x)**2 + (my_y - mosquito_y)**2)**0.5
    if distance <= radius:
        result = "Yes"
    else:
        result = "No"
    if distance == radius:
        result += ""
    print(result)
circle1()
