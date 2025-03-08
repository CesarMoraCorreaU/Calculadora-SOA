# Función para sumar sin usar el operador "+"
def sumar(a, b):
    while b:  # Mientras haya un acarreo
        carry = a & b  # Encuentra los bits que generan acarreo
        a = a ^ b  # Suma sin considerar el acarreo (XOR)
        b = carry << 1  # Desplaza el acarreo a la izquierda para sumarlo en la siguiente iteración
    return a  # Devuelve la suma de a y b

# Función para restar sin usar el operador "-"
def restar(a, b):
    return sumar(a, sumar(~b, 1))  # Convierte b a su complemento a dos (-b) y lo suma a a

# Función para multiplicar sin usar el operador "*"
def multiplicar(a, b):
    resultado = 0  # Variable para almacenar el resultado de la multiplicación
    negativo = (a < 0) ^ (b < 0)  # Determina si el resultado debe ser negativo
    a, b = abs(a), abs(b)  # Trabajamos con valores absolutos para facilitar la operación
    
    while b:  # Mientras b sea mayor que 0
        if b & 1:  # Si el último bit de b es 1, sumamos a al resultado
            resultado = sumar(resultado, a)
        a <<= 1  # Duplicamos a (equivalente a a * 2)
        b >>= 1  # Reducimos b a la mitad (equivalente a b // 2)
    
    return resultado if not negativo else restar(0, resultado)  # Aplica el signo correcto al resultado

# Función para dividir sin usar el operador "/"
def dividir(a, b):
    if b == 0:  # Manejo de error: No se puede dividir por cero
        raise ValueError("No se puede dividir por cero")
    
    negativo = (a < 0) ^ (b < 0)  # Determina si el resultado debe ser negativo
    a, b = abs(a), abs(b)  # Trabajamos con valores absolutos para facilitar la operación
    cociente = 0  # Variable para almacenar el resultado de la división
    
    while a >= b:  # Mientras el dividendo sea mayor o igual que el divisor
        temp_b, multiplicador = b, 1  # Variables auxiliares para encontrar el mayor múltiplo posible
        while a >= (temp_b << 1):  # Encuentra el mayor múltiplo de b que se pueda restar
            temp_b <<= 1  # Duplicamos temp_b (b * 2)
            multiplicador <<= 1  # Multiplicamos por 2 el factor de multiplicación
        
        a = restar(a, temp_b)  # Restamos el mayor múltiplo posible de b
        cociente = sumar(cociente, multiplicador)  # Sumamos el factor de multiplicación al cociente
    
    return cociente if not negativo else restar(0, cociente)  # Aplica el signo correcto al resultado

# Función principal de la calculadora
def calculadora():
    while True:
        print("\nSeleccione la operación: suma, resta, multiplicación, división o salir")
        opcion = input().strip().lower()  # Leer la opción del usuario y convertir a minúsculas
        
        if opcion == "salir":  # Si el usuario elige salir, termina el programa
            print("👋 ¡Gracias por usar la calculadora!")
            break
        
        if opcion not in ["suma", "resta", "multiplicación", "división"]:  # Validar opción ingresada
            print("⚠️ Operación no válida. Intente de nuevo.")
            continue  # Volver al inicio del ciclo
        
        try:
            a = input("Ingrese el primer número: ").strip()  # Leer el primer número
            b = input("Ingrese el segundo número: ").strip() if opcion in ["suma", "resta", "multiplicación", "división"] else "0"

            # Verificar si los números ingresados son enteros
            if "." in a or "." in b:  # Si detecta un punto decimal, mostrar error
                print("⚠️ Error: Solo se permiten números enteros. No se admiten decimales.")
                continue  # Volver al inicio del ciclo

            a, b = int(a), int(b)  # Convertimos a enteros si no hubo error

            # Ejecutar la operación seleccionada
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
        except ValueError:  # Si el usuario ingresa algo que no es un número
            print("⚠️ Entrada no válida. Por favor, ingrese solo números enteros.")

# Ejecutar la calculadora si este archivo es ejecutado directamente
if __name__ == "__main__":
    calculadora()
