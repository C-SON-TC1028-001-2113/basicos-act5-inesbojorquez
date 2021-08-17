import math
def main():
    #escribe tu código abajo de esta línea
     h = int(input("Cual es la altura de la casa? "))
     g = int(input("Cual es el angulo? "))
     s = math.sin(g)
     largo = h/s
     print ("El largo de la escalera es:  "+str(math.ceil(largo)))
   
   
if __name__ == '__main__':
    main()
