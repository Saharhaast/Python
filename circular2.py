"""Circular"""
def main():
    """cricket"""
    my_x = float(input())
    my_y = float(input())
    my_radius = float(input())
    friend_x = float(input())
    friend_y = float(input())
    friend_radius = float(input())
    distance = ((my_x - friend_x)**2 + (my_y - friend_y)**2)**0.5
    if distance < abs(my_radius + friend_radius):
        result = "Yes"
    else:
        result = "No"
    print(result)
main()
