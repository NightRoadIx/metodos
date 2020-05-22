import numpy as np
import sympy as sp

xs = sp.Symbol('x')

# Datos
x = [1, 4, 6, 5]
y = [0, 1.386294, 1.791759, np.log(5)]

# Grado del polinomio
n = len(x) - 1

# Valor a calcular
xc = 2

fnx = 0
for i in range(0, n+1):
    Lix = 1
    for j in range(0,n+1):
        if j == i: continue
        Lix *= ((xs - x[j]) / (x[i] - x[j]))
    fnx += (Lix * y[i])

sp.pretty_print( sp.expand(fnx) )

print("Valor final {:6f}".format( fnx.subs(xs, 2).evalf() ))