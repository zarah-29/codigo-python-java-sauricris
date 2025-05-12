S = 0
C = 100
contador = 0

for _ in range(35):
    S = S + C
    C = S
    contador += S
print(f"Total S: {contador}")