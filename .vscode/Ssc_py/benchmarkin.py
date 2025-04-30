import time
from Metodos_ordenamiento import Metodos_ordenamiento
import random
class Benchmarkin:
    def __init__(self):
        print("Benchmarking instanciado")
        self.mO=Metodos_ordenamiento()
        arreglo=self.build_arreglo(10000)
        tarea=lambda:self.mO.bubble_sort(arreglo)
        tiempomillisegundos=self.contar_con_current_time_millis(tarea)
        tiemponanosegundos=self.contar_con_nano_time(tarea)
        print(f"El tiempo en millisegundos es : {tiempomillisegundos}\nEL tiempo en nanosegundos del metodo burbuja es: {tiemponanosegundos}")
        tarea_con_burbuja_mejorado=lambda:self.mO.sort_burbuja_mejorado_optimizado(arreglo)
        tiemponanosegundos_burbuja_mejorado=self.contar_con_nano_time(tarea_con_burbuja_mejorado)
        print(f"El timepo en nanosegundos con el metodo burbuja mejorado es: {tiemponanosegundos_burbuja_mejorado}")

        tarea_con_seleccion=lambda:self.mO.sort_seleccion(arreglo)
        tiemponanosegundos_seleccion=self.contar_con_nano_time(tarea_con_seleccion)
        print(f"EL tiempo en nanoseugndos con el metodo seleccion es: {tiemponanosegundos_seleccion}")
    def build_arreglo(self, tamaño):
        arreglo=[]
        for i in range(tamaño):
            numero=random.randint(0,99999)
            arreglo.append(numero)
        return(arreglo)
    #importar time
    #milisegundos en segundos con # x=time.time()
    #nanosegundo con #x=time.time_ns()
    
    def contar_con_current_time_millis(self, tarea):
        x = time.time_ns()
        tarea()
        x2 = time.time_ns()
        return (x2 - x) / 1_000_000_000  
    def contar_con_nano_time(self, tarea):
        x = time.time()
        tarea()
        x2 = time.time()
        return x2 - x 

        