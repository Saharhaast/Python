"""composfunct"""
def funct(fxt):
    """copofut"""
    return 2 * fxt
def gunct(fxt):
    """copofut"""
    return fxt / 2 + 1
fxt = float(input())
fgx = funct(gunct(fxt))
print('%.2f'%fgx)
gfx = gunct(funct(fxt))
print('%.2f'%gfx)
