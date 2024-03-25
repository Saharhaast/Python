"""Sataramp"""
def main():
    """Stamps"""
    time = int(input())
    billtostamp = int(input())
    stampup = int(input())
    sasomtopro = int(input())
    pro = int(input())
    stamp = 0
    bill = 0
    for _ in range(time):
        price = int(input())
        if stamp >= sasomtopro:
            rounddis = price // pro
            if price % pro > 0:
                rounddis += 1
            tmp = stamp // sasomtopro
            can = min(rounddis, tmp)
            if can > 0:
                price -= can * pro
                price = max(price, 0)
                stamp -= can * sasomtopro
        if price >= billtostamp:
            stamp += (price//billtostamp)*stampup
        bill += price
    print(bill)
    print(stamp)
main()
