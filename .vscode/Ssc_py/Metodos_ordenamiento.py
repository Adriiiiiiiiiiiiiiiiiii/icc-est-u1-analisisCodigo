class Metodos_ordenamiento:
    def bubble_sort(self, array):
        arreglo=array.copy()  
        n=len(arreglo)
        for i in range(n):
            for j in range(i+1,n):
                if arreglo[i]> arreglo[j]:
                    arreglo[i], arreglo[j]=arreglo[j], arreglo[i]
        return(arreglo)
    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            cambio = False
            for j in range(0 , n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    cambio = True
            if not cambio:
                break  
        return arreglo

    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_idx]:
                    min_idx = j
            arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
        return arreglo


