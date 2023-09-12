#hilos
import time,os,threading as th,threading
from time import sleep


print('Metodo de hilos \n')
def info():
    print(f'{threading.current_thread().name} {threading.get_native_id()}')


# creamos los hilos
hilo1 = threading.Thread(target=info)
hilo2 = threading.Thread(target=info)
hilo3 = threading.Thread(target=info)

# ejecutamos los hilos
hilo1.start()
hilo2.start()
hilo3.start()


# el programa principal sigue ejecutándose aunque los hilos no hayan terminado
print(f'{threading.current_thread().name} {threading.get_native_id()}')
print('    ')

#procesos
from multiprocessing import Process
import os

def info(title):
    print('Metodo de procesos')
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

#demonios
def chequear(nombre):
    #revisar el tamaño de un archivo
    contador = 0
    tam = 0
    while contador < 50:
        contador +=1
        if os.path.exists(nombre):
            estado = os.star(nombre)
            tam = estado.st_size
        print(th.current_thead().getName(),contador,tam,'bytes')
        time.sleep(0.1)

def escribir(nombre):
    #escribir un archivo de texto
    contador = 1
    while contador <= 10:
        with open(nombre,'a') as archivo:
            archivo.write('1')
            rint(th.current_thead().getName(),contador)
            time.sleep(0.3)
            contador+=1

nombre = 'archivo.txt'

if os.path.exists(nombre):
    os.remove(nombre)

hilo1 = th.Thread(name='chequear',target=chequear,args=(nombre,),daemon=True)

hilo2 = th.Thread(name='chequear',target=chequear,args=(nombre,))

hilo1.start()
print(hilo1.is_alive())
hilo2.start()

hilo1.join()
print(hilo1.is_alive())


#concurrencia
def suma_y_producto(a, b):
	sleep(.2)
	mostrar_actual()
	s, p = a + b, a * b
	print(f'{a} + {b} = {s}, {a} * {b} = {p}')

def estado(t):
	if t.is_alive():
		print(f'Thread {t.name} esta activo.')
	else:
		print(f'Thread {t.name} ha terminado.')

def mostrar_actual():
	print('El thread actual es {}.'.format(
		threading.current_thread()
	))
	print('Threads: {}'.format(
		list(threading.enumerate())))

mostrar_actual()
t = threading.Thread(target=suma_y_producto,
	name='SumPro', args=(3, 7))

t.start()
estado(t)
t.join()
estado(t)
