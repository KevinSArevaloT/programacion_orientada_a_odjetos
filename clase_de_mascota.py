class mascota:
    def __init__(self,raza,edad,altura,genero):
        self.raza = raza
        self.edad = edad
        self.altura = altura
        self.genero = genero
    def mostrar_informacion(self):
        print("\ninformacion de la mascota:")
        print(f"la raza de la mascota es:  {self.raza}")
        print(f"la edad de la mascota es:  {self.edad}")
        print(f"la altura de la mascota es:  {self.altura}")
        print(f"el genero de la mascota es:  {self.genero}")
def main():
    raza = input("ingrese la raza de la mascota:  ")
    edad = input("ingrese la edad de la mascota:  ")
    altura = input("ingrese la altura de la mascota:  ")
    genero = input("ingrese el genero de la mascota:  ")
    mascota1 =mascota(raza,edad,altura,genero)
    mascota1.mostrar_informacion()
if __name__ == "__main__":
    main()