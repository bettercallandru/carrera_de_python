class Automovil: 
    def __init__ (self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros = 4)

        def acelerar (self, tipo='despacio'):            
            if self._motor.gasolina > 0: 
                print(f'acelerar {tipo}')
            else: 
                print(f'nivel de gasolina = {self._motor.gasolina}')

        def cambiar_estado (self) :
             if self._motor.enscender():
                 self._estado = 'enscendido'

class Motor: 
    def __init__ (self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura
        self.gasolina = 0

    def inyecta_gasolina (self, cantidad):        
        self.gasolina += cantidad

    def enscender (self):
        if self._temperatura > 10: 
            return true
