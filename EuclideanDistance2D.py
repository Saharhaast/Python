"""euclidean_distance"""
def euclidean_distance(variable1, in2, nm1, nm2):
    """euclidean_distance"""
    distance = ((variable1 - nm1) ** 2 + (in2 - nm2) ** 2) ** 0.5
    return distance
variable1 = float(input())
in2 = float(input())
nm1 = float(input())
nm2 = float(input())
end = euclidean_distance(variable1, in2, nm1, nm2)
print(end)
