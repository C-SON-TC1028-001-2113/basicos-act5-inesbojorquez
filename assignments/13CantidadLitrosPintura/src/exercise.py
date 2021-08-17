import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input('Area a pintar en metros: '))
    rendimiento = int(input('Rendimiento(m2/l): '))
    comprar = area/rendimiento
    print("Litros a comprar: " +str(math.ceil(comprar)))

    print("El area es: " +str(area))



if __name__ == '__main__':
    main()
