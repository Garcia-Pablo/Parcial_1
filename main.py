
import time
import statistics
import random


# Super clase - Clase padre
class ListaAvanzada:

    # Método constructor
    def __init__(self,lista):
        self.lista = lista

    # Método mágico __str__
    def __str__(self):
        return str(self.lista[:10])

    # Método mágico __len__
    def __len__(self):
        return len(self.lista)

    def __getitem__(self, indice):
        if 0 <= indice < len(self.lista):
            return self.lista[indice]
        else:
            raise IndexError("Índice fuera de rango")

    def __setitem__(self, indice, valor):
        if 0 <= indice < len(self.lista):
            self.lista[indice] = valor
        else:
            raise IndexError("Índice fuera de rango")

    @staticmethod
    # Función para mantener la lista original
    def lista_segura(lista):
        return list(lista)


    # Implementa la búsqueda lineal en la lista
    def busqueda_lineal(self, elemento):
        for i in range(len(self.lista)):
            if self.lista[i] == elemento:
                return i  # Índice donde se encuentra el elemento
        return -1  # El elemento no está en la lista


    # Implementa la búsqueda binaria en la lista (requiere que la lista esté ordenada)
    def busqueda_binaria(self, elemento):
        """Búsqueda binaria
        Devuelve -1 si el elemento no está en lista;
        """

        izq = 0 # izq guarda el índice inicio del segmento
        der = len(self.lista) -1 # der guarda el índice fin del segmento

        while izq <= der:
            # el punto medio del segmento
            medio = (izq+der)//2

            # si el medio es igual al valor buscado, lo devuelve
            if self.lista[medio] == elemento:
                return medio
            elif self.lista[medio] > elemento:
                der = medio-1
            else:
                izq = medio+1
        return -1

    def sumar_elementos(self):
        return sum(self.lista)

    def calcular_promedio(self):
        return statistics.mean(self.lista)

    def calcular_mediana(self):
        # Implementa el cálculo de la mediana
        return statistics.median(self.lista)

    def calcular_varianza(self):
        # Implementa el cálculo de la varianza
        return statistics.pvariance(self.lista)

    def encontrar_valor_minimo(self):
        return min(self.lista)

    def encontrar_valor_maximo(self):
        return max(self.lista)

    def comparar_con_otra_lista(self, otra_lista):
        # Implementa la comparación de esta lista con otra_lista
        lista_2 = ListaAvanzada(otra_lista)
        if self.lista == lista_2:
            print("Las listas son iguales")
        else:
            print("Las listas son diferentes")

# Comparar los atributos relevantes de los objetos
    def __eq__(self,obj):
        if isinstance(obj,ListaAvanzada):
            if self.lista == obj.lista:
                return True
            else:
                return False

# Clase hija - subclase
class OrdenarLista(ListaAvanzada):

    # Método constructor
    def __init__(self,lista):
        super().__init__(lista)
        self.lista_burbuja = lista

    def __str__(self):
        super().__str__()

    # Función para ordenar con burbuja
    def ordenamiento_burbuja(self):
        """Esta función ordenara la lista con el Método de ordenamiento tipo burbuja"""
        tiempo_1 = time.time()
        n = len(self.lista_burbuja)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.lista_burbuja[j] > self.lista_burbuja[j + 1]:
                    self.lista_burbuja[j], self.lista_burbuja[j + 1] = self.lista_burbuja[j + 1], self.lista_burbuja[j]
        tiempo_2 = time.time()
        tiempo_burbuja = tiempo_2 - tiempo_1
        men_list = f"Lista ordenada con burbuja (primeros 10 elementos):{self.lista_burbuja}"
        men_tiempo = f"\nTiempo de ejecución con burbuja: {tiempo_burbuja} segundos"
        return men_list, men_tiempo

    # Implementa el algoritmo de ordenamiento tipo lineal (por ejemplo, seleccion tipo 'sort')
    def ordenar_rapido(self):
        """Esta función ordenara el vector que le pases como argumento 
        con el Método rapido_orden 'Sort'"""
        tiempo_1 = time.time()
        lista_rapida = self.lista
        
        def rapido_orden(lista_rapida, inicio = 0, fin = len(lista_rapida) - 1):
            
            if inicio >= fin:
                return

            def particion(lista_rapida, inicio = 0, fin = len(lista_rapida) - 1):
                pivot = lista_rapida[inicio]
                menor = inicio + 1
                mayor = fin

                while True:
                    # Si el valor actual es mayor que el pivot
                    # está en el lugar correcto (lado derecho del pivot) y podemos 
                    # movernos hacia la izquierda, al siguiente elemento.
                    # También nos aseguramos de no haber superado el limite, ya que indica 
                    # que ya hemos movido todos los elementos a su lado correcto del pivot
                    while menor <= mayor and lista_rapida[mayor] >= pivot:
                        mayor = mayor - 1

                    # Proceso opuesto al anterior            
                    while menor <= mayor and lista_rapida[menor] <= pivot:
                        menor = menor + 1

                    # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                    # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                    if menor <= mayor:
                        lista_rapida[menor], lista_rapida[mayor] = lista_rapida[mayor], lista_rapida[menor]
                        # Continua el bucle
                    else:
                        # Salimos del bucle
                        break

                lista_rapida[inicio], lista_rapida[mayor] = lista_rapida[mayor], lista_rapida[inicio]
                
                return mayor
            
            p = particion(lista_rapida, inicio, fin)
            rapido_orden(lista_rapida, inicio, p-1)
            rapido_orden(lista_rapida, p+1, fin)
            
        rapido_orden(lista_rapida)
        tiempo_2 = time.time()
        tiempo_rapido = tiempo_2 - tiempo_1
        men_list = f"Lista ordenada con rápido: {lista_rapida}"
        men_tiempo = f"\nTiempo de ejecución con rapido: {tiempo_rapido} segundos"
        return men_list, men_tiempo

    @classmethod 
    def comparar_sorted(cls,lista,tiempo1,tiempo2):
        # 
        tiempo_1 = time.time()
        lista_segura = cls.lista_segura(lista)
        sorted(lista_segura)
        tiempo_2 = time.time()
        tiempo_sorted = tiempo_2 - tiempo_1
        # try:
        print(tiempo1,tiempo2)
        print(f"Tiempo de ejecución con sorted: {tiempo_sorted} segundos\nComparación de tiempos realizada.")
        # except UnboundLocalError:
        #     print("Primero debe ejecutar los ordenamientos con burbuja (b) y con rapido (c)")


# Función para validar un número entero
def num_entero(num):
    try:
        # Se intenta convertir el numero ingresado (string) a entero
        int(num)
        return int(num)
    # Si no es posible, implica que el valor ingresado no puede ser un numero entero
    except ValueError:
        print("El número ingresado no es un número entero")

# Función para validar las opciones del menú 1
def validar_menu1(num,n_opciones):
    try:
        # Se usa valida que el opcion seleccionada de menú sea un número entero
        menu = num_entero(num)
        # Si la opcion ingresada no esta en el rango del menú se "instancia un ValueError"
        if menu not in range(1, (n_opciones+1)):
            raise ValueError("\nEl valor ingresado no es una opción del menú")
    except ValueError as mes:
        print(mes)
    # Si el ValueError no se evoca se retorna el valor seleccionado de menú
    else:
        return menu

# Función para validar un caracter
def caracter(char):
    try:
        # Se verifica que el dato ingresado sea una sola letra
        if char.isalpha() and len(char)==1:
            return char
        else:
            raise ValueError("\nEl dato ingresado debe ser una sola letra")
    # Si no es posible, implica que el valor dato no es una única letra
    except ValueError as mes:
        print(mes)

# Función para validar las opciones del menú 2
def validar_menu2(char,n_opciones):
    try:
        # Se usa valida que el opcion seleccionada de menú sea un número entero
        menu = caracter(char)

        # Generar letras del alfabeto en minúsculas desde a - o
        letras_min = [chr(i) for i in range(97, 97 + n_opciones)]

        # Si la opcion ingresada no esta en el rango del menú se "instancia un ValueError"
        if menu not in letras_min:
            raise ValueError("\nEl valor ingresado no es una opción del menú")
    except ValueError as mes:
        print(mes)
    # Si el ValueError no se evoca se retorna el valor seleccionado de menú
    else:
        return menu

def obtener_lista_enteros():
    while True:
        entrada = input("Ingrese la lista de números enteros separados por espacios: ")
        elementos = entrada.split()  # Dividir la entrada en elementos individuales
        
        # Intentar convertir los elementos en números enteros
        try:
            numeros_enteros = [int(elemento) for elemento in elementos]
            return numeros_enteros  # Si se convierte correctamente, retornar la lista de enteros
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números enteros separados por espacios.")


#
def submenu():
    while True:
        menu = input("\nSubmenú:\na. Imprimir lista\nb. Ordenar la lista con burbuja\nc. Ordenar la lista con rápido\nd. Comparar con sorted()\ne. Buscar elemento (búsqueda lineal)\nf. Buscar elemento (búsqueda binaria)\ng. Sumar elementos\nh. Calcular promedio\ni. Calcular mediana\nj. Calcular varianza\nk. Encontrar el valor mínimo\nl. Encontrar el valor máximo\nm. Mostrar longitud de la lista\nn. Comparar con otra lista\no. Volver al menú principal\nSeleccione una opción: ")
        opcion = validar_menu2(menu,15)  

        if opcion == 'a':
            print(f"Lista cargada actualmente (primeros 10 elementos):{lista_original[:10]}")

        elif opcion == 'b':
            lista_orden = OrdenarLista(mi_lista)
            lista_burbuja , tiempo_ejecucion_1 = lista_orden.ordenamiento_burbuja()
            print(lista_burbuja, tiempo_ejecucion_1)

        elif opcion == 'c':
            lista_orden = OrdenarLista(mi_lista)
            lista_rapida, tiempo_ejecucion_2 = lista_orden.ordenar_rapido()
            print(lista_rapida, tiempo_ejecucion_2)

        elif opcion == 'd':
            lista_orden = OrdenarLista(mi_lista)

            try:
                lista_orden.comparar_sorted(lista_orden,tiempo_ejecucion_1,tiempo_ejecucion_2)
            except UnboundLocalError:
                print("Primero debe ejecutar los ordenamientos con burbuja (b) y con rapido (c)")

        elif opcion == 'e':
            elemento = num_entero(input("Ingrese el dato que desea encontrar: "))
            lista_busqueda = ListaAvanzada(mi_lista)
            tiempo_1 = time.time()
            posicion = lista_busqueda.busqueda_lineal(elemento)
            tiempo_2 = time.time()
            tiempo_lineal = tiempo_2 - tiempo_1
            print(f"\nTiempo de ejecución busqueda lineal: {tiempo_lineal} segundos")

            if posicion == -1:
                print("El elemento no se encuentra en la lista")
            else:
                print(f"La posición en la lista en donde se encuentra el elemento es: {posicion}")

        elif opcion == 'f':
            elemento = num_entero(input("Ingrese el dato que desea encontrar: "))
            lista_busqueda = ListaAvanzada(mi_lista)
            tiempo_1 = time.time()
            posicion = lista_busqueda.busqueda_binaria(elemento)
            tiempo_2 = time.time()
            tiempo_lineal = tiempo_2 - tiempo_1
            print(f"\nTiempo de ejecución busqueda binaria: {tiempo_lineal} segundos")

            if posicion == -1:
                print("El elemento no se encuentra en la lista")
            else:
                print(f"La posición en la lista en donde se encuentra el elemento es: {posicion}")

        elif opcion == 'g':
            lista_suma = ListaAvanzada(mi_lista)
            suma = lista_suma.sumar_elementos()
            print(f"La suma de los elementos en la lista es: {suma}")

        elif opcion == 'h':
            lista_promedio = ListaAvanzada(mi_lista)
            promedio = lista_promedio.calcular_promedio()
            print(f"El promedio de los elementos en la lista es: {promedio}")

        elif opcion == 'i':
            lista_mediana = ListaAvanzada(mi_lista)
            mediana = lista_mediana.calcular_mediana()
            print(f"La mediana de los elementos en la lista es: {mediana}")

        elif opcion == 'j':
            lista_varianza = ListaAvanzada(mi_lista)
            varianza = lista_varianza.calcular_varianza()
            print(f"La varianza de los elementos en la lista es: {varianza}")

        elif opcion == 'k':
            lista_min = ListaAvanzada(mi_lista)
            valor_min = lista_min.encontrar_valor_minimo()
            print(f"El valor mínimo entre los elementos de la lista es: {valor_min}")

        elif opcion == 'l':
            lista_max = ListaAvanzada(mi_lista)
            valor_max = lista_max.encontrar_valor_maximo()
            print(f"El valor máximo entre los elementos de la lista es: {valor_max}")

        elif opcion == 'm':
            lista_len = ListaAvanzada(mi_lista)
            longitud = len(lista_len) 
            print(f"La longitud de la lista es: {longitud}")

        elif opcion == 'n':
            lista_1 = ListaAvanzada(mi_lista)
            lista_ingresada = obtener_lista_enteros()
            lista_1.comparar_con_otra_lista(lista_ingresada)

        elif opcion == 'o':
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    
    while True:
        menu = input("\nMenú Principal:\n1. Generar lista aleatoria\n2. Ingresar lista manualmente\n3. Usar lista previamente cargada\n4. Crear lista desde rango\n5. Ayuda\n6. Salir\nSeleccione una opción: ")
        opcion = validar_menu1(menu,6)
        if opcion == 1:
            tamano = num_entero(input("Ingrese el tamaño de la lista: "))
            if tamano != None:
                lista_aleatoria = [random.randint(0, 10000) for _ in range(tamano)]
                mi_lista = ListaAvanzada(lista=lista_aleatoria)
                lista_original = ListaAvanzada.lista_segura(lista_aleatoria)
                print(f"Lista generada (primeros 10 elementos): {lista_original[:10]}")
                submenu()
        elif opcion == 2:
            lista_manual = obtener_lista_enteros()
            mi_lista = ListaAvanzada(lista=lista_manual)
            lista_original = ListaAvanzada.lista_segura(lista_manual)
            print(f"Lista ingresada manualmente (primeros 10 elementos): {lista_original[:10]}")
            submenu()
        elif opcion == 3:
            if lista_original != None:
                print(f"Lista actual (primeros 10 elementos): {lista_original[:10]}")
            submenu()
        elif opcion == 4:
            inicio = num_entero(input("Ingrese el punto inicial: "))
            final = num_entero(input("Ingrese el punto final: "))
            tamano = num_entero(input("Ingrese el tamaño de la lista: "))
            if tamano != None:
                lista_aleatoria = [random.randint(inicio, final) for _ in range(tamano)]
                mi_lista = ListaAvanzada(lista=lista_aleatoria)
                lista_original = ListaAvanzada.lista_segura(lista_aleatoria)
                print(f"Lista generada (primeros 10 elementos): {lista_original[:10]}")
                submenu()
        elif opcion == 5:
            print("Ayuda:\nLa búsqueda lineal recorre la lista de principio a fin hasta encontrar el número.\nLa búsqueda binaria requiere que la lista esté ordenada y encuentra el elemento dividifino la lista en mitades.\nEl ordenamiento por burbuja compara pares de elementos adyacentes y los intercambia si están en orden incorrecto.\nEl ordenamiento rápido utiiza un elemento 'pivote' para dividir la lista y ordenarla de manera más eficiente.\n")
        elif opcion == 6:
            print("Adiós, Vuelva pronto\n")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    
