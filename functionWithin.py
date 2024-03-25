def f(x):
    return 2 * x
def g(x):
    return 3 * x**4 - x**3 + 2 * x**2 + 10
def h(x, y, z):
    return (z + x)**2 - x * y + y**2
def i(a, b, c, d):
    return ((a**2) + (b**2) - (c**2)) / ((d**2) - (2 * a * d) + (2*a))
a = float(input())
b = float(input())
c = float(input())
d = float(input())
output_f = f(f(a))
output_g = g(f(a - b))
output_h = h(f(a + b), f(a + c), g(f(d**2)))
output_i = i(h(f(a + b), f(a - c), g(f(d**2))), g(f(a - b)), f(f(f(f(f(c))))), d**8)

print(output_f)
print(output_g)
print(output_h)
print(output_i)
