 #a) sumatoria de i=1 hasta 1000 de 0.0001
 #b) 1 + a)
 #c) 100 + a)
 #d) 10000 + a)
 
 #Para el inciso a) haremos la sumatoria
 
suma = 0.0
for i in range(10000):
    suma += 0.0001

print(f"Resultado inciso a): {suma}")

#b)
b = 1 + suma
print(f"Resultado inciso b): {b}")

#c)
c = 100 + suma
print(f"El resultado del inciso c):  {c}")

#d)
d = 10000 + suma
print(f"El resultado del inciso d es:  {d}")