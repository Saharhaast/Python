# take input from user
max_height = int(input())
num_stairs = int(input())
stairs = [int(input()) for i in range(num_stairs)]
target_height = stairs[-1]

# check if it's possible to climb to the second floor
if max(stairs) > max_height:
    print("NO")
else:
    # climb the stairs
    steps = 0
    current_height = 0
    for i in range(num_stairs):
        current_height += stairs[i]
        if current_height > max_height:
            steps += 1
            current_height = stairs[i]
    if current_height > 0 and current_height <= max_height:
        steps += 1

    # print the minimum number of steps required
    print(steps)
