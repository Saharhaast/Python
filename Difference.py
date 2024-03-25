"""TopDiff"""
def main():
    """Difference"""
    numseta = int(input())
    numsetb = int(input())
    seta = set()
    setb = set()
    for _ in range(numseta):
        seta.add(int(input()))
    for _ in range(numsetb):
        setb.add(int(input()))
    for i in sorted(seta.difference(setb)):
        print(i, end=" ")
main()
