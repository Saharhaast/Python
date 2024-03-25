"""Ejudge"""
def main():
    """Kayak"""
    num = int(input())
    people = input().split()
    people = list(map(int, people))
    people.sort()
    weight = []
    for i in range((num*2)-1):
        weight.append(people[i+1] - people[i])
    weight.sort()
    tmp = 0
    for i in range(len(weight)-2):
        tmp += weight[i]
    print(tmp)
main()
