class pc:
    def __init__(self,cpu,gpu,placa,ram,almacenamiento,fuente,refrigeracion,red,audio,video,teclado,mouse):
        self.cpu = cpu
        self.gpu = gpu
        self.placa = placa
        self.ram =ram
        self.almacenamiento = almacenamiento
        self.fuente = fuente
        self.refrigeracion =refrigeracion
        self.red = red
        self.audio = audio
        self.video = video
        self.teclado = teclado
        self.mouse = mouse
    def mostrar_informacion(self):
        print("\ninformacion de la pc:")
        print(f"\nla cpu es:  {self.cpu}")
        print(f"la gpu es: {self.gpu}")
        print(f"la placa madre es: {self.placa}")
        print(f"la ram es:  {self.ram}")
        print(f"el almacenamiento es:  {self.almacenamiento}")
        print(f"la fuente es: {self.fuente}")
        print(f"la refrigeracion es:  {self.refrigeracion}")
        print(f"la conexion es:  {self.red}")
        print(f"la conexion de audio es:  {self.audio}")
        print(f"la conexion de video es:  {self.video}")
        print(f"el teclado usado es:  {self.teclado}")
        print(f"el mouse usado es:  {self.mouse}")
def main():
    cpu = input("¿cpu que usa la pc?")
    gpu = input("¿gpu que usa la pc?")
    placa = input("¿placa madre que usa la pc?")
    ram = input("¿ram que usa la pc?")
    almacenamiento = input("¿almacenamiento que usa la pc?")
    fuente = input("¿fuente que usa la pc?")
    refrigeracion = input("¿refrigeracion que usa la pc?")
    red = input("¿conexion de red que usa la pc?")
    audio = input("¿conexion de audio que usa la pc?")
    video = input("¿conexion de video que usa la pc?")
    teclado = input("¿teclado que usa la pc?")
    mouse = input("¿mouse que usa la pc?")
    pc1 = pc(cpu, gpu, placa, ram, almacenamiento, fuente, refrigeracion, red, audio, video, teclado, mouse)
    pc1.mostrar_informacion()
if __name__ == "__main__":
    main()