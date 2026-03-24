import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk 

#Definir la función para el metodo de biseccion 
def f(x):
    return x**3 - 5

#abrir la ventana de tkinter para mostrar la gráfica y pedir el intervalo
root = tk.Tk()
root.title("Programa para encontrar la raíz de f(x) = x^3 - 5 mediante el método de bisección")

def mostrar_grafica():
    #Imprimir la gráfica de la función
    x = np.linspace(-2, 2, 100)
    y = f(x)
    plt.plot(x,y)
    plt.axhline(0 , color = 'red', lw = 0.5)
    plt.title('Gráfica de f(x) = x^3 - 5')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()


#mostrar gráfica en ventana de tkinter

btn_grafica = tk.Button(root, text='Mostrar gráfica de f(x)', command=mostrar_grafica)
btn_grafica.pack()

#Para ingresar a
a_Label = tk.Label(root, text='Ingrese el primer valor del intervalo (a): ')
a_Label.pack()
a_entry = tk.Entry(root)
a_entry.pack()

#Para ingresar b
b_Label = tk.Label(root, text='Ingrese el segundo valor del intervalo (b): ')
b_Label.pack()
b_entry = tk.Entry(root)
b_entry.pack()

#Ingresar la tolerancia
tolerancia_Label = tk.Label(root, text='Ingrese la tolerancia (debe ser un valor mayor a 0 y menor a 1): ')
tolerancia_Label.pack()
tolerancia_entry = tk.Entry(root)
tolerancia_entry.pack()

#Botón para ejecutar el método de bisección
def ejecutar_biseccion():
    
    #limpiar el resultado anterior
    resultado_Label.config(text='Calculando...')
    root.update()
    
    #Pausar un poco el programa para que aparezca el mensaje
    import time
    time.sleep(3)
    
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        valor_tolerancia = float(tolerancia_entry.get())
    
        #validar que la tolerancia sea valida
        if valor_tolerancia <= 0 or valor_tolerancia >=1:
            resultado_Label.config(text='La tolerancia debe ser un valor mayor a 0 y menor a 1.')
            return
    
        #Ver si se puede usar el método (f(a) y f(b) < 0)
        if f(a) * f(b) >= 0:
            resultado_Label.config(text='El método de bisección no se puede aplicar. f(a) y f(b) deben tener signos opuestos.')
            return
        
        else:
            #empezar el proceso de bisección
            iteraciones = 0 
        
        while True:
            
            
            #Calcular el punto medio
            Pm = a + (b-a)/2
            #Si el punto medio es la raíz, entonces hay que deterner todo 
            if f(Pm) == 0:
                resultado_Label.config(text=f'La raíz exacta es: {Pm}')
                break
            
            #Calcular el error absoluto
            error_absoluto = abs(a-b)
            #Calcular el error relativo
            error_relativo = error_absoluto/Pm if Pm != 0 else float('inf')
            
            #Imprimir el resultado de la aproximación de la raíz, cuantas iteraciones se hicieron y los errores en la ventana
            resultado_Label.config(text='Aproximación de la ráiz: ' + str(Pm) + '\nNúmero de iteraciones: ' + str(iteraciones) + '\nError absoluto ' + str(error_absoluto) + '\nError relativo: ' + str(error_relativo))
             #condicion de salida porque si se me trabo haciendo esto xd
            if error_absoluto < valor_tolerancia:
                break    
            
            #Aqui agrego el contador, porque si se hace antes entrega 1 iteracion de más
            iteraciones += 1 
            
            #si no es raíz, encontrar el nuevo intervalo
            if f(a) * f(Pm) < 0:
                b = Pm 
            else:
                a = Pm
           
    except ValueError:
        resultado_Label.config(text='Por favor, ingrese valores numéricos válidos')
    #mostrar el resultado en la ventana
    resultado_Label.config(text='Aproximación de la raíz: ' + str(Pm) + '\nNúmero de iteraciones: ' + str(iteraciones) + '\nError absoluto: ' + str(error_absoluto) + '\nError relativo: ' + str(error_relativo))
    
ejecutar_biseccion_button = tk.Button(root, text='Ejectuar el método de bisección', command = ejecutar_biseccion)
ejecutar_biseccion_button.pack()
resultado_Label = tk.Label(root, text='')
resultado_Label.pack()
root.mainloop()