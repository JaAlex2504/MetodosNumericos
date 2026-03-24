#En este código hay que hacer que el usuario meta una ecuación y que se defina su aproximación, error absoluto y relato de la última iteración.



import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


#crear la ventana de tkinter
ventana = tk.Tk()
ventana.title('Porgrama para encontrar las raíces de un polinomio mediante el método de bisección')

#Aqui le pido al usuario que ingrese la función

def f(x):
    return eval(funcion.get())

funcion=tk.Entry(ventana, width=50)
funcion.pack()


#antes de mostrar la gráfica hay que limiarla por si se ingresa una nueva ecuación
def limpiar_grafica():
    plt.clf()

#Hacer la gráfica de la función
def grafica():
    x = np.linspace(-10, 10, 400)
    y = f(x)
    plt.plot(x,y, label='f(x)')
    plt.axhline(0, color='blue', lw=0.5, ls='')
    plt.axvline(0, color='blue', lw=0.5, ls='')
    plt.title(f'Gráfica de f(x) = {funcion.get()}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.legend()
    plt.show()
    
#hacer el boton de la gráfica para mostrarla
boton_grafica = tk.Button(ventana, text='Mostrar gráfica', command=lambda: [limpiar_grafica(), grafica()])
boton_grafica.pack()

#Pedir valores de a y b
label_a = tk.Label(ventana, text='Ingrese el valor de a:')
label_a.pack()
entry_a = tk.Entry(ventana)
entry_a.pack()
label_b = tk.Label(ventana, text='Ingrese el valor de b:')
label_b.pack()
entry_b =tk.Entry(ventana)
entry_b.pack()

#Pedir la tolerancia
label_tol = tk.Label(ventana, text='Ingrese la tolerancia (debe ser un valor mayor a 0 y menor a 1):')
label_tol.pack()
entry_tol = tk.Entry(ventana)
entry_tol.pack()

#Pedir el número máximo de iteraciones
label_iter = tk.Label(ventana, text='Ingrese el número máximo de iteraciones:')
label_iter.pack()
entry_iter = tk.Entry(ventana)
entry_iter.pack()

#hacer el metodo de bisección
def biseccion():

    
    a = float(entry_a.get())
    b = float(entry_b.get())
    tol = float(entry_tol.get())
    max_iter = int(entry_iter.get())
    
    resultado = tk.Label(ventana, text='')
    resultado.pack()
    
    if f(a) * f(b) >= 0:
        resultado.config(text='Error: f(a) y f(b) deben tener signos opuestos.', fg='orange')
        return
    
    iter_count = 0
    while iter_count < max_iter:
        c = a + (b - a) / 2
         #Calcular el error absoluto y relativo
        error_absoluto = abs(b - a)
        error_relativo = error_absoluto / abs(c) if c != 0 else float('inf')   
        
        if abs(f(c)) < tol:
            break
        
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
        
       
                  
    resultado.config(text=f'La raiz aproximada es: {c} después de {max_iter} iteraciones. \nError absoluto: {error_absoluto} \nError relativo: {error_relativo}',fg='green')
    
#Botón para ejecutar el método
boton_biseccion = tk.Button(ventana, text='Ejecutar método de bisección', command=biseccion)
boton_biseccion.pack()  


ventana.mainloop()


        



