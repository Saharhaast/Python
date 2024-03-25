'''Calculator'''
def cal():
    '''Calculator'''
    num = int(input())
    final = '1'
    if num != 1:
        for i in range(2, num+1):
            final += '+'+str(i)
        print(len(final)+1)
    else:
        print(1)
cal()
