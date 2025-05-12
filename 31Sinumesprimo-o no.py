n = int(input("Ingrese un número: "))

if n <= 1:
    print("NO es primo")
else:
    es_primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("NO es primo")
            es_primo = False
            break
    if es_primo:
        print("ES primo")

