"""Restaurant"""
def main():
    """Restaurant"""
    pricefirst = float(input())
    pricekamnod = float(input())
    pricepercent = (100-float(input()))/100
    priceadd = float(input())
    pricesum = pricefirst+priceadd
    if pricesum >= pricekamnod:
        pricesum = pricesum*pricepercent
    if pricefirst >= pricekamnod:
        pricefirst = pricefirst*pricepercent
    if pricefirst < pricesum:
        print("No %.3f" % (pricesum-pricefirst))
    elif pricefirst > pricesum:
        print("Yes %.3f" % (pricefirst-pricesum))
    else:
        print("Yes")
main()
