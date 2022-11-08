import json
from json import JSONEncoder

class Joven(object):
    def __init__(self, Nombres, Apellidos, Comunidad, Celular):
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Comunidad = Comunidad
        self.Celular = Celular


#leer un objeto JSON o deserializar un objeto desde un archivo
with open ("Documents/jovenes.json", "r") as file: #modo read
    list = json.load(file) #OJO sin la s, son funciones similares pero no iguales

objeto = Joven(**list[0])
print(objeto.Nombres)

