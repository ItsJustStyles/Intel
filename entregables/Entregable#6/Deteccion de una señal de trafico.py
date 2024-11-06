#Se importan las librerías necesarias
import cv2
import numpy as np
import os

#NOTAS: El programa tomara el video y tomara cada uno de sus frames y los convertira en imagenes, al presionar cualquier tecla el programa mostrara otro frame con el objeto detectado, el programa se cerrara cuando ya no hayan más imagenes

#Se crea la funcion para extraer los frames del video, los cuales se van a convertir en imagenes, estas iran a una carpeta la cual si no existe se creara :)
def extraer_frames_del_video(video_direccion, folder_frames):

    if not os.path.exists(folder_frames):
        os.makedirs(folder_frames)
    cap = cv2.VideoCapture(video_direccion)

    contador_de_frames = 0
    while True:

        ret, frame = cap.read()
        if not ret:
            break
        #Se crea la imagen y se añade a la carpeta con el nombre dado
        nombre_de_la_imagen = os.path.join(folder_frames, f'frame_{contador_de_frames:04d}.jpg')
        cv2.imwrite(nombre_de_la_imagen, frame)

        contador_de_frames += 1

    cap.release()

def procesar_y_mostrar_frames(folder_frames):
    #Se toman una por una las imagenes de la carpeta
    frames = sorted([f for f in os.listdir(folder_frames) if f.endswith('.jpg')])
    for frame_filename in frames:
        frame_path = os.path.join(folder_frames, frame_filename)
        imagen = cv2.imread(frame_path)
        #Se procede a realizar las transformaciones necesarias para la detección

        #Se pasa la imagen en escala de grises
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        #A esta se le aplica una umbralización
        _, mascara_umbral = cv2.threshold(imagen_gris, 130, 255, cv2.THRESH_BINARY)

        #A esta umbralización se le da vuelta es decir lo que estaba negro pasa a ser blanco y viceversa
        #Esto debido a que la umbralización dejaba como zona de no interes a la señal de transito, pero esto es un beneficio, ya que al darle vuelta
        #Todos los demás colores en tono azul desaparecieron casi por completo
        mascara_invertida = cv2.bitwise_not(mascara_umbral)

        #Se define el color azul, para esto se uso una herramienta para lograr tener el color de la señal, lo cual hace más exacta la detección
        azul_bajo = np.array([95, 200, 150], np.uint8)  
        azul_alto = np.array([125, 255, 255], np.uint8)  

        imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

        mascara_azul = cv2.inRange(imagen_hsv, azul_bajo, azul_alto)

        mascara_resultado = cv2.bitwise_and(mascara_azul, mascara_invertida)

        contornos, _ = cv2.findContours(mascara_resultado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #Estas áreas se deben a que algunos colores azules aun estaba presentes entonces se opto por tomar un area minima para que programa detectara dicho onjeto
        #Logrando con esto que lo unico que se detectara sea la señal de transito
        area_minima = 50
        area_maxima = 3500

        #Se dibujan el rectangulo en el objeto que cumple con el area, el color del rectangulo es negro
        imagen_dibujada = imagen.copy()
        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area_minima <= area <= area_maxima:
                x, y, w, h = cv2.boundingRect(contorno)
                cv2.rectangle(imagen_dibujada, (x, y), (x + w, y + h), (0, 0, 0), 4) 

        cv2.imshow('Detectando una señal de transito de un video', imagen_dibujada)

        key = cv2.waitKey(0)
        if key == 27:  
            break


    cv2.destroyAllWindows()

#Ruta donde se encuentra el video, además del nombre de la carpeta a crear
video_direccion = 'video.mp4'
folder_frames = 'frames_del_video'

extraer_frames_del_video(video_direccion, folder_frames)
procesar_y_mostrar_frames(folder_frames)
