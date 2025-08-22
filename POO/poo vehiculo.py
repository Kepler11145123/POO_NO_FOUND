
class Vehiculo:
    def __init__(self, marca, modelo, anio, encendido=True):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = encendido
        self.combustible = "Ninguno"

    def mueve(self):
        print(f"El vehículo {self.marca}{self.modelo} se está moviendo.")

    def enciende(self):
        if self.encendido: 
            print(f"El Vehiculo {self.marca}, está encendido")
        else: 
            print(f"El Vehiculo {self.marca}, está apagado")

    def sonido(self):
        if self.encendido: 
            print(f"El Vehiculo {self.marca}, ha rugido")
        else:
            print(f"El Vehiculo {self.marca}, no puede rugir")



class Electrico(Vehiculo):

    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.combustible = "electrica"
    def caminar(self):
        print(f"El vehículo {self.marca} {self.modelo} se está moviendo silenciosamente.") 
       
    def mostrar_combustible(self):
        print(f"El vehículo {self.marca} usa energía {self.combustible}")


class Gasolina(Vehiculo):

    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.combustible = "Gasolina"
    def caminar(self):
        print(f"El vehículo {self.marca} {self.modelo} se está moviendo con motor de combustión.")
    def mostrar_combustible(self):
        print(f"El vehículo {self.marca} usa {self.combustible}")

tesla = Electrico("Tesla", "Model S", 2020)
ford = Gasolina("Ford", "Mustang", 2021)
tesla.encendido = False
tesla.mostrar_combustible()
ford.mostrar_combustible()
tesla.mueve()
ford.mueve()
tesla.enciende()
ford.enciende()
tesla.sonido()
ford.sonido()


