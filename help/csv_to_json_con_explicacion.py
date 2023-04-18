import csv
import json
import os

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as f:
        fields = f.readline().strip().split(',')
        reader = csv.reader(f)
        data = list(reader)
    array = [dict(zip(fields, element)) for element in data]
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(array, indent=4))

if __name__ == '__main__':
    csv_to_json(
        os.path.join('data', 'cod_estacion.csv'),
        os.path.join('data', 'cod_estacion.json'),
    )
    

"""
Este script de Python convierte un archivo CSV en un archivo JSON.

La función (def) csv_to_json toma dos argumentos: el nombre del archivo CSV (csv_file) y el nombre del archivo JSON (json_file). En la primera línea, el archivo CSV se abre en modo de lectura ('r') y se lee la primera línea que contiene los nombres de las columnas. Estos nombres se almacenan en la lista fields. Luego, se crea un objeto csv.reader para leer el resto del archivo.

La siguiente línea lee todo el contenido del archivo utilizando el objeto csv.reader y lo almacena en la lista data. Cada elemento en data es una lista que representa una fila en el archivo CSV.

A continuación, se utiliza una comprensión de lista para crear una lista de diccionarios a partir de data. La función zip toma los elementos de fields y element y los empareja en tuplas. La función dict luego convierte cada tupla en un diccionario. El resultado es una lista de diccionarios donde cada elemento en la lista representa una fila en data y cada clave en el diccionario corresponde a una columna en data.

Por último, se abre el archivo especificado en json_file en modo de escritura ('w') y con la codificación especificada ('utf-8'). Luego, se escribe la lista de diccionarios en el archivo utilizando la función json.dumps, que convierte los datos en una cadena JSON. El parámetro indent=4 le dice a la función que agregue cuatro espacios de sangría a cada nivel de anidamiento para mejorar la legibilidad del archivo JSON resultante.

La última parte del código comprueba si este archivo está siendo ejecutado como un script independiente (__name__ == '__main__') y llama a la función csv_to_json, pasando los nombres de archivo especificados como argumentos. En este caso, el código convierte un archivo CSV en un archivo JSON y los guarda en la carpeta 'data'.
"""
