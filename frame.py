"""Frame"""
def main():
    """Rate"""
    text = input()
    border_length = len(text) + 2
    top_border = '*' * border_length
    print(top_border)
    print("*", text, "*", sep="")
    print(top_border)
main()
