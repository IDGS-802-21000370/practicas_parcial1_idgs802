class piramide():
#declaración de propiedades
    numero=0

#declaración de contructor
    def __init__(self,num):
        self.numero=num

#declaracion de metodos de clase
    def crear_piramide(self):
        columna=0
        while columna<self.numero:
            fila=columna+1
            cont=0
            x=""
            while(cont<fila):
                x="*"*(columna+1)
                cont+=1
            print(x)
            columna=columna+1

            

def main():
    n = int(input("Ingresa los asteriscos para la piramide"))
    x = piramide(n)
    x.crear_piramide()

if __name__ == "__main__":
    main()