class automovil:
    def __init__(self,marca, modelo, año, color ): #contenedor
        self.marca  = marca
        self.modelo = modelo
        self.año = año
        self.color = color
    def mostrar_info(self):
        print("\ninformacion del automovil:")
        print(f"\nla marca de carro es: {self.marca}")
        print(f"el modelo es: {self.modelo}")
        print(f"el año es:  {self.año}")
        print(f"el color es:  {self.color}")
def main():
    marca = input("ingrese la marca del automovil:  ")
    modelo = input("ingrese modelo:  ")
    año = input("ingrese año del automovil:  ")
    color = input("ingresar color de automovil:  ")
    carro1= automovil(marca, modelo, año, color)
    carro1.mostrar_info()
if __name__ == "__main__":
    main()