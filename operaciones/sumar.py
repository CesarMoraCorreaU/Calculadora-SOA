# ---------------------------------------
# ✅ Función para sumar (SOA)
# ---------------------------------------
def sumar(a, b):
    c = b  # iguala el futuro retultado ==> b
    while a > 0:
        c += 1  # Incrementa en 1 c
        a -= 1  # Decrementa en 1 a
    return c  # Resultado de la suma