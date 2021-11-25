import cv2
import numpy as np
import os

# importar fotos con y sin tapaboca+
direccion = "C:/Users/pepe/Music/IA/Fotos" # REEMPLAZA LA DIRECCION DONDE SE GUARDA EL MODELO , DEBE ESTAR EN LA MISMA UBICACION DEL PROYECTO
lista = os.listdir(direccion)
etiquetas  = []
rostros = []
cont = 0

for nameDir in lista:
    nombre = direccion + '/' + nameDir # leer fotos de los rostros
    for fileName in os.listdir(nombre):
        etiquetas.append(cont)
        rostros.append(cv2.imread(nombre+'/'+fileName,0))
    cont = cont + 1
# se crea modelo
reconocimiento = cv2.face.LBPHFaceRecognizer_create()
# entrenar modelo reconocmiento
reconocimiento.train(rostros, np.array(etiquetas))
# guardar reconocimiento
reconocimiento.write("ModeloEntrenado.xml")
print("Modelo creado")
