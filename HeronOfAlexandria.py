"""WhatTheHeck!!!!"""
def main():
    """Heron of Alexandria"""
    numa = float(input())
    numb = float(input())
    numc = float(input())
    nums = (numa+numb+numc)/2
    print("%.3f" % ((nums*(nums-numa)*(nums-numb)*(nums-numc))**0.5))
main()
