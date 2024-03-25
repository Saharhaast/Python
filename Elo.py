"""Elo"""
def main():
    """LOW-HiGH"""
    ra_ = int(input())
    rb_ = int(input())
    player = input()
    if player == "A":
        ea_ = 1 / (1 + 10**((rb_ - ra_) / 400))
        print("%.2f"%ea_)
    elif player == "B":
        eb_ = 1 / (1 + 10**((ra_ - rb_) / 400))
        print("%.2f"%eb_)
main()
