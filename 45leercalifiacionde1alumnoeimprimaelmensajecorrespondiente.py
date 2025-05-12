calif = float(input("Ingrese la calificación: "))

if (calif >= 0) and (calif <= 5.9):
    print("Reprobado")
elif (calif >= 6) and (calif <= 6.9):
    print("Aprobado bajo")
elif (calif >= 7) and (calif <= 8.9):
    print("Aprobado medio")
elif (calif >= 9) and (calif <= 10):
    print("Aprobado excelente")
else:
    print("Calificación fuera de rango")