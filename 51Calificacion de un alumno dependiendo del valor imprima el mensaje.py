cal=0
cal=float(input("Ingresa una calificación: "))

if  (cal>=0)  and  (cal<=5):
     print ("reprobado")

if (cal>5)  and  (cal<6):
     print ("mal")

if (cal>=6)  and  (cal<7):
    print ("bajo")

if (cal>=7)  and  (cal<8):
     print ("medio")

if (cal>=8)  and  (cal<9):
     print ("alto")

if (cal>=9)  and  (cal<=10):
     print ("muy alto")

if  (cal>10)  or  (cal<0):
     print ("fuera de rango")