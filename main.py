
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

    @property
    def lista_segura(self):
        return self.lista


    

    # def buscar_elemento_lineal(self, elemento):
    #     # Implementa la búsqueda lineal en la lista
    # def busqueda_lineal(lista, elemento):
    #     for i in range(len(lista)):
    #         if lista[i] == elemento:
    #             return i  # Índice donde se encuentra el elemento
    #     return -1  # El elemento no está en la lista

    # def linearSearch(item,my_list):
    #     found = False
    #     position = 0
    #     while position < len(my_list) and not found:
    #         if my_list[position] == item:
    #             found = True
    #         position = position + 1
    #     return found

    # def buscar_elemento_binaria(self, elemento):
    #     # Implementa la búsqueda binaria en la lista (requiere que la lista esté ordenada)
    # def busqueda_binaria(lista, elemento):
    #     izquierda, derecha = 0, len(lista) - 1
    #     while izquierda <= derecha:
    #         medio = (izquierda + derecha) // 2
    #         if lista[medio] == elemento:
    #             return medio  # Índice donde se encuentra el elemento
    #         elif lista[medio] < elemento:
    #             izquierda = medio + 1
    #         else:
    #             derecha = medio - 1
    #     return -1  # El elemento no está en la lista


    

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

    def mostrar_longitud(self):
        return len(self.lista)

    def comparar_con_otra_lista(self, otra_lista):
        # Implementa la comparación de esta lista con otra_lista
        pass

    # class MiClase:
    # def __init__(self, valor):
    #     self.valor = valor

    # def __eq__(self, other):
    #     if isinstance(other, MiClase):
    #         # Comparar los atributos relevantes de los objetos
    #         return self.valor == other.valor
    #     return False  # Si 'other' no es una instancia de MiClase, considerar que no son iguales

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
        tiempo_3 = tiempo_2 - tiempo_1
        print(f"Lista ordenada con burbuja (primeros 10 elementos):{self.lista_burbuja}\nTiempo de ejecución para burbuja: {tiempo_3} segundos")

    def ordenar_lineal(self):
        # Implementa el algoritmo de ordenamiento tipo lineal (por ejemplo, selection sort)
        tiempo_1 = time.time()
        vectorquick = self.lista
        def quicksort(vectorquick, start = 0, end = len(vectorquick) - 1 ):
            """Esta función ordenara el vector que le pases como argumento 
            con el Método Quick Sort"""
            
            def quick(vectorquick, start = 0, end = len(vectorquick) - 1):
                
                
                if start >= end:
                    return

                def particion(vectorquick, start = 0, end = len(vectorquick) - 1):
                    pivot = vectorquick[start]
                    menor = start + 1
                    mayor = end

                    while True:
                        # Si el valor actual es mayor que el pivot
                        # está en el lugar correcto (lado derecho del pivot) y podemos 
                        # movernos hacia la izquierda, al siguiente elemento.
                        # También nos aseguramos de no haber superado el limite, ya que indica 
                        # que ya hemos movido todos los elementos a su lado correcto del pivot
                        while menor <= mayor and vectorquick[mayor] >= pivot:
                            mayor = mayor - 1

                        # Proceso opuesto al anterior            
                        while menor <= mayor and vectorquick[menor] <= pivot:
                            menor = menor + 1

                        # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                        # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                        if menor <= mayor:
                            vectorquick[menor], vectorquick[mayor] = vectorquick[mayor], vectorquick[menor]
                            # Continua el bucle
                        else:
                            # Salimos del bucle
                            break

                    vectorquick[start], vectorquick[mayor] = vectorquick[mayor], vectorquick[start]
                    
                    return mayor
                
                p = particion(vectorquick, start, end)
                quick(vectorquick, start, p-1)
                quick(vectorquick, p+1, end)
                
            quick(vectorquick)
            tiempo_2 = time.time()
            tiempo_3 = tiempo_2 - tiempo_1
            print(f"Lista ordenada con rápido: {vectorquick}\nTiempo de ejecución para burbuja: {tiempo_3} segundos")
        quicksort(vectorquick)

    def comparar_sorted(self):
        self.lista = sorted(self.lista)
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

#
def submenu():
    while True:
        menu = input("\nSubmenú:\na. Imprimir lista\nb. Ordenar la lista con burbuja\nc. Ordenar la lista con rápido\nd. Comparar con sorted()\ne. Buscar elemento (búsqueda lineal)\nf. Buscar elemento (búsqueda binaria)\ng. Sumar elementos\nh. Calcular promedio\ni. Calcular mediana\nj. Calcular varianza\nk. Encontrar el valor mínimo\nl. Encontrar el valor máximo\nm. Mostrar longitud de la lista\nn. Comparar con otra lista\no. Volver al menú principal\nSeleccione una opción: ")
        opcion = validar_menu2(menu,15)  
# a. Imprimir lista
# b. Ordenar la lista tipo burbuja
# c. Ordenar la lista tipo lineal
# d. Ordenar con sorted()
# e. Buscar elemento (búsqueda lineal)
# f. Buscar elemento (búsqueda binaria)
# g. Sumar elementos
# h. Calcular promedio
# i. Calcular mediana
# j. Calcular varianza
# k. Encontrar el valor mínimo
# l. Encontrar el valor máximo
# m. Mostrar longitud de la lista
# n. Comparar con otra lista
        if opcion == 'a':
            print(f"Lista cargada actualmente (primeros 10 elementos):{mi_lista}")
        elif opcion == 'b':
            lista_orden = OrdenarLista(mi_lista)
            lista_orden.ordenamiento_burbuja()

        elif opcion == 'c':
            lista_orden = OrdenarLista(mi_lista)
            lista_orden.ordenar_lineal()
        elif opcion == 'd':
            lista_orden = OrdenarLista(mi_lista)
            lista_orden.comparar_sorted()
        elif opcion == 'e':
            pass
        elif opcion == 'f':
            pass
        elif opcion == 'g':
            pass
        elif opcion == 'h':
            pass
        elif opcion == 'i':
            pass
        elif opcion == 'j':
            pass
        elif opcion == 'k':
            pass
        elif opcion == 'l':
            pass
        elif opcion == 'm':
            pass
        elif opcion == 'n':
            pass
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
                # mi_lista.imprimir_lista()
                print(f"Lista generada (primeros 10 elementos): {mi_lista}")
                submenu()
        elif opcion == 2:
            submenu()
        elif opcion == 3:
            submenu()
        elif opcion == 4:
            submenu()
        elif opcion == 5:
            print("Ayuda:\nLa búsqueda lineal recorre la lista de principio a fin hasta encontrar el número.\nLa búsqueda binaria requiere que la lista esté ordenada y encuentra el elemento dividiendo la lista en mitades.\nEl ordenamiento por burbuja compara pares de elementos adyacentes y los intercambia si están en orden incorrecto.\nEl ordenamiento rápido utiiza un elemento 'pivote' para dividir la lista y ordenarla de manera más eficiente.\n")
        elif opcion == 6:
            print("Adiós, Vuelva pronto\n")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    
