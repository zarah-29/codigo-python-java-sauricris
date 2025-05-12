total = 0

while True:
    compra = float(input("Ingrese el total de la compra (0.0 para terminar): "))

    if compra == 0.0:
        break

    total += compra

print(f"Total a pagar: ${total:.2f}")