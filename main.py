#LA FUNCION DE INTERFAZ
from interfaz import mostrar_menu, solicitar_numero

#LAS OPERACIONES 
from operaciones.sumar import sumar
from operaciones.restar import restar
from operaciones.multiplicar import multiplicar
from operaciones.dividir import dividir

def calculadora():
    while True:
        opcion = mostrar_menu()

        if opcion == "salir":
            print("👋 ¡Gracias por usar la calculadora SOA!")
            break

        if opcion not in ["suma", "resta", "multiplicación", "multiplicacion", "division", "división"]:
            print("⚠️  Error: Opción inválida. Debe ingresar exactamente 'suma', 'resta', 'multiplicación', 'división' o 'salir'.")
            continue

        a = solicitar_numero("➡️ Ingrese el primer número (entero positivo): ")
        b = solicitar_numero("➡️ Ingrese el segundo número (entero positivo): ")

        # Ejecución de la operación seleccionada
        if opcion == "suma":
            resultado = sumar(a, b)
            print(f"✅ El resultado de {a} + {b} es: {resultado}")

        elif opcion == "resta":
            resultado = restar(a, b)
            print(f"✅ El resultado de {a} - {b} es: {resultado}")

        elif opcion in ["multiplicacion", "multiplicación"]:
            resultado = multiplicar(a, b)
            print(f"✅ El resultado de {a} × {b} es: {resultado}")

        elif opcion in ["division", "división"]:
            resultado = dividir(a, b)
            print(f"✅ El resultado de {a} ÷ {b} es: {resultado}")

if __name__ == "__main__":
    calculadora()
