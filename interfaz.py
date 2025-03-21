# interfaz.py

def mostrar_menu():
    print("\n" + "=" * 40)
    print("🧮 CALCULADORA SOA".center(40))
    print("=" * 40)
    print("1️  Suma")
    print("2️  Resta")
    print("3️  Multiplicación")
    print("4️  División")
    print("0️  Salir")
    print("=" * 40)

    opciones = {
        '1': 'suma',
        '2': 'resta',
        '3': 'multiplicación',
        '4': 'división',
        '0': 'salir'
    }

    opcion = input("➡️ Elige una opción (1-4) o 0 para salir: ").strip()

    # Devuelve la opción correspondiente o inválida
    return opciones.get(opcion, "invalida")


def solicitar_numero(mensaje):
    while True:
        try:
            valor = int(input(mensaje + " "))
            return valor
        except ValueError:
            print("⚠️ Entrada no válida. Debes ingresar un número entero.")
