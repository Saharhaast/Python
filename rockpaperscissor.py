
input_str = input()
score_a = 0
score_b = 0
rounds = len(input_str)
for i in range(rounds):
    move_a = input_str[i]
    move_b = input_str[(i + 1) % rounds]

    if (move_a == 'R' and move_b == 'P') or (move_a == 'S' and move_b == 'R') or (move_a == 'P' and move_b == 'S'):
        score_b += 1
    elif (move_a == 'P' and move_b == 'R') or (move_a == 'R' and move_b == 'S') or (move_a == 'S' and move_b == 'P'):
        score_a += 1
if score_a > score_b:
    print(f"A WIN {score_a}-{score_b}")
elif score_b > score_a:
    print(f"B WIN {score_b}-{score_a}")
else:
    print(f"DRAW {score_a}-{score_b}")

