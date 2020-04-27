def fibonacci_iterativo_vl(numero):
    f1=0
    f2=1
    tmp=0
    for i in range(1,numero-1):
        tmp = f1+f2
        f1 = f2
        f2 = tmp
    return f2
#invocamos
fibonacci_iterativo_vl(6)

#Asignacion paralela

def fibonacci_iterativo_v2(numero):
    f1 = 0
    f2 = 1
    for i in range(1, numero-1):
        f1,f2=f2,f1+f2 #Asignación paralela
    return f2
#invocamos
fibonacci_iterativo_v2(6)
