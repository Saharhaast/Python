"""LondonBridgeisFallingDown"""
def main():
    """Heads and Legs"""
    num = int(input())
    leg = int(input())
    rabbit, nohave = divmod(leg-2 * num, 2)
    bird = num - rabbit
    if rabbit >= 0 and bird >= 0 and nohave == 0:
        print(rabbit, bird)
    else:
        print("Impossible")
main()
