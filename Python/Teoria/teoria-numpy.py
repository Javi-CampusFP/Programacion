# Importar libreria escrita en C 
import numpy as np
# Función porque quiero separar los outputs
def linea():
    print("---------------")
# Crear listas para ver su diferencia
mi_lista = [1, 2, 3, 4]
mi_array = np.array(mi_lista)
print(mi_lista)
print(mi_array)
# Trata los datos como un array, no como una lista con sus ','
linea()
# Crear una matriz para ver como se comporta
mi_matriz = np.array([[1,2,3],[4,5,6]])
print(mi_matriz)

linea()
# Crea una matriz de ceros con 3 filas y 5 columnas
ceros = np.zeros((3,5))
print(ceros)
linea()
# Lo mismo que el cero pero con 1
unos = np.ones((3,5))
print(unos)
linea()
# Puedes sumar los valores de las matrices
nueva = ceros + unos
print(nueva)
linea()
# Acceder a los valores de la matriz
nueva[1,3] = 5
print(nueva)
linea()
# Secuencia de numeros
# Se genera una secuencia de números saltandose un número cada 2 hasta el 10. 
secuencia = np.arange(0,10,2)
print(secuencia)
linea()
# Saca valores en el rango de 0 a 1 dividiendolo 5 veces
valores = np.linspace(0,1,5)
print(valores)
linea()
# Creamos 2 listas
lista = [5,12,3,18,7,20,9]
array = np.array([5,12,3,18,7,20,9])
# Primera solución, sin numpy
lista2 = []
for articulo in lista:
    if articulo > 10:
        lista2.append(articulo)
print(lista2)
linea()
# El de numpy es mucho más conciso
nuevo_array = array[array > 10]
print(nuevo_array)

