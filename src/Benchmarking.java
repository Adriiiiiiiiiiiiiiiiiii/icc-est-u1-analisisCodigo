import java.util.Random;

public class Benchmarking {
    private MetodosOrdenamiento mOrdenamiento;

    public Benchmarking() {
        long currentMillis = System.currentTimeMillis(); 
        long currentNano = System.nanoTime();           

        System.out.println("CurrentTimeMillis: " + currentMillis);
        System.out.println("NanoTime: " + currentNano);

        int[] arreglo = generarArregloAleatorio(1000000);

        mOrdenamiento = new MetodosOrdenamiento(); 
        Runnable tarea = () -> mOrdenamiento.burbujaTradicional(arreglo.clone()); 

        double tiempoDuracionMillis = medirConCurrentTimeMillis(tarea);
        double tiempoDuracionNano = medirConNanoTime(tarea);

        System.out.println("Tiempo en Millis: " + tiempoDuracionMillis + " s");
        System.out.println("Tiempo en Nano: " + tiempoDuracionNano + " s");
    }

    private int[] generarArregloAleatorio(int tamaño) {
        int[] array = new int[tamaño];
        Random random = new Random();
        for (int i = 0; i < tamaño; i++) {
            array[i] = random.nextInt(1000000);
        }
        return array;
    }

    private double medirConCurrentTimeMillis(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        return (fin - inicio) / 1000.0; 
    }

    private double medirConNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0; 
    }
}