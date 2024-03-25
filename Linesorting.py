"""SORTING"""
def main():
    """LineSorting"""
    line = int(input())
    wordlist = []
    for i in range(line):
        wordlist.append(input())
    wordlist.sort(key=len)
    for i in range(len(wordlist)):
        print(wordlist[i])
main()
