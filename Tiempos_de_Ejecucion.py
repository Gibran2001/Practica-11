#Importamos bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#Cargando modulos
import random
from time import time

#Cargamos las funciones
from insertionSort import insertionSort_time
#Llamamos a la función principal
from quickSort import quickSort_time

datos = [ii*100 for ii in range(0,21)]

tiempo_is = [] #Lista para guardar el tiempo de ejecución de insert sort
tiempo_qs = [] #Lista para guardar el tiempo de ejcución de quick sort

for ii in datos:
    lista_is = random.sample(range(0,10000000),ii)
    #Copia de la lista para que se ejecute el algoritmo con los mismos numeros
    lista_qs = lista_is.copy()

    t0 = time()
    insertionSort_time(lista_is)
    tiempo_is.append(round(time()-t0,6))

    t0 = time ()
    quickSort_time(lista_qs)
    tiempo_qs.append(round(time()-t0,6))

#Imprimimos tiempos parciales
print("Tiempos parciales de ejcución en INSERT SORT {} [s]\n".format(tiempo_is))
print("Tiempos parciales de ejcución en QUICK SORT {} [s]".format(tiempo_qs))

#Imprimimos tiempos totales
#Aplicamos la función sum() para calcular el tiempo total
print("Tiempo total de ejcución en INSERT SORT {} [s]\n".format(sum(tiempo_is)))
print("Tiempo total de ejcución en QUICK SORT {} [s]\n".format(sum(tiempo_qs)))

#Genera la gráfica
fig, ax = subplots()
ax.plot(datos, tiempo_is, label ="insert sort", marker="*", color="r")
ax.plot(datos, tiempo_qs, label ="quick sort", marker="o", color="b")
ax.set_xlabel('Datos')
ax.set_ylabel('Tiempo')
ax.grid(True)
ax.legend(loc=2);

plt.tittle('Tiempo de ejcución [s] (insert vs. quick)')
plt.show()
