import matplotlib.pyplot as plt
import numpy as np

dia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20,21,22,23,24,25,26,27,28,29,30,31,32]
casos = [3,4,5,5,5,5,5,6,7,7,7,7,11,15,26,41,53,82,93,118,164,203,251,316,367,405,475,585,717,848,993,1094]

dia = np.array(dia)
casos = np.array(casos)

plt.plot(dia, casos, ".")
plt.title('Casos Khareanoviro')
plt.xlabel('# Día')
plt.ylabel('# Casos')
plt.grid()
plt.show()

ln_casos = np.log(casos)

plt.plot(dia, ln_casos, ".")
plt.title('Casos Khareanoviro')
plt.xlabel('# Día')
plt.ylabel('ln(# Casos)')
plt.grid()
plt.show()

plt.semilogy(dia, casos, ".", color = "red")
plt.title('Casos Khareanoviro')
plt.xlabel('# Día')
plt.ylabel('ln(# Casos)')
plt.grid()
plt.show()

# Datos
n = float(len(dia))
sumxi = float(np.sum(dia))
sumyi = float(np.sum(ln_casos))
sumxiyi = float(np.sum(dia * ln_casos))
sumxi2 = float(np.sum( dia**2 ))
xmed = np.mean(dia) 
ymed = np.mean(ln_casos)

a1 = (n*sumxiyi - (sumxi*sumyi))/(n*sumxi2 - (sumxi**2))
a0 = ymed - a1*xmed

x = np.linspace(0, n, 60)
y = a0 + a1*x

plt.plot(x, y, color="black")
plt.plot(dia, ln_casos, ".")
plt.title('Casos Khareanoviro')
plt.xlabel('# Día')
plt.ylabel('ln(# Casos)')
plt.grid()
plt.show()

print("a0: ", a0)
print("a1: ", a1)

yor = np.exp(a0)*np.exp(a1*x)

plt.plot(x, yor, color="black")
plt.plot(dia, casos, ".")
plt.title('Casos Khareanoviro')
plt.xlabel('# Día')
plt.ylabel('# Casos')
plt.grid()
plt.show()

print("alfa: ", np.exp(a0))
print("beta: ", a1)