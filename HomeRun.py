"""Home"""
def main():
    """Run"""
    num = abs(int(input()))
    distance = abs(float(input()))
    home_run_count = 0
    for i in range(num):
        field_length = abs(float(input()))
        if field_length <= distance:
            home_run_count += 1
        else:
            home_run_count += 0 
    print(home_run_count)
main()
    