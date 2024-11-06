#Se importan las librerías necesarias
import cv2
import os
#NOTA: El programa grabara video hasta que se presione cualquier tecla - Justin :)

nombre_carpeta = "Videos_del_ejercicio_3"
nombre_video = "video_grabado_con_opencv.mp4"
ruta_video = os.path.join(nombre_carpeta, nombre_video)

def grabar_video(nombre_carpeta, ruta_video):
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)
        
    camara = cv2.VideoCapture(1) # Yo uso 1 porque en ese se encuentra mi camara, por lo general es 0, así que cambialo por si el codigo tiene algun error
    ancho = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
    alto = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(ruta_video, codec, 20.0, (ancho, alto))
    
    while True:
        ret, frame = camara.read()
        video.write(frame)
        
        cv2.imshow('Grabando Video', frame)
        #Al presionar cualquier tecla se detiene la grabación
        if cv2.waitKey(1) != -1:
            break

    camara.release()
    video.release()
    cv2.destroyAllWindows()

grabar_video(nombre_carpeta, ruta_video)
