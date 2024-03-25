"""Celsiusvsfahrenhite?"""
def main(temp, tempnow, tempnew):
    """[Recommend] Temperature"""
    if tempnow == "C":
        tempcel = temp
    elif tempnow == "F":
        tempcel = (temp-32)*(5/9)
    elif tempnow == "K":
        tempcel = temp-273.15
    elif tempnow == "R":
        tempcel = (temp*5/9)-273.15
    tempnewval = tempcel
    if tempnew == "F":
        tempnewval = (tempcel*(9/5))+32
    elif tempnew == "K":
        tempnewval = tempcel+273.15
    elif tempnew == "R":
        tempnewval = (tempcel+273.15)*(9/5)
    print("%.2f" % (tempnewval))
main(float(input()), input(), input())
