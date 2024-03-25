'iPad Air'
def checkmem(connect):
    'check 64'
    if connect == 'Wi-Fi':
        print(19900)
    elif connect == 'Wi-Fi + Cellular':
        print(24400)
    else:
        print('Not Available')
def checkmem2(connect):
    'check 256'
    if connect == 'Wi-Fi':
        print(24900)
    elif connect == 'Wi-Fi + Cellular':
        print(29400)
    else:
        print('Not Available')
def main(color, mem, connect):
    'iPad Air'
    if color == 'Space Gray' or color == 'Silver' or \
        color == 'Green' or color == 'Rose Gold' or color == 'Sky Blue':
        if mem == 64:
            checkmem(connect)
        elif mem == 256:
            checkmem2(connect)
        else:
            print('Not Available')
    else:
        print('Not Available')
main(input(), int(input()), input())
