print("=== Conversor de Monedas ===")

print("1. USD → PEN")
print("2. PEN → USD")
print("3. USD → ARS")
print("4. ARS → USD")

opcion = int(input("Elige una opción: "))

cantidad = float(input("Ingresa la cantidad: "))

# Tasas (puedes cambiarlas)
usd_pen = 3.80
usd_ars = 950

if opcion == 1:
    print("Resultado:", cantidad * usd_pen, "PEN")

elif opcion == 2:
    print("Resultado:", cantidad / usd_pen, "USD")

elif opcion == 3:
    print("Resultado:", cantidad * usd_ars, "ARS")

elif opcion == 4:
    print("Resultado:", cantidad / usd_ars, "USD")

else:
    print("Opción inválida")
input("\nPresiona ENTER para salir...")
