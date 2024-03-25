"""FreetoPlay"""
def main():
    """Fever"""
    temp = float(input())
    if temp >= 40:
        print("Very High Fever")
    elif temp >= 39:
        print("High Fever")
    elif temp >= 38:
        print("Mild Fever")
    else:
        print("No Fever")
main()
