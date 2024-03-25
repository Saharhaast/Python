"""Phone"""
def main():
    """Number"""
    phone = input()
    country = input()
    if country == "International":
        print("+66"+phone[1:-8], phone[-8:-4], phone[-4:])
    else:
        print(phone[:-8], phone[-8:-4], phone[-4:])
main()
