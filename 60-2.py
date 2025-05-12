def gradocentigrados_a_fahrenheit(grados_celsius):
    return (grados_celsius * 9/5) + 32


grados_celsius = float(input("Introduce los grados Celsius: "))
grados_fahrenheit = gradocentigrados_a_fahrenheit(grados_celsius)
print(f"{grados_celsius}°C equivalen a {grados_fahrenheit}°F")