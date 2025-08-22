class vehiculo:
    def __init__(self, tipo, modelo, año, color):
        self.tipo = tipo
        self.modelo = modelo
        self.año = año
        self.color = color
        self.estado_motor = "apagado"
    
    def describir(self):
        return f"Vehículo: {self.tipo} {self.modelo}, Año: {self.año}, Color: {self.color}"
    
    def encender(self):
        if self.estado_motor == "apagado":
            self.estado_motor = "encendido"
            return f"El {self.tipo} {self.modelo} se ha encendido."
        else:
            return f"El {self.tipo} {self.modelo} ya está encendido."
        
    def apagar(self):
        if self.estado_motor == "apagado":
            self.estado_motor = "encendido"
            return f"El {self.tipo} {self.modelo} se ha encendido."
        else:
            return f"El {self.tipo} {self.modelo} ya está encendido."


class carro(vehiculo):
    def __init__(self, marca, modelo, año, color, numero_puertas):
        super().__init__(marca, modelo, año, color)
        self.numero_puertas = numero_puertas
    
    def tocar_bocina(self):
        return "el carro hace: ¡BEEP BEEP!"
    
    def abrir_maletero(self):
        if self.estado_motor == "apagado":
            return "El maletero del carro se ha abierto."
        else:
            return "No se puede abrir el maletero con el motor encendido."

class moto(vehiculo):
    def __init__(self, tipo, modelo, año, color, cilindraje):
        super().__init__(tipo, modelo, año, color)
        self.cilindraje = cilindraje
    
    def hacer_caballito(self):
        return "la moto hace un caballito."
    
    def acelerar(self):
        if self.estado_motor == "encendido":
            return "¡La moto está acelerando con fuerza!"
        else:
            return "No se puede acelerar, la moto está apagada."


print("--- Probar la clase Carro ---")
mi_carro = carro("Ford", "Mustang", 2023, "Rojo", 2)

# Métodos heredados del padre
print(mi_carro.describir())
print(mi_carro.apagar())      # El motor ya está apagado
print(mi_carro.encender())    # El motor se enciende
print(mi_carro.encender())    # El motor ya está encendido

# Métodos específicos de la clase carro
print(mi_carro.tocar_bocina())
print(mi_carro.abrir_maletero()) # No se puede abrir porque el motor está encendido

# Apagar el motor para probar de nuevo
print(mi_carro.apagar())
print(mi_carro.abrir_maletero())




print("--- Probar la clase Moto ---")
mi_moto = moto("Kawasaki", "Ninja", 2022, "Verde", "636cc")

# Métodos heredados del padre
print(mi_moto.describir())
print(mi_moto.acelerar())     # No se puede acelerar, la moto está apagada
print(mi_moto.encender())     # El motor se enciende

# Métodos específicos de la clase moto
print(mi_moto.acelerar())
print(mi_moto.hacer_caballito())
print(mi_moto.apagar())       # El motor se apaga




