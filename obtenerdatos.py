# Librerías necesarias
import numpy as np              # Tratamiento de arreglos numéricos
import pandas as pd             # Tratamiento de grandes cantidades de información
import matplotlib.pyplot as mp  # Tratamiento de gráficas

# Dirección con el archivo CSV para tratar
# CSV (Comma Separated Values) son archivos que contienen grandes cantidades
# de información, los cuales se almacenan en texto plano y están separados
# los datos por (',') comas y las filas de datos están separadas por saltos de
# línea ('\n')
urlDescarga = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# Con la dirección URL de descarga, proceder a obtener los datos direcamente
# de la Web
df = pd.read_csv(urlDescarga)

# Mostrar las primeras 5 filas de datos
df.head()
# Los datos como se puede observar estásn encbezados por un título en cada una 
# de las columnas y los datos organizados en una tabla

# Ahora, solo se obtendrán los datos para un solo país (en este caso Méxicalpan de las tunas)
# Se coloca el nombre de la columna y se iguala a un valor
datosMexico = df[df['location'] == 'Mexico']

# Mostrar las primeras 5 filas
datosMexico.head()

# Se obtiene una lista con todas las fechas
fechas = datosMexico['date'].tolist()

# Se obtiene una lista con los nuevos casos
# Aquí cabe aclarar que en esta columna aparecen datos del tipo NaN (Not a Number)
# los cuales son datos perdidos o no proporcionados
# se puede utilizar la instrucción:
#    datosMexico['total_cases'].isnull().values.any()
# para preguntar si hay valores NaN en la columna
# y la instrucción:
#    datosMexico['total_cases'].isnull().sum()
# para conocer la cantidad
# Si se halla alguno, entonces se aplica la función fillna(k) donde se remplazan
# esos datos por el valor 'k'
totalCasos = datosMexico['total_cases']
if totalCasos.isnull().values.any():
  totalCasos = totalCasos.fillna(0).tolist()
else:
  totalCasos = totalCasos.fillna(0).tolist()

# Graficar fecha - nuevos casos
# Cambiar el tamaño de la gráfica
fig = mp.figure(figsize=(20,10))
# Graficar
mp.plot(fechas, totalCasos, '.')
mp.xlabel('Fecha')
mp.ylabel('Casos Totales')
# Rotar las etiquetas del eje x 90! para que se observen mejor
mp.xticks(rotation=90)
# Mostrar la gráfica
mp.show()

