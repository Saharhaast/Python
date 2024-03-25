"""Valid"""
def main():
    """Variety"""
    people = int(input())
    for _ in range(people):
        name = input()
        if name.isidentifier() and (name != "if" \
        and name != "else" and name != "elif" and name != "for" and name != "while" \
        and name != "True" and name != "False" and name != "continue" and name != "break" \
        and name != "return" and name != "is" and name != "in" and name != "and" and name != "or" \
        and name != "from" and name != "as" and name != "pass" and name != "not" and name != "def" \
        and name != "None"):
            print("Valid")
        else:
            print("Invalid")
main()
