#Se importan las librerías necesarias
import cv2
import os
import time
#NOTA: Se modifico el codigo 2, para obtener una espera de 5 segundo antes de tomar la foto, además la transformación utilizada fueron los bordes de canny
nombre_carpeta = "Fotos_del_ejercicio_4"
nombre_foto_canny = "fotos_con_canny.png"

def captura_de_foto(nombre_carpeta, nombre_foto_canny):
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
    
    camara = cv2.VideoCapture(1) # Yo uso 1 porque en ese se encuentra mi camara, por lo general es 0, así que cambialo por si el codigo tiene algun error

    start_time = time.time()
    while time.time() - start_time < 5:
        ret, frame = camara.read()
        cv2.imshow('Camara', frame)
         #Añade una pausa logrando que se pueda actualizar el frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    ret, frame = camara.read()

    #Se aplica la transformación de canny
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    bordes = cv2.Canny(gris, 100, 200)  
    ruta_foto_canny = os.path.join(nombre_carpeta, nombre_foto_canny)
    cv2.imwrite(ruta_foto_canny, bordes)

    camara.release()
    cv2.destroyAllWindows()

captura_de_foto(nombre_carpeta, nombre_foto_canny)