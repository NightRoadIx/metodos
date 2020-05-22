import sympy as sp

x = sp.Symbol('x')
f = 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
sp.plotting.plot(f, xlim = [-0.1, 0.81], ylim = [0,4])

n = 10
a = 0.0
b = 0.8

xi = []
sumar = 0
for i in range(1, n):
    xi.append( (i)*(b-a)/n )
    sumar += f.subs(x, (i)*(b-a)/n ).evalf()

Res = (b-a) * ( (f.subs(x,a).evalf() + 2*sumar + f.subs(x,b).evalf() )/(2*n) )

print("Resultado: ", Res)
print("Real     : ", sp.integrate(f, (x, 0, 0.8)))