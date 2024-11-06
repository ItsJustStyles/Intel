#Se importan las librerias necesarias
import cv2
import os
import time

nombre_carpeta = "Fotos_del_ejercicio_2"
nombre_foto = "fotos_con_temporizador_en_opencv.png"

def captura_de_foto(nombre_carpeta, nombre_foto):
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    
    camara = cv2.VideoCapture(1)  # Yo uso 1 porque en ese se encuentra mi camara, por lo general es 0, así que cambialo por si el codigo tiene algun error

    start_time = time.time()
    while time.time() - start_time < 5:
        ret, frame = camara.read()
        cv2.imshow('Camara', frame)
        #Añade una pausa logrando que se pueda actualizar el frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    ret, frame = camara.read()
    ruta_foto = os.path.join(nombre_carpeta, nombre_foto)
    cv2.imwrite(ruta_foto, frame)

    camara.release()
    cv2.destroyAllWindows()

captura_de_foto(nombre_carpeta, nombre_foto)
