def sumar(a, b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def restar(a, b):
    return sumar(a, sumar(~b, 1))  # Usa complemento a dos para obtener -b

def multiplicar(a, b):
    resultado = 0
    negativo = (a < 0) ^ (b < 0)  # Determinar si el resultado debe ser negativo
    a, b = abs(a), abs(b)
    
    while b:
        if b & 1:
            resultado = sumar(resultado, a)
        a <<= 1
        b >>= 1
    
    return resultado if not negativo else restar(0, resultado)

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    
    negativo = (a < 0) ^ (b < 0)
    a, b = abs(a), abs(b)
    cociente = 0
    
    while a >= b:
        temp_b, multiplicador = b, 1
        while a >= (temp_b << 1):
            temp_b <<= 1
            multiplicador <<= 1
        
        a = restar(a, temp_b)
        cociente = sumar(cociente, multiplicador)
    
    return cociente if not negativo else restar(0, cociente)

def calculadora():
    while True:
        print("\nSeleccione la operación: suma, resta, multiplicación, división o salir")
        opcion = input().strip().lower()
        
        if opcion == "salir":
            print("👋 ¡Gracias por usar la calculadora!")
            break
        
        if opcion not in ["suma", "resta", "multiplicación", "división"]:
            print("⚠️ Operación no válida. Intente de nuevo.")
            continue  # Volver al inicio del ciclo
        
        try:
            a = input("Ingrese el primer número: ")
            b = input("Ingrese el segundo número: ") if opcion in ["suma", "resta", "multiplicación", "división"] else "0"

            # Verificar si los números ingresados son enteros
            if "." in a or "." in b:
                print("⚠️ Error: Solo se permiten números enteros. No se admiten decimales.")
                continue  # Volver al inicio del ciclo

            a, b = int(a), int(b)  # Convertimos a enteros si no hubo error

            if opcion == "suma":
                print(f"✅ El resultado de {a} + {b} es: {sumar(a, b)}")
            elif opcion == "resta":
                print(f"✅ El resultado de {a} - {b} es: {restar(a, b)}")
            elif opcion == "multiplicación":
                print(f"✅ El resultado de {a} × {b} es: {multiplicar(a, b)}")
            elif opcion == "división":
                try:
                    resultado = dividir(a, b)
                    print(f"✅ El resultado de {a} ÷ {b} es: {resultado}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
        except ValueError:
            print("⚠️ Entrada no válida. Por favor, ingrese solo números enteros.")


if __name__ == "__main__":
    calculadora()
