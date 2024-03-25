"""grader"""
def main():
    """machinegunblow"""
    start_weight = abs(int(input()))
    end_weight = abs(int(input()))
    pass_weights = ""
    total_weight = 0
    number = start_weight
    while number <= end_weight:
        if number % 2 == 0:
            pass_weights += str(number) + " "
            total_weight += number
        number += 1
    else:
        while number > end_weight:
            if number % 2 == 0:
                pass_weights += str(number) + " "
                total_weight += number
            number -= 1
    print("pass :", pass_weights)
    print("Sum:", total_weight)
main()
