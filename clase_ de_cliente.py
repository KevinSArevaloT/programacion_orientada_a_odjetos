class cliente:
    def __init__(self,nombre,edad,numero,documento,direccion):
        self.nombre = nombre
        self.edad = edad
        self.numero = numero
        self.documento = documento
        self.direccion = direccion
    def mostrar_info(self):
        print("\ninformacion del cliente:")
        print(f"nombre del cliente es:  {self.nombre}")
        print(f"edad del cliente es:  {self.edad}")
        print(f"numero del cliente es:  {self.numero}")
        print(f"documento del cliente es:  {self.documento}")
        print(f"direccion del cliente es:  {self.direccion}")
def main():
   nombre = input("ingresa nombre de cliente:  ")
   edad = input("ingrese edad del cliente:  ")
   numero = input("ingrese numero de contacto:  ")
   documento = input("ingrese numero de identificacion:   ")
   direccion = input("ingrese direccion de envio:  ")
   cliente1 = cliente(nombre,edad,numero,documento,direccion)
   cliente1.mostrar_info()
if __name__ == "__main__":
    main()