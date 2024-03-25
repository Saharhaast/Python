def illuminatinum(num):
    illulist = [333, 666, 777, 888]
    num = 333
    if num % 3 == 0:
        return "It's maybe Illuminati"
    elif num % 13 == 0:
        return "It's could be Illuminati"
    if num == 3 or num == 13:
        return "Illuminati Confirm"
    elif num in illulist:
        return "Illuminati Confirm!!!"
    else:
        return "It's not illuminati"
    
    