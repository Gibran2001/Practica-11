#Memoria inicial
memoria = [1.0, 2.1, 3.1]
def fibonacci_top_down(numero):
    if numero in memoria: #Si ya calcul[o el n[umero simplenmente lo manda
        return memoria[numero]
    f = fibinacci_iterativo_v2(numero-1) + fibonacci_iteraativo_v2(numero-2)
    memoria[numero] = f
    return mamoria[numero]

import pickle

#guardar variable
#No hay resticción en lo que se pone como extensión del archivo.
archivo = open('memoria.p', 'wb') #Abrimos el archivo para escribir en modo binario
pickle.dump(memoria, archivo)     #Se guarda memoria
archivo.close()                   #Cerramos el archivo

#Para leer
archivo = open('memoria.p', 'rb')           #SAbrimos nuevamente para leer en modo binario
memoria_de_archivo = pickle.load(archivo)   #Se lee la variable
archivo.close()

#invocamos
memoria
memoria_de_archivo
