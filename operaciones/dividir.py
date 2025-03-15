from operaciones.restar import restar
from operaciones.sumar import sumar

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

