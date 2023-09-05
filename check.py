from io import open
import pickle

class Partidas:

    # Constructor de clase
    def __init__(self, nombre, puntaje, tiempo):
        self.nombre = nombre
        self.puntaje = puntaje
        self.tiempo = tiempo
        print('Se ha guardado la partida:',self.nombre)

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.puntaje)


class CheckP:

    Puntajes = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.Puntajes.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.Puntajes) == 0:
            print("No hay partidas")
            return
        for p in self.Puntajes:
            print("Nombre  | puntos")
            print(p)

    def cargar(self):
        fichero = open('data.txt', 'ab+')
        fichero.seek(0)
        try:
            self.Puntajes = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} partidas".format(len(self.Puntajes)))

    def guardar(self):
        fichero = open('data.txt', 'wb')
        pickle.dump(self.Puntajes, fichero)
        fichero.close()
