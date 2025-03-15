# interfaz.py

def mostrar_menu():
    print("\n🧮 Calculadora SOA - Operaciones disponibles:")
    print("👉 suma, resta, multiplicación, división o salir")
    return input("➡️ Elige una opción: ").strip().lower()

def solicitar_numero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("⚠️ Entrada no válida. Debes ingresar un número entero.")
