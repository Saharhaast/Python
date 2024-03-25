"""FOR!F-Ball"""
def main():
    """FOR!F-Ball"""
    moveball = input()
    pointball = 1
    for move in moveball:
        if move == "A":
            if pointball == 1:
                pointball = 2
            elif pointball == 2:
                pointball = 1
        elif move == "B":
            if pointball == 2:
                pointball = 3
            elif pointball == 3:
                pointball = 2
        elif move == "C":
            if pointball == 1:
                pointball = 3
            elif pointball == 3:
                pointball = 1
    print(pointball)
main()
