import time

class Archivos:
    def abro(self, nombre, tipo="r"):
        open(nombre, tipo)

    def leo(self):
        pass

    def cierro(self):
        pass

    def escribo(self):
        pass


class Lista:
    def cargo(self):  # aca cargo los expedientes
        pass

    def tildo(self):  # aca hago el cruze
        pass

    def busco_falta(self):  # aca genero un listado de faltantes
        pass

    def busco_sobra(self):  # aca genero un listado de sobrantes
        pass


class Pantalla:
    def __init__(self):
        self.titulo = "Control de Expedientes de Lista"

    def muestro_opciones(self, opciones=[]):
        print(self.titulo)
        for i in range(1, len(opciones) + 1):
            print(str(i) + " :" + opciones[i - 1])


menu = Pantalla()
opciones = ["Cargo", "Cruzo", "Sobrantes", "Faltantes", "Salir"]
opcion = len(opciones) - 1
while opciones[opcion - 1] != "Salir":
    menu.muestro_opciones(opciones)
    opcion = int(input("elija una opcion:"))
    while opcion > len(opciones) or opcion < 1:
        opcion = int(input("Ingrese una opcion valida entre 1 y " + str(len(opciones) + " :")))
        continue
    if opciones[opcion-1] == "Cargo":
        archivo = Archivos()
        archivo.abro("carga"+time.strftime("%d%m%y")+".txt", "a+")
        lista = Lista()
        lista.cargo()

