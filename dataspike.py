"""dataspike"""
def dataspike():
    """dataspike"""
    a_a = int(input())
    b_b = int(input())
    c_c = int(input())
    d_d = int(input())
    e_e = int(input())
    f_f = int(input())
    g_g = int(input())
    h_h = int(input())
    a_b = a_a if a_a > b_b else b_b
    c_d = c_c if c_c > d_d else d_d
    e_f = e_e if e_e > f_f else f_f
    g_h = g_g if g_g > h_h else h_h
    ab_cd = a_b if a_b > c_d else c_d
    ef_gh = e_f if e_f > g_h else g_h
    highest = ab_cd if ab_cd > ef_gh else ef_gh
    print(highest)

dataspike()
