"""Suprise"""
def check_surprising(ano_score1, max_score):
    """Word"""
    if max_score - ano_score1 > 2:
        return "Surprising"
    elif diff_score1/2 - max_score <= 2:
        return "Not surprising"
total_score = abs(float(input()))
max_score = abs(float(input()))
diff_score = total_score - max_score
diff_score1 = abs(diff_score)
ano_score = diff_score - max_score
ano_score1 = abs(ano_score)
result = check_surprising(ano_score1, max_score)
print(result)
