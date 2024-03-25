"""FR2"""
def fibonacci(num):
    """FibonacciRecursionV1"""
    if num in {0, 1}:  # Base case
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
def main():
    """FibonacciRecursionV1"""
    print((fibonacci(int(input()))))
main()
