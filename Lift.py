n = int(input())
max_weight = float(input())

total_weight = 0
has_adult = False

for i in range(n):
    age = int(input())
    weight = float(input())
    if age < 12:
        if has_adult == False:
            print("Not Safe")
            break
    else:
        has_adult = True
    total_weight += weight
