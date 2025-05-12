A = 100
B = 101
fibonacci = [A, B]
for _ in range(33):
    C = A + B
    fibonacci.append(C)
    A = B
    B = C
suma_total = sum(fibonacci)
print("Secuencia de Fibonacci desde 100 (35 términos):")
print(fibonacci)
print(f"\nSuma total de los 35 términos: {suma_total}")