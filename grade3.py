"""Grade"""
def main():
    """the third"""
    num = abs(int(input()))
    total_grade = 0
    for _ in range(num):
        score = abs(float(input()))
        if 0 <= score <= 100:
            if 95 <= score <= 100:
                total_grade += 4
            elif 90 <= score < 95:
                total_grade += 3.5
            elif 85 <= score < 90:
                total_grade += 3
            elif 80 <= score < 85:
                total_grade += 2.5
            elif 75 <= score < 80:
                total_grade += 2
            elif 70 <= score < 75:
                total_grade += 1.5
            elif 65 <= score < 70:
                total_grade += 1
            elif 60 <= score < 65:
                total_grade += 0.5
            elif 0 <= score < 60:
                total_grade += 0
    your_grade = total_grade / num
    print("%.2f"%your_grade)
main()
