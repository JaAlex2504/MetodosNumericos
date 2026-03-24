#limite de: 0.995, 1.016
import matplotlib.pyplot as plt
import numpy as np

# 1. Definir el dominio (rango de x)
x = np.linspace(0.995,1.016) # 

# 2. Definir la función y
y = (x-1) ** 7

# 3. Graficar
plt.plot(x, y)
plt.title("Gráfica de $y = x^2$")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(False) 
plt.show() 


#segunda gráfica

#1. Definir el dominio 
z = np.linspace(0.995,1.016)

#2. Funcion g 
g = (z**7 - 7*z**6 + 21*z**5 - 35*z**4 + 35*z**3 -21*z**2 + 7*z -1)

#3. Graficar 
plt.plot(z,g)
plt.title("Grafica de funcion")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(False)
plt.show()