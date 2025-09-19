import requests
import time
import random

class ConsultaDatosClimaticos:
    """
    Clase para obtener datos climáticos (temperatura o humedad) de varias ciudades de Colombia.
    Utiliza la API de OpenWeatherMap para realizar las peticiones.
    """
    def __init__(self, api_key, ciudades, dato_a_consultar):
        """
        Constructor de la clase.
        
        Args:
            api_key (str): La clave de la API de OpenWeatherMap.
            ciudades (list): Una lista de nombres de ciudades para consultar.
            dato_a_consultar (str): El tipo de dato a obtener, 'temp' para temperatura o 'humedad' para humedad.
        """
        self.api_key = api_key
        self.ciudades = ciudades
        # La lista que almacenará las tuplas (valor, ciudad)
        self.datos_climaticos = []
        self.dato_a_consultar = dato_a_consultar
    
    def obtener_datos(self):
        """
        Consulta la API de OpenWeatherMap para cada ciudad en la lista.
        
        Realiza una petición HTTP para cada ciudad, procesa la respuesta JSON
        y extrae el valor del dato solicitado (temperatura o humedad).
        Los resultados se guardan en una lista de tuplas.
        
        Returns:
            list: Una lista de tuplas donde cada tupla contiene el valor del dato
                  climático y el nombre de la ciudad, por ejemplo (25.5, 'Bogota').
        """
        print(f"Obteniendo {self.dato_a_consultar} de las ciudades...")
        for ciudad in self.ciudades:
            try:
                # Construye el enlace de la API con la ciudad, país (CO), clave y unidades métricas.
                link = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad},CO&appid={self.api_key}&units=metric&lang=es"
                peticion = requests.get(link)
                resultado = peticion.json()
                
                # Verifica si la petición fue exitosa (código de estado 200).
                if peticion.status_code == 200:
                    if self.dato_a_consultar == 'humedad':
                        # Accede al valor de humedad en el JSON.
                        valor = resultado['main']['humidity']
                        self.datos_climaticos.append((valor, ciudad))
                        print(f"  ✅ Ciudad: {ciudad} - Humedad: {valor}%")
                    elif self.dato_a_consultar == 'temp':
                        # Accede al valor de temperatura en el JSON.
                        valor = resultado['main']['temp']
                        self.datos_climaticos.append((valor, ciudad))
                        print(f"  ✅ Ciudad: {ciudad} - Temperatura: {valor}°C")
                else:
                    # Muestra un mensaje si la API no devuelve un resultado exitoso.
                    print(f"  ❌ No se pudo obtener el dato para {ciudad}.")
            except requests.exceptions.RequestException as e:
                # Captura y muestra errores de conexión o de la petición.
                print(f"  ❌ Error de conexión para {ciudad}: {e}")
        return self.datos_climaticos

class Ordenador:
    """
    Contiene todos los métodos de ordenamiento con visualización del proceso.
    Cada método manipula una lista de tuplas (valor, ciudad) en su lugar.
    """
    def __init__(self, lista):
        """
        Constructor de la clase.
        
        Args:
            lista (list): Una lista de tuplas (valor, ciudad) que será ordenada.
        """
        self.lista = lista

    def burbuja(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento de burbuja.
        Compara y, si es necesario, intercambia elementos adyacentes repetidamente.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        n = len(self.lista)
        print(f"\n--- Ordenamiento de Burbuja {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        print(f"Lista inicial: {self.lista}")
        for i in range(n - 1):
            intercambio_hecho = False
            print(f"\n> Pasada {i+1}:")
            for j in range(0, n - i - 1):
                # Determina la condición de comparación según el orden (ascendente o descendente).
                comparacion = self.lista[j][0] > self.lista[j+1][0] if ascendente else self.lista[j][0] < self.lista[j+1][0]
                
                if comparacion:
                    # Si la condición es True, realiza el intercambio de los elementos.
                    print(f"  🔄 Intercambiando {self.lista[j][0]} ({self.lista[j][1]}) y {self.lista[j+1][0]} ({self.lista[j+1][1]}).")
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
                    intercambio_hecho = True
            
            print(f"  ✅ Estado después de la pasada {i+1}: {self.lista}")
            # Si no hubo intercambios en una pasada completa, la lista ya está ordenada.
            if not intercambio_hecho:
                print("\n  👍 Lista ordenada. Finalizando.")
                break
        return self.lista

    def seleccion(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento por selección.
        En cada pasada, encuentra el elemento extremo (mínimo o máximo) en la parte no ordenada
        y lo coloca en su posición correcta.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        n = len(self.lista)
        print(f"\n--- Ordenamiento por Selección {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        print(f"Lista inicial: {self.lista}")
        for i in range(n):
            idx_extremo = i
            print(f"\n> Pasada {i+1}: Buscando el elemento {'mínimo' if ascendente else 'máximo'} en la sublista {self.lista[i:]}")
            for j in range(i + 1, n):
                # Compara el elemento actual con el 'extremo' encontrado hasta ahora.
                comparacion = self.lista[j][0] < self.lista[idx_extremo][0] if ascendente else self.lista[j][0] > self.lista[idx_extremo][0]
                if comparacion:
                    idx_extremo = j
            if idx_extremo != i:
                # Realiza el intercambio si se encontró un nuevo elemento extremo.
                print(f"  🔄 Intercambiando {self.lista[i][0]} ({self.lista[i][1]}) con el elemento {'mínimo' if ascendente else 'máximo'} {self.lista[idx_extremo][0]} ({self.lista[idx_extremo][1]}).")
                self.lista[i], self.lista[idx_extremo] = self.lista[idx_extremo], self.lista[i]
            else:
                print(f"  El elemento en la posición {i} ya es el correcto.")
            print(f"  ✅ Estado de la lista: {self.lista}")
        return self.lista

    def insercion(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento por inserción.
        Toma un elemento de la lista y lo inserta en su posición correcta
        dentro de la parte ya ordenada.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        n = len(self.lista)
        print(f"\n--- Ordenamiento por Inserción {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        print(f"Lista inicial: {self.lista}")
        for i in range(1, n):
            key = self.lista[i]
            j = i - 1
            print(f"\n> Pasada {i}: Tomando {key} para insertar.")
            
            while j >= 0:
                # Mueve los elementos mayores (o menores, si es descendente) que la clave una posición a la derecha.
                comparacion = (self.lista[j][0] > key[0]) if ascendente else (self.lista[j][0] < key[0])
                if comparacion:
                    print(f"  ➡️ Moviendo {self.lista[j][0]} a la derecha.")
                    self.lista[j+1] = self.lista[j]
                    j -= 1
                else:
                    break
            self.lista[j + 1] = key
            print(f"  ✅ Insertado {key[0]} ({key[1]}) en la posición {j+1}. Estado: {self.lista}")
        return self.lista

    def merge_sort(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento Merge Sort.
        Es un algoritmo recursivo que divide la lista en mitades, las ordena, y luego las fusiona.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        print(f"\n--- Ordenamiento Merge Sort {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        
        # Función auxiliar recursiva para la lógica de merge sort.
        def merge(arr, ascendente):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]
                
                print(f"  ▶️ Dividiendo: Izquierda: {L}, Derecha: {R}")
                # Llamadas recursivas para dividir las sublistas.
                merge(L, ascendente)
                merge(R, ascendente)
                
                i = j = k = 0
                # Fusiona las dos sublistas ordenadas.
                while i < len(L) and j < len(R):
                    comparacion = L[i][0] < R[j][0] if ascendente else L[i][0] > R[j][0]
                    if comparacion:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                
                # Copia los elementos restantes, si los hay.
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
                print(f"  ➕ Fusionando: {arr}")
            return arr

        merge(self.lista, ascendente)
        return self.lista

    def quick_sort(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento Quick Sort.
        Selecciona un 'pivote' y particiona la lista alrededor de él,
        colocando elementos menores/mayores en sublistas separadas y luego
        ordenándolas de forma recursiva.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        print(f"\n--- Ordenamiento Quick Sort {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")

        def _quick_sort(arr, ascendente):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[0]
                print(f"  🎯 Pivot: {pivot}")
                
                # Crea sublistas de elementos menores y mayores que el pivote.
                if ascendente:
                    menores = [x for x in arr[1:] if x[0] <= pivot[0]]
                    mayores = [x for x in arr[1:] if x[0] > pivot[0]]
                else:
                    menores = [x for x in arr[1:] if x[0] >= pivot[0]]
                    mayores = [x for x in arr[1:] if x[0] < pivot[0]]
                
                print(f"  Sublista de {'menores' if ascendente else 'mayores'}: {menores}")
                print(f"  Sublista de {'mayores' if ascendente else 'menores'}: {mayores}")
                
                # Llamada recursiva y combinación de las sublistas.
                sublista_ordenada = _quick_sort(menores, ascendente) + [pivot] + _quick_sort(mayores, ascendente)
                print(f"  🔄 Combinando sublistas: {sublista_ordenada}")
                return sublista_ordenada

        # Reemplaza el contenido de la lista original con la lista ordenada.
        self.lista[:] = _quick_sort(self.lista, ascendente)
        return self.lista

    def counting_sort(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento Counting Sort.
        Funciona para datos enteros en un rango limitado.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        print(f"\n--- Ordenamiento Counting Sort {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        
        arr = self.lista
        if not arr: return arr
        
        # Redondea los valores a enteros para que el algoritmo funcione.
        valores = [t[0] for t in arr]
        valores_enteros = [int(round(v)) for v in valores]
        
        max_val = max(valores_enteros)
        min_val = min(valores_enteros)
        rango = max_val - min_val + 1
        
        # Inicializa el arreglo de conteo y el arreglo de salida.
        count = [0] * rango
        salida = [None] * len(arr)
        
        print(f"Valores enteros para ordenar: {valores_enteros}")
        print(f"Rango de valores: {min_val} a {max_val}. Tamaño del arreglo de conteo: {rango}")

        # Paso 1: Cuenta las ocurrencias de cada elemento.
        for item in arr:
            num = int(round(item[0]))
            count[num - min_val] += 1
        
        print(f"1️⃣ Arreglo de conteo: {count}")
        
        # Paso 2: Modifica el arreglo de conteo para que contenga las posiciones de los elementos.
        if ascendente:
            for i in range(1, len(count)):
                count[i] += count[i-1]
        else:
            for i in range(len(count) - 2, -1, -1):
                count[i] += count[i+1]
        
        print(f"2️⃣ Arreglo de conteo acumulado: {count}")
        
        # Paso 3: Construye el arreglo de salida usando el arreglo de conteo acumulado.
        for i in range(len(arr) - 1, -1, -1):
            item = arr[i]
            num = int(round(item[0]))
            posicion = count[num - min_val] - 1
            salida[posicion] = item
            count[num - min_val] -= 1
        
        self.lista[:] = salida
        print(f"3️⃣ Arreglo final: {self.lista}")
        return self.lista

    def radix_sort(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento Radix Sort.
        Funciona ordenando los números dígito por dígito, de derecha a izquierda.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        print(f"\n--- Ordenamiento Radix Sort {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        
        # Adapta los valores flotantes a enteros para aplicar el algoritmo.
        lista_tuplas_enteros = [(int(round(t[0] * 100)), t[1]) for t in self.lista]
        print(f"Lista para ordenar: {lista_tuplas_enteros}")
        
        max_num = max(t[0] for t in lista_tuplas_enteros)
        exp = 1  # Exponente para el dígito actual (1, 10, 100, etc.)
        
        # Itera a través de los dígitos, del menos significativo al más significativo.
        while max_num // exp > 0:
            cubetas = [[] for _ in range(10)]
            print(f"\n> Pasada del dígito de las {exp}s:")
            
            # Distribuye los elementos en cubetas según el dígito actual.
            for item in lista_tuplas_enteros:
                digito = (item[0] // exp) % 10
                cubetas[digito].append(item)
            
            for i in range(10):
                print(f"  Cubeta {i}: {cubetas[i]}")

            # Concatena las cubetas para formar la nueva lista ordenada.
            salida = []
            if ascendente:
                for cubeta in cubetas:
                    salida.extend(cubeta)
            else:
                for cubeta in reversed(cubetas):
                    salida.extend(cubeta)
            
            lista_tuplas_enteros[:] = salida
            print(f"  ✅ Lista después de la pasada: {lista_tuplas_enteros}")
            exp *= 10
        
        # Convierte los valores de nuevo a su forma original (flotantes).
        self.lista[:] = [(t[0] / 100, t[1]) for t in lista_tuplas_enteros]
        return self.lista

    def heap_sort(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento Heap Sort.
        Construye un heap (montículo) y luego extrae repetidamente el elemento raíz
        para ordenar la lista.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        print(f"\n--- Ordenamiento Heap Sort {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        n = len(self.lista)

        # Función auxiliar para convertir un subárbol en un heap.
        def heapify(arr, tamano, i):
            extremo = i
            izq = 2 * i + 1
            der = 2 * i + 2
            
            # Para orden ascendente, se busca el elemento más grande (Max-Heap).
            if ascendente:
                if izq < tamano and arr[izq][0] > arr[extremo][0]:
                    extremo = izq
                if der < tamano and arr[der][0] > arr[extremo][0]:
                    extremo = der
            # Para orden descendente, se busca el elemento más pequeño (Min-Heap).
            else:
                if izq < tamano and arr[izq][0] < arr[extremo][0]:
                    extremo = izq
                if der < tamano and arr[der][0] < arr[extremo][0]:
                    extremo = der

            if extremo != i:
                # Si el elemento más grande/pequeño no es la raíz, se intercambian.
                arr[i], arr[extremo] = arr[extremo], arr[i]
                # Se llama recursivamente a heapify en el subárbol afectado.
                heapify(arr, tamano, extremo)

        # Paso 1: Construir el heap inicial.
        print("1️⃣ Construyendo el Heap:")
        # Bucle para convertir la lista en un heap. Se empieza por el último nodo padre.
        for i in range(n // 2 - 1, -1, -1):
            heapify(self.lista, n, i)
        print(f"  Heap inicial: {self.lista}")

        # Paso 2: Extraer elementos uno a uno para ordenar.
        print("\n2️⃣ Extrayendo elementos y ordenando:")
        for i in range(n - 1, 0, -1):
            # Intercambia el elemento raíz (el más grande/pequeño) con el último elemento.
            print(f"  🔄 Intercambiando la raíz ({self.lista[0][0]}) con el último elemento ({self.lista[i][0]}).")
            self.lista[i], self.lista[0] = self.lista[0], self.lista[i]
            # Reduce el tamaño del heap y llama a heapify en el subárbol restante.
            heapify(self.lista, i, 0)
            print(f"  Estado de la lista: {self.lista}")
            
        return self.lista

    def bucket_sort(self, ascendente=True):
        """
        Implementa el algoritmo de ordenamiento Bucket Sort.
        Divide los elementos en cubetas, ordena cada cubeta y luego las concatena.
        
        Args:
            ascendente (bool): Si es True, ordena de menor a mayor. Si es False, de mayor a menor.
        
        Returns:
            list: La lista ordenada.
        """
        print(f"\n--- Ordenamiento Bucket Sort {'(Menor a Mayor)' if ascendente else '(Mayor a Menor)'} ---")
        if not self.lista:
            return []
        
        valores = [t[0] for t in self.lista]
        min_val = min(valores)
        max_val = max(valores)
        # El número de cubetas se establece como el tamaño de la lista para una buena distribución.
        num_buckets = len(self.lista)
        buckets = [[] for _ in range(num_buckets)]
        
        print(f"Valores de la lista van de {min_val} a {max_val}.")
        print(f"Creando {num_buckets} cubetas.")
        
        if max_val != min_val:
            # Distribuye los elementos en las cubetas.
            for item in self.lista:
                # Calcula el índice de la cubeta para el elemento.
                idx = int((item[0] - min_val) * (num_buckets - 1) / (max_val - min_val))
                buckets[idx].append(item)
        else:
            # Si todos los valores son iguales, todos van a la primera cubeta.
            for item in self.lista:
                buckets[0].append(item)
        
        print("\n1️⃣ Distribución en las cubetas:")
        for i, bucket in enumerate(buckets):
            print(f"  Cubeta {i}: {bucket}")

        salida = []
        print("\n2️⃣ Ordenando cada cubeta y uniéndolas:")
        # Ordena cada cubeta y las concatena en la lista de salida.
        if ascendente:
            for i, bucket in enumerate(buckets):
                bucket.sort(key=lambda x: x[0])
                print(f"  Cubeta {i} ordenada: {bucket}")
                salida.extend(bucket)
        else:
            for i, bucket in reversed(list(enumerate(buckets))):
                bucket.sort(key=lambda x: x[0], reverse=True)
                print(f"  Cubeta {i} ordenada: {bucket}")
                salida.extend(bucket)
        
        self.lista[:] = salida
        print(f"  ✅ Lista final: {self.lista}")
        return self.lista

# --- LÓGICA PRINCIPAL DEL PROGRAMA ---
if __name__ == "__main__":
    # Lista de ciudades a consultar.
    ciudades = ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira", "Santa Marta", "Manizales", "Villavicencio"]
    # Clave de API de OpenWeatherMap.
    api_key = "3c961419c5a90e5649266ae986c5ba85"
    # Pide al usuario el tipo de dato para ordenar.
    dato = input("Ingrese 'temp' para ordenar por temperatura o 'humedad' para ordenar por humedad: ")

    # Crea una instancia de la clase de consulta de datos.
    consulta = ConsultaDatosClimaticos(api_key, ciudades, dato)
    # Llama al método para obtener los datos.
    lista_de_datos = consulta.obtener_datos()

    if not lista_de_datos:
        print("No se obtuvieron datos para ordenar. Saliendo.")
    else:
        # Bucle principal para el menú interactivo.
        while True:
            print("\n" + "="*50)
            print("         MENÚ DE ORDENAMIENTO DE DATOS CLIMÁTICOS")
            print("="*50)
            print("1. Burbuja")
            print("2. Selección")
            print("3. Inserción")
            print("4. Merge Sort")
            print("5. Quick Sort")
            print("6. Counting Sort")
            print("7. Radix Sort")
            print("8. Heap Sort")
            print("9. Bucket Sort")
            print("0. Salir")
            
            opcion = input("Elige un método de ordenamiento (0-9): ")
            
            if opcion == '0':
                print("¡Hasta la próxima!")
                break
            
            if opcion in [str(i) for i in range(1, 10)]:
                try:
                    # Pide la dirección de ordenamiento.
                    orden = input("¿Ordenar de forma ascendente (a) o descendente (d)? ").lower()
                    ascendente = (orden == 'a')
                    
                    # Crea una copia de la lista para no alterar la original en cada ordenamiento.
                    lista_copia = lista_de_datos.copy()
                    ordenador = Ordenador(lista_copia)
                    
                    # Llama al método de ordenamiento seleccionado por el usuario.
                    if opcion == '1': lista_ordenada = ordenador.burbuja(ascendente)
                    elif opcion == '2': lista_ordenada = ordenador.seleccion(ascendente)
                    elif opcion == '3': lista_ordenada = ordenador.insercion(ascendente)
                    elif opcion == '4': lista_ordenada = ordenador.merge_sort(ascendente)
                    elif opcion == '5': lista_ordenada = ordenador.quick_sort(ascendente)
                    elif opcion == '6': lista_ordenada = ordenador.counting_sort(ascendente)
                    elif opcion == '7': lista_ordenada = ordenador.radix_sort(ascendente)
                    elif opcion == '8': lista_ordenada = ordenador.heap_sort(ascendente)
                    elif opcion == '9': lista_ordenada = ordenador.bucket_sort(ascendente)
                    
                    # Muestra el resultado final.
                    print("\n--- ¡ORDENAMIENTO FINALIZADO! ---")
                    print(f"Lista final ordenada: {lista_ordenada}")
                    
                except Exception as e:
                    print(f"Error inesperado: {e}")
            else:
                print("Opción no válida. Intenta de nuevo.")
