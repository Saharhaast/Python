def check_weight_balance(avg_weight, weights):
    max_total_weight = 15000  
    max_deviation = avg_weight / 2  
    missing_weight = round(4 * avg_weight - sum(weights), 2)
    total_weight = sum(weights)
    if total_weight > max_total_weight-1700:
        return "Overweight"

    for w in weights:
        if abs(w - avg_weight) > max_deviation:
            return "Unbalance"

    return "Pass %.2f"%missing_weight

avg_weight = abs(float(input()))
weights = [abs(float(input())) for _ in range(3)]
result = check_weight_balance(avg_weight, weights)
print(result)

