class Empleado:
    def __init__(self, nombre: str, puesto: str, antiguedad: int) -> None:
        self.nombre = nombre
        self.puesto = puesto
        self.antiguedad = antiguedad

    def __str__(self) -> str:
        return f"{self.nombre}, Puesto: {self.puesto}, Antigüedad: {self.antiguedad} años"
        
    def ascender(self, nuevo_puesto: str):
        self.puesto = nuevo_puesto

    def aumentar_antiguedad(self, anios: int):
        self.antiguedad += anios

empleado1 = Empleado("Erick", "developer", 6)
empleado1.aumentar_antiguedad(2)
print(empleado1)