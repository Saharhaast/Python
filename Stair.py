"""STAIR"""
def main():
    """STAR"""
    height = int(input())
    num = int(input())
    stairs = [int(input()) for _ in range(num)]
    if max(stairs) > height:
        print("NO")
    else:
        steps = 0
        current = 0
        for i in range(num):
            current += stairs[i]
            if current > height:
                steps += 1
                current = stairs[i]
        if current > 0 and current <= height:
            steps += 1
        print(steps)
main()
