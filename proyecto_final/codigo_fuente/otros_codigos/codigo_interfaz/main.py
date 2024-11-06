import cv2
import numpy as np

def recortar_frame(frame, porcentaje=0.74):
    # Recorta el frame central
    alto, ancho = frame.shape[:2]
    nuevo_ancho = int(ancho * porcentaje)
    nuevo_alto = int(alto * porcentaje)
    inicio_x = (ancho - nuevo_ancho) // 2
    inicio_y = (alto - nuevo_alto) // 2

    # Recorte del frame
    frame_recortado = frame[inicio_y:inicio_y+nuevo_alto, inicio_x:inicio_x+nuevo_ancho]

    # Escalar el recorte al tamaño original del frame
    frame_recortado = cv2.resize(frame_recortado, (ancho, alto), interpolation=cv2.INTER_LINEAR)

    frame_recortado = frame_recortado[inicio_y:inicio_y+nuevo_alto, inicio_x:inicio_x+nuevo_ancho]

    return frame_recortado

def encontrar_y_dibujar_contornos(frame, area_minima_exterior = 500, area_minima_interior = 20):
    # Convierte todo lo que sea diferente de blanco a negro
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, umbralizado = cv2.threshold(gris, 200, 255, cv2.THRESH_BINARY)

    # Encuentra los contornos del objeto y con ellos crea una mascara del objeto
    umbralizado_invertido = cv2.bitwise_not(umbralizado)
    contornos, jerarquia = cv2.findContours(umbralizado_invertido, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    mascara = np.zeros_like(umbralizado)

    contorno_exterior_max_area = None
    area_maxima = 0
    contorno_exterior_max_index = -1

    # Encuentra el contorno exterior con la mayor área
    for i, contorno in enumerate(contornos): # Revisa contorno por contorno
        area = cv2.contourArea(contorno) # Cauntifica el area revisada
        if area > area_minima_exterior and jerarquia[0][i][3] == -1:  # Revisa si es un contorno exterior
            if area > area_maxima: # Compara el area revisada con la anterior mas grande
                area_maxima = area 
                contorno_exterior_max_area = contorno
                contorno_exterior_max_index = i

    # Dibuja el contorno exterior con la mayor área
    if contorno_exterior_max_area is not None:
        cv2.drawContours(mascara, [contorno_exterior_max_area], -1, 255, thickness=cv2.FILLED)  # Hace la mascara de los contornos en blanco
        for j, contorno in enumerate(contornos): # Revisa cada contorno
            if jerarquia[0][j][3] == contorno_exterior_max_index:  # Descubre el contorno interior (hijo del contorno exterior más grande)
                area_interior = cv2.contourArea(contorno)
                if area_interior > area_minima_interior: # Revisa si el contorno tiene la suficiente area
                    contorno_interior_min_area = contorno
                    cv2.drawContours(mascara, [contorno_interior_min_area], -1, 0, thickness=cv2.FILLED)  # Hace la mascara de los contornos interiores en blanco

    return mascara

def detectar_bordes(frame):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convertir la imagen a escala de grises
    bordes = cv2.Canny(gris, 100, 200) # Aplicar el filtro de Canny

    # Aplicar dilatación y erosión
    kernel = np.ones((5, 5), np.uint8)
    dilatado = cv2.dilate(bordes, kernel, iterations=2)
    bordes_preprocesados = cv2.erode(dilatado, kernel, iterations=2)

    # Aplicar dilatación y erosión
    kernel = np.ones((5, 5), np.uint8)
    dilatado = cv2.dilate(bordes_preprocesados, kernel, iterations=3)
    bordes_preprocesados = cv2.erode(dilatado, kernel, iterations=3)

    return bordes_preprocesados

def detectar_formas(bordes, frame):
    # Encontrar contornos en la imagen de bordes
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Crear una copia del fotograma original para dibujar los contornos
    imagen_formas = frame.copy()
    cont = 0

    for contorno in contornos:
        # Aproximar el contorno a una forma poligonal
        epsilon = 0.035 * cv2.arcLength(contorno, True)
        aproximado = cv2.approxPolyDP(contorno, epsilon, True)

        # Identificar la forma a partir del numero de vertices
        num_vertices = len(aproximado) 
        if 4 >= num_vertices and num_vertices >= 1:
            nombre_forma = "Tornillo"
        elif num_vertices >= 5 and 6 >= num_vertices:
            nombre_forma = "Tuerca"
        else:
            nombre_forma = "Arandela"

        # Escribir el nombre de la forma en la imagen
        if cont != 1:
            cv2.putText(imagen_formas, nombre_forma, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cont += 1
    try:
        return nombre_forma
    except:
        return "No se detecta ningun objeto"

def obtener_colores_predominantes(hsv, num_colores=7):
    # Obtiene colores únicos y cuanto aparecen
    colores, count = np.unique(hsv.reshape(-1, hsv.shape[-1]), axis=0, return_counts=True)
    
    # Ordena colores por frecuencia en orden del mayor al menor
    indices = np.argsort(-count)[:num_colores]
    colores_predominantes = colores[indices]
    colores_predominantes = [color for color in colores_predominantes if str(color) != "[0 0 0]"]

    # Verifica que la lista de colores no esta vacia
    try:
        # Convierte los colores HSV a BGR para su visualización
        colores_bgr = cv2.cvtColor(np.uint8([colores_predominantes]), cv2.COLOR_HSV2BGR)[0]
        return colores_bgr, colores_predominantes
    except:
        # Convierte los colores HSV a BGR para su visualización
        colores_predominantes= []
        colores_predominantes.append([0, 0, 0])
        colores_bgr = cv2.cvtColor(np.uint8([colores_predominantes]), cv2.COLOR_HSV2BGR)[0]
        return colores_bgr, colores_predominantes

def color_cafe(hsv_color):
    #Verifica que la lista no este vacia
    if "[0, 0, 0]" == str(hsv_color):
        return " "
    
    # Definir el rango inicial de colores calidos en HSV
    rango_inferior_1 = np.array([0, 0, 0])  # Hue: Rojo
    rango_superior_1 = np.array([30, 225, 225])  # Hue: amarillo

    # Definir el rango final de colores calidos en HSV
    rango_inferior_2 = np.array([148, 0, 0])  # Hue: Rosado
    rango_superior_2 = np.array([179, 225, 225])  # Hue: Rojo 
    
    # Convertir hsv_color a un array de una sola fila
    hsv_color = np.array(hsv_color, dtype=np.uint8)

    # Verifica si hay algun color cafe con bajo Hue
    if cv2.inRange(hsv_color[None, None, :], rango_inferior_1, rango_superior_1).any():
        return True
    else:
        # Confirma que no hay clores cafe con alto Hue
        if cv2.inRange(hsv_color[None, None, :], rango_inferior_2, rango_superior_2).any():
            return True
        else:
            return False
        
def mostrar_colores_predominantes(colores,h=100,w=140):
    # Muestra en una ventana aparte los colores que recibe 
    indices = range(0, len(colores)-1, 1)
    first = True
    for i in indices:
        if first:
            color = colores[i] 
            img1 = np.zeros((h, w, 3), np.uint8)
            img1[:] = color
            
            color = colores[i+1] 
            img = np.zeros((h, w, 3), np.uint8)
            img[:] = color
            
            hconcat = cv2.hconcat([img1,img])
            first = False
        else:
            color = colores[i+1] 
            img = np.zeros((h, w, 3), np.uint8)
            img[:] = color

            hconcat = cv2.hconcat([hconcat,img])
    if not first:
        return hconcat
