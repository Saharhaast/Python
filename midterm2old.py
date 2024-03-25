def main(num, msg):
    num_ones = num.count('1')   
    if msg == 'Even':
        if num_ones % 2 == 1:
            num += '1'
        else:
            num += '0'
    elif msg == 'Odd':
        if num_ones % 2 == 0:
            num += '1'
        else:
            num += '0'   
    return num
num = input()
msg = input()
result = main(num, msg)
print(result)
