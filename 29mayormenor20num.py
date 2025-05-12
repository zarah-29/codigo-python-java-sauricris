N = float(input("Ingrese un número: "))

if N <= 1:
    print("El número debe ser mayor que 1")
else:
    mayor_menor = N
    for i in range(20):
        num = float(input("Ingrese un número: "))
        if num <= N and (num > mayor_menor):
            mayor_menor = num
    print("El número mayor menor o igual es:", mayor_menor)


    

