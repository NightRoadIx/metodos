import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

def tritop(f, a, b, n):
    xi = []
    sumar = 0
    for i in range(1, n):
        xi.append( a + ((i)*((b-a)/n)) )
        sumar += f.subs(x, xi[i-1] ).evalf()

    Res = (b-a) * ( (f.subs(x,a).evalf() + 2*sumar + f.subs(x,b).evalf() )/(2*n) )
    return Res


# Ingresar ecuaciones
x = sp.Symbol('x')
y1 = x**2 + 1
y2 = x + 3

print('Las ecuaciones: ')
sp.pretty_print(y1)
sp.pretty_print(y2)

# Encontrar los puntos donde se intersectan
# Resolver la ecuación y1 = y2
print("Ecuación a resolver: ")
sp.pretty_print(y1-y2)
print("Soluciones: ")
xsols = sp.solve(y1-y2)
print("x1 = ", xsols[0], " x2 = ", xsols[1])

# Mostrar las gráficas en 2D
xs = np.linspace(float(xsols[0]), float(xsols[1]), 60)
ys1 = (xs**2 + 1)
ys2 = (xs + 3)
plt.plot(xs, ys1)
plt.plot(xs, ys2)
plt.grid()
plt.show()

# Mostrar los sólidos de revolución
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1, projection='3d')

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1, projection='3d')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

u = xs
v = np.linspace(0, 2*np.pi, 60)
U, V = np.meshgrid(u, v)

X = U
Y1 = (U**2 + 1)*np.cos(V)
Z1 = (U**2 + 1)*np.sin(V)

Y2 = (U + 3)*np.cos(V)
Z2 = (U + 3)*np.sin(V)


ax1.plot_surface(X, Y1, Z1, color='red')
ax2.plot_surface(X, Y2, Z2, color='blue')

ax.plot_surface(X, Y1, Z1, alpha=0.5, color='red', rstride=6, cstride=12)
ax.plot_surface(X, Y2, Z2, alpha=0.3, color='blue', rstride=6, cstride=12)

n = 50
V1 = float(  np.pi * tritop( y1**2, float(xsols[0]), float(xsols[1]), n ))
print("Volumen 1: ", round(V1,4))
V2 = float(  np.pi * tritop( y2**2, float(xsols[0]), float(xsols[1]), n ))
print("Volumen 2: ", round(V2,4))
print("Volumen Total: ", round(V2-V1,4))

print("Valor analítico: ", round(sp.integrate(np.pi * y2**2, (x, float(xsols[0]), float(xsols[1]))) - sp.integrate(np.pi * y1**2, (x, float(xsols[0]), float(xsols[1]))),4) )



