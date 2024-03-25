"""CoinKing"""
def main():
    """CoinChangev1"""
    change = int(input())
    ans = 0
    ans += change//25
    change = change%25
    ans += change//10
    change = change%10
    ans += change//5
    change = change%5
    ans += change//1
    print(ans)
main()
