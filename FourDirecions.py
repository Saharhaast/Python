"""Four"""
def main():
    """Arrow"""
    input_string = input()
    arrows = (
        ["  *  ", " *** ", "* * *", "  *  ", "  *  "],
        ["  *  ", "  *  ", "* * *", " *** ", "  *  "],
        ["  *  ", " *   ", "*****", " *   ", "  *  "],
        ["  *  ", "   * ", "*****", "   * ", "  *  "]
    )
    result = []
    for direction in input_string:
        arrow = arrows["UDLR".index(direction)]
        if not result:
            result = arrow
        else:
            result = [result[i] + " " + arrow[i] for i in range(5)]
    for line in result:
        print(line)

main()
