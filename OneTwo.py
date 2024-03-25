"""Left-Right"""
def cal(num):
    """cal"""
    if num in {1}:
        return "1"
    elif num in {2}:
        return "2"
    return cal(num-1) + cal(num-2)
def main():
    """OneTwo"""
    print(cal(int(input())))
main()
