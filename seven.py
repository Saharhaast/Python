"""seven"""
def main(num0, num1, num2):
    """seven"""
    if num1 == 0:
        return 1
    if num1 == 1:
        return num0 % num2
    half_exponent = num1 // 2
    half_result = main(num0, half_exponent, num2)
    result = (half_result * half_result) % num2
    if num1 % 2 == 1:
        result = (result * (num0 % num2)) % num2
    return result

mil = int(input())
result = main(7, mil, 10)
print(result)
