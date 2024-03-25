"""WSI"""
def main():
    """WordSequence I"""
    word = input()
    for i in range(len(word)):
        print(word[:i+1])
main()
