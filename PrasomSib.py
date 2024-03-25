'PrasomSib'
def main(num):
    way = 0
    length = len(num)
    for i in range(length):
        if int(num[i]) + int(num[i+1]) == 10:
            way += 1
        # if now == 10:
        #     way += 1
    print(way)
main(input())
