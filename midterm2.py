"""bad"""
def sub(s):
    """worse"""
    count = 0
    for char in s:
        if char == '1':
            count += 1
    return count
def main(num, msg):
    """worst"""
    num_ones = sub(num)
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
