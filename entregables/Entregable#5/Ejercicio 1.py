#Se importan las librerias necesarias
import cv2
import os

nombre_carpeta = "Fotos del ejercicio 1"
nombre_foto = "Foto_con_opencv.png"

def captura_de_foto(nombre_carpeta,nombre_foto):
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    camara = cv2.VideoCapture(1) # Yo uso 1 porque en ese se encuentra mi camara, por lo general es 0, así que cambialo por si el codigo tiene algun error

    ret, frame = camara.read()
    cv2.imshow("Camara", frame)
    ruta_foto = os.path.join(nombre_carpeta, nombre_foto)
    cv2.imwrite(ruta_foto, frame)
    camara.release()
    cv2.destroyAllWindows()
captura_de_foto(nombre_carpeta, nombre_foto) 
#Holap