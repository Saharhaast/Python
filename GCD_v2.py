"""Ejudge"""
def main(numa, numb):
    """GCD_v2"""
    if numb == 0:
        return numa
    else:
        return main(numb, numa % numb)
print(main(int(input()), int(input())))
