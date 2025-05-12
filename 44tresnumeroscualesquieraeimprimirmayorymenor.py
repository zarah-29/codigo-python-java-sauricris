N1 = float(input("Ingrese número 1: "))
N2 = float(input("Ingrese número 2: "))
N3 = float(input("Ingrese número 3: "))

if (N1 > N2) and (N1 > N3) and (N2 > N3):
    print(f"{N1} es mayor y {N3} es menor")
elif (N1 > N2) and (N1 > N3) and (N3 > N2):
    print(f"{N1} es mayor y {N2} es menor")
elif (N2 > N1) and (N2 > N3) and (N1 > N3):
    print(f"{N2} es mayor y {N3} es menor")
elif (N2 > N1) and (N2 > N3) and (N3 > N1):
    print(f"{N2} es mayor y {N1} es menor")
elif (N3 > N1) and (N3 > N2) and (N2 > N1):
    print(f"{N3} es mayor y {N1} es menor")
elif (N3 > N1) and (N3 > N2) and (N1 > N2):
    print(f"{N3} es mayor y {N2} es menor")