'''Meteorite'''
def main():
    '''save the earth'''
    weight = float(input())
    remnant = int(input())
    passive = float(input())
    som = 0
    how = 1
    while True:
        if weight < passive:
            break
        weight /= remnant
        som += how
        how *= remnant
    print(som)
main()
