print("Try programiz.pro")
p=float(input())
s=0
while (p!=0):
    s=s+p
    iva=p*(16/100)
    print ("precio del producto:", p, " su impuesto:", iva)
    p=float(input())

    print("Suma total de productos:", s)