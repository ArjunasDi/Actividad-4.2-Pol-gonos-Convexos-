from functools import cmp_to_key

class Punto:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

def siguienteEnPila(S):
    return S[-2]

def distanciaCuadrada(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

def orientacion(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    return 0 if val == 0 else (1 if val > 0 else 2)

def comparar(p1, p2):
    o = orientacion(p0, p1, p2)
    if o == 0:
        return -1 if distanciaCuadrada(p0, p2) >= distanciaCuadrada(p0, p1) else 1
    return -1 if o == 2 else 1

def envolturaConvexa(puntos, n):
    global p0
    ymin = puntos[0].y
    min = 0
    for i in range(1, n):
        y = puntos[i].y
        if (y < ymin) or (ymin == y and puntos[i].x < puntos[min].x):
            ymin = puntos[i].y
            min = i

    puntos[0], puntos[min] = puntos[min], puntos[0]
    p0 = puntos[0]
    puntos = sorted(puntos, key=cmp_to_key(comparar))

    m = 1
    for i in range(1, n):
        while (i < n - 1) and (orientacion(p0, puntos[i], puntos[i + 1]) == 0):
            i += 1
        puntos[m] = puntos[i]
        m += 1

    if m < 3:
        return

    S = []
    S.append(puntos[0])
    S.append(puntos[1])
    S.append(puntos[2])

    for i in range(3, m):
        while (len(S) > 1) and (orientacion(siguienteEnPila(S), S[-1], puntos[i]) != 2):
            S.pop()
        S.append(puntos[i])

    print("Puntos de la envoltura convexa:")
    while S:
        p = S[-1]
        print(f"({p.x}, {p.y})")
        S.pop()

def ingresar_puntos():
    puntos = []
    n = int(input("Ingrese el número de puntos: "))
    for _ in range(n):
        x, y = map(float, input("Ingrese las coordenadas x e y (separadas por espacio): ").split())
        puntos.append(Punto(x, y))
    return puntos

# Código principal
opcion = input("¿Desea ingresar puntos manualmente (M) o usar un conjunto predeterminado (P)? ").strip().upper()
if opcion == 'M':
    puntos = ingresar_puntos()
else:
    puntos_predeterminados = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    print("Puntos predeterminados: ")
    print(puntos_predeterminados)
    puntos = [Punto(x, y) for x, y in puntos_predeterminados]

n = len(puntos)
envolturaConvexa(puntos, n)


#Ayuda de https://www.geeksforgeeks.org/convex-hull-using-graham-scan/