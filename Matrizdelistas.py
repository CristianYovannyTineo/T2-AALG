import random
import math

def icoordenadas(n):
    matriz = []
    for _ in range(n):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        matriz.append([x, y])
    return matriz

def ing():
    puntos = []
    cantidad = int(input("¿Cuántos pares deseas ingresar ? "))
    for i in range(cantidad):
        print(f"Ingresando par {i + 1}:")
        x = int(input("  Ingrese X(+): "))
        y = int(input("  Ingrese Y(-): "))
        puntos.append([x, y])
    return puntos

def distancia(punto):
    x, y = punto
    return math.sqrt(x**2 + y**2)

def co_alejada(puntos):
    if not puntos:
        return ["Incorrecto", "Incorrecto"]

    if len(puntos) == 1:
        x, y = puntos[0]
        if x > 0 and y < 0:
            return puntos[0]
        else:
            return ["Incorrecto", "Incorrecto"]

    mid = len(puntos) // 2
    izquierda = co_alejada(puntos[:mid])
    derecha = co_alejada(puntos[mid:])

    if izquierda == ["Incorrecto", "Incorrecto"]:
        return derecha
    if derecha == ["Incorrecto", "Incorrecto"]:
        return izquierda

    return izquierda if distancia(izquierda) > distancia(derecha) else derecha

def main():
    print("Menú")
    print("1. Ingresar las coordenadas (par)")
    print("2. Generar coordenadas aleatoriamente")

    opcion = input("Seleccione una opción [1 o 2]: ")
    coordenadas = []

    if opcion == "1":
        coordenadas = ing()
    elif opcion == "2":
        n = int(input("¿Cuántos pares deseas generar? "))
        coordenadas = icoordenadas(n)
    else:
        print("Opción no válida.")
        return

    print("\n|Coordenadas ingresadas|")
    for punto in coordenadas:
        print(punto)

    resultado = co_alejada(coordenadas)

    print("\nCoordenada más alejada (0,0) :")
    if resultado == ["Incorrecto", "Incorrecto"]:
        print("Ingresar cordenadas X(+) , Y(-)")
    else:
        print(f"{resultado} con distancia {distancia(resultado):.2f}")

main()
