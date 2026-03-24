"""
Hacer el programa del método de bisección con la ecuación f(x)=x^3-5
1.- Definir la función f(x)
2.-Imprimir la gráfica de la función
3.- Pedir la usuario el intervalo [a,b] 
4.- Limitar dentro del mismo programa la tolerancia a 0.00001
5.- Imprimir el resultado de la aproximación de la raíz, el número de interaciones y el error absoluto y relativo
"""

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk 

def f(x):
    return x**3 - 5

#Imprimir la gráfica

x = np.linspace(-2, 2, 100)
y = f(x)
plt.plot(x,y)
plt.axhline(0, color='red', lw=0.5)
plt.title('Gráfica de f(x) = x^3 - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

#Pedir al usuario el intervalo [a,b] depués de ver la gráfica
a = float(input("Ingrese el primer valor del intervalo: "))
b = float(input("Ingrese el segundo valor del intervalo: "))

#Limitar la tolerancia
tolerancia = 0.00001

#Haciendo el metodo de bisección
#Asegurarse de que f(a) y f(b) tengan signos opuestos para f(a)*f(b) < 0
if f(a) * f(b) >= 0:
    print("El método de bisección no se puede aplicar. f(a) y f(b) deben tener signos opuestos.")
else:
    
    #Proceso de bisección
    #definir la cantidad de iteraciones para la aproximación 
    iteraciones = 0 
    while True:
        iteraciones += 1
        x1 = (a + b) / 2 #punto medio de mi intervalo 
        #si el punto medio es raíz exacta hay que detener el proceso
        if f(x1) == 0:
            print(f"La raíz exacta es: {x1}")
            break
        #si no es raíz exacta, hay que encontrar el nuevo intervalo
        elif f(a) * f(x1) < 0:
            b = x1
        else:
            a = x1
            
            #Calcular el error absoluto
            error_absoluto = abs(a - b)
            #Calcular error relativo
            error_relativo = error_absoluto / abs(x1) if x1 != 0 else float('inf')
            
            #Imprimir el resultado de la aproximación de la raíz, cuantas iteraciones se hicieron y los errores.
            print(f"Aproximación de la raíz: {x1}")
            print(f"Número de iteraciones: {iteraciones}")
            print(f"Error absoluto: {error_absoluto}")
            print(f"Error relativo: {error_relativo}") 
            
            
"""
Hay que hacer una tabla donde aparezca el número de iteraciones, el rango utilizado, la aproximación de la raíz, 
los errores de cada iteración y al final dar la aproximacion final de la raíz como resultado del programa
Hacer que el programa regrese de nuevo a escoger un rango si el rango escogido por el usuario no contiene la raíz.
Programar para que no tengas que cerrar la grafica cada vez que quieras escoger el rango
Si se puede entregar el programa con interfaz gráfica con tkinter (no tenga que leer la terminal)

"""