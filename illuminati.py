def illuminatinum():
    num = int(input())
    illulist = [333, 666, 777, 888]
    if num % 3 == 0:
        print("It's maybe Illuminati")
    elif num % 13 == 0:
        print("It's could be Illuminati")
    
    if num == 3 or num == 13:
        print("Illuminati Confirm")
    elif num in illulist:
        print("Illuminati Confirm!!!")
    else:
        print("It's not illuminati")
illuminatinum()
