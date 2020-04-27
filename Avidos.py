def cambio(cantidad, denominaciones):
    resultado = []
    while (cantidad > 0):
        if (cantidad >= denominaciones[0]):

            num = cantidad // denominaciones[0]
            cantidad = cantidad - (num * denominaciones[0])
            resultado.append([denominaciones[0], num])
        denominaciones = denominaciones[1:] #Consume la lista de denominaciones
    return resultado
#Probamos

print(cambio(1000, [500,200,100,50,20,5,1]))
print(cambio(500, [500,200,100,50,20,5,1]))

#Regresando una opcion que no es la optima
print(cambio(98, [5,20,1,50]))
