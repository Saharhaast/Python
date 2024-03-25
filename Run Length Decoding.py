"""Run Length Encoding"""
def main():
    """RLECD"""
    decoding = input()
    decoded = ""
    num = ""
    for dec in decoding:
        if dec.isdigit():
            num += dec
        else:
            decoded += dec * int(num)
            num = ""
    print(decoded)
main()
