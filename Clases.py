class Coche:    
    def __init__(self, color, motor):
        self.color = color
        self.motor = motor
    def verCoche(self):
        print("El coche es: ", self.color, self.motor)

C1 = Coche("rojo",1800)
C2 = Coche("verde",2000)
C1.verCoche()
C2.verCoche()

C1.color = "Rosa"
C1.verCoche()
