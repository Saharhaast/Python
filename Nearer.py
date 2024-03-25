"""Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    ice_cream = int(input())
    alice_distance = abs(ice_cream - alice)
    bob_distance = abs(ice_cream - bob)
    if alice_distance < bob_distance:
        print("Alice", alice_distance)
    elif bob_distance < alice_distance:
        print("Bob", bob_distance)
    else:
        print("Sundaes", alice_distance)
main()
