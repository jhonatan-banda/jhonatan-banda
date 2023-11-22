import threading
import time

class MiAplicacion:
    def __init__(self):
        self.usuario_autenticado = False
        self.conexion_bd = False
        self.modo_debug = True

    def verificar_estado(self):
        print("Estado de la aplicación:")
        print(f"Usuario autenticado: {self.usuario_autenticado}")
        print(f"Conexión a la base de datos: {self.conexion_bd}")
        print(f"Modo debug: {self.modo_debug}")

def tarea_asincrona(aplicacion):
    time.sleep(2)  # Simular una operación que lleva tiempo
    aplicacion.usuario_autenticado = True
    aplicacion.conexion_bd = True
    aplicacion.verificar_estado()

if __name__ == "__main__":
    # Crear una instancia de la aplicación
    mi_aplicacion = MiAplicacion()

    # Crear un hilo para realizar una tarea asíncrona
    hilo = threading.Thread(target=tarea_asincrona, args=(mi_aplicacion,))

    # Iniciar el hilo
    hilo.start()

    # Continuar con otras operaciones en el hilo principal
    print("Realizando otras operaciones en el hilo principal.")

    # Esperar a que el hilo termine
    hilo.join()

    # Verificar el estado actual de la aplicación
    mi_aplicacion.verificar_estado()
