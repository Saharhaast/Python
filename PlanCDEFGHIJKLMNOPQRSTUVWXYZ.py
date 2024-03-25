"""mod"""
def main():
    """mad"""
    option = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if option == "Ascend":
        if num1 <= num2 <= num3:
            result = f"{num1:.2f}, {num2:.2f}, {num3:.2f}"
        elif num1 <= num3 <= num2:
            result = f"{num1:.2f}, {num3:.2f}, {num2:.2f}"
        elif num2 <= num1 <= num3:
            result = f"{num2:.2f}, {num1:.2f}, {num3:.2f}"
        elif num2 <= num3 <= num1:
            result = f"{num2:.2f}, {num3:.2f}, {num1:.2f}"
        elif num3 <= num1 <= num2:
            result = f"{num3:.2f}, {num1:.2f}, {num2:.2f}"
        else:
            result = f"{num3:.2f}, {num2:.2f}, {num1:.2f}"
    elif option == "Descend":
        if num1 >= num2 >= num3:
            result = f"{num1:.2f}, {num2:.2f}, {num3:.2f}"
        elif num1 >= num3 >= num2:
            result = f"{num1:.2f}, {num3:.2f}, {num2:.2f}"
        elif num2 >= num1 >= num3:
            result = f"{num2:.2f}, {num1:.2f}, {num3:.2f}"
        elif num2 >= num3 >= num1:
            result = f"{num2:.2f}, {num3:.2f}, {num1:.2f}"
        elif num3 >= num1 >= num2:
            result = f"{num3:.2f}, {num1:.2f}, {num2:.2f}"
        else:
            result = f"{num3:.2f}, {num2:.2f}, {num1:.2f}"
    print(result)
main()
