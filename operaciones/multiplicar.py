from operaciones.sumar import sumar
# ---------------------------------------
# ✅ Función para multiplicar (SOA)
# ---------------------------------------
def multiplicar(a, b):
    c = 0  # Acumulador
    while b > 0:
        c = sumar(c, a)  # Suma a al acumulador c
        b -= 1
    return c  # Resultado de la multiplicación

