# ---------------------------------------
# ✅ Función para sumar (SOA)
# ---------------------------------------
def sumar(a, b):
    c = b  # iguala el futuro retultado ==> b
    while a > 0:
        c += 1  # Incrementa en 1 c
        a -= 1  # Decrementa en 1 a
    return c  # Resultado de la suma


# ---------------------------------------
# ✅ Función para restar (SOA)
# ---------------------------------------
def restar(a, b):
    c = a  # iguala el futuro retultado ==> a
    while b > 0:
        c -= 1  # Decrementa c
        b -= 1  # Decrementa b
    return c  # Resultado de la resta


# ---------------------------------------
# ✅ Función para multiplicar (SOA)
# ---------------------------------------
def multiplicar(a, b):
    c = 0  # Acumulador
    while b > 0:
        c = sumar(c, a)  # Suma a al acumulador c
        b -= 1
    return c  # Resultado de la multiplicación


# ---------------------------------------
# ✅ Función para dividir (SOA)
# ---------------------------------------
def dividir(a, b):
    if b == 0:
        print("❌ No se puede dividir por cero.")  # Muestra un mensaje
        return "Math Error"  # Termina la función devolviendo un valor nulo

    cociente = 0
    while a >= b:
        a = restar(a, b)  # Resta b de a
        cociente = sumar(cociente, 1)  # Aumenta el cociente en 1
    return cociente  # Resultado de la división entera


# ---------------------------------------
# ✅ Función principal de la calculadora
# ---------------------------------------
def calculadora():
    while True:
        print("\n🧮 Calculadora SOA - Operaciones disponibles:")
        print("👉 suma, resta, multiplicación, división o salir")
        opcion = input("➡️ Elige una opción: ").strip().lower()

        if opcion == "salir":
            print("👋 ¡Gracias por usar la calculadora SOA!")
            break

        if opcion not in ["suma", "resta", "multiplicación","multiplicacion", "division", "división"]:
            print("⚠️ Operación no válida. Intente de nuevo.")
            continue

        try:
            a = input("➡️ Ingrese el primer número (positivo): ").strip()
            b = input("➡️ Ingrese el segundo número (positivo): ").strip()

            a, b = int(a), int(b)
            
            # Ejecución de la operación seleccionada
            if opcion == "suma":
                resultado = sumar(a, b)
                print(f"✅ El resultado de {a} + {b} es: {resultado}")

            elif opcion == "resta":
                if a < b:
                    print("⚠️ Error: El primer número debe ser mayor o igual al segundo para esta resta.")
                else:
                    resultado = restar(a, b)
                    print(f"✅ El resultado de {a} - {b} es: {resultado}")

            elif opcion in ["multiplicacion", "multiplicación"]:
                resultado = multiplicar(a, b)
                print(f"✅ El resultado de {a} × {b} es: {resultado}")

            elif opcion in ["division", "división"]:
                    resultado = dividir(a, b)
                    print(f"✅ El resultado de {a} ÷ {b} es: {resultado}")

        except ValueError:
            print("⚠️ Entrada no válida. Debes ingresar números enteros positivos.")


# ---------------------------------------
# ✅ Ejecutar calculadora
# ---------------------------------------
    calculadora()
