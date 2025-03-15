# ---------------------------------------
# ✅ Función para restar (SOA)
# ---------------------------------------
def restar(a, b):
    if a >= b:
        # a es mayor o igual que b
        c = a
        while b > 0:
            c -= 1
            b -= 1
        return c
    else:
        # a es menor que b
        c = b
        while a > 0:
            c -= 1
            a -= 1
        return -c