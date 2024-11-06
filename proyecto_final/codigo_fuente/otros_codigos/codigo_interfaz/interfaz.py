from tkinter import * 
import tkinter
from PIL import Image, ImageTk
from tkinter.font import Font
from main import *
import os

# Convertir cm a píxeles (asumiendo 96 DPI, que es común en muchas pantallas)
cm_a_pixeles = lambda cm: int(cm * 96 / 2.54)

#///////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

valor_principal = 12.7 # Determina el indice de tamaño en la ventana.

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\///////////////////////////////////

# Crear la ventana principal
root = tkinter.Tk()

root.overrideredirect(True) # Ocultar los iconos de la ventana

mult_window= 5
remult_window = 2*mult_window

# Obtener el tamaño de la pantalla
ancho_pantalla = root.winfo_screenwidth()
ancho_pantalla= int(ancho_pantalla - ancho_pantalla/mult_window)
alto_pantalla = root.winfo_screenheight()
alto_pantalla = int(alto_pantalla - alto_pantalla/mult_window)

# Configurar la ventana para que sea del tamaño de la pantalla
root.geometry(f"{ancho_pantalla}x{alto_pantalla}+{int(ancho_pantalla/remult_window)}+{int(alto_pantalla/remult_window)}")

tamaño_cuadrado = cm_a_pixeles(valor_principal)

def cerrar(event=0):
    root.destroy()

# Configurar el fondo de la ventana para que sea blanco
root.configure(bg="#f7f7f6")

# Definir el tamaño del borde en píxeles
borde_exterior = tamaño_cuadrado/10
borde_superior = cm_a_pixeles(1)
margen_inferior = cm_a_pixeles(0.5)
margen_izquierdo = cm_a_pixeles(0.5)
margen_superior = cm_a_pixeles(0.8)


# Definir el tamaño del rectángulo pequeño (8 cm de largo y 2 cm de ancho)
lado_largo_rectangulo_pequeño = tamaño_cuadrado 
lado_corto_rectangulo_pequeno = tamaño_cuadrado/4.4

# Calcular las coordenadas para centrar el cuadrado rojo
x1_cuadrado = borde_exterior + margen_izquierdo
y1_cuadrado = borde_exterior + borde_superior + margen_inferior + margen_superior  # Bajado 0.5 cm
x2_cuadrado = x1_cuadrado + tamaño_cuadrado
y2_cuadrado = y1_cuadrado + tamaño_cuadrado - int(tamaño_cuadrado/8)

# Calcular las coordenadas para posicionar el primer rectángulo pequeño
x1_interior = x2_cuadrado + tamaño_cuadrado/20
y1_interior = borde_exterior + borde_superior + margen_superior + tamaño_cuadrado/20 # Bajado 0.5 cm
x2_interior = x1_interior + lado_largo_rectangulo_pequeño
y2_interior = y1_interior + lado_corto_rectangulo_pequeno

# Definir el tamaño del rectángulo grande adicional 
lado_largo_rectangulo_grande = lado_largo_rectangulo_pequeño + tamaño_cuadrado + int(tamaño_cuadrado/16)

# Calcular las coordenadas para el rectángulo grande adicional (19.5 cm de largo y 2 cm de ancho)f
x1_grande = x1_cuadrado
y1_grande = y2_cuadrado + int(tamaño_cuadrado/16) # Posicionado a 2.5 cm debajo del cuadrado rojo
x2_grande = x1_grande + lado_largo_rectangulo_grande
y2_grande = y1_grande

# Dibujar el rectángulo azul de 1.5 cm de ancho en la parte superior del rectángulo principal
x1_azul = borde_exterior
y1_azul = borde_exterior
x2_azul = ancho_pantalla - borde_exterior
y2_azul = y1_azul + cm_a_pixeles(1.5)

x1_cuadrado_pequeño = x1_cuadrado + lado_largo_rectangulo_grande + tamaño_cuadrado/5.4
y1_cuadrado_pequeño = y2_cuadrado + tamaño_cuadrado/6.2
x2_cuadrado_pequeño = x1_cuadrado_pequeño + tamaño_cuadrado/5.7
y2_cuadrado_pequeño = y1_cuadrado_pequeño + tamaño_cuadrado/5.7

font_size = valor_principal + 12
fuente = Font(family="Bradley Hand ITC", size=int(font_size))  # Tamaño de fuente ajustado a 25
fuente_2 = Font(family= 'Britannic Bold', size=int(font_size-2))
icon_font = Font(family="Britannic Bold", size=int(font_size*1.8)) 
exit_icon = Font(family="arial",size=int(font_size-3), weight="bold")
# Crear un canvas para dibujar los rectángulos y la línea
canvas = tkinter.Canvas(root, width=ancho_pantalla, height=alto_pantalla, bg="#f7f7f6", highlightthickness=0)
canvas.pack()

# Dibujar el relleno azul del rectángulo grande primero
canvas.create_rectangle(
    borde_exterior,
    borde_exterior,
    ancho_pantalla - borde_exterior,
    borde_exterior + borde_superior,
    fill="#7DA3E0",  # Azul especificado
    outline="#7DA3E0"  # Azul especificado
)

# Dibujar la línea negra a 1 cm desde la parte superior del rectángulo principal
canvas.create_line(
    borde_exterior, 
    borde_exterior + borde_superior, 
    ancho_pantalla - borde_exterior, 
    borde_exterior + borde_superior, 
    fill="black", 
    width=2
)

# Dibujar el rectángulo principal dejando un borde de 2 cm
canvas.create_rectangle(
    borde_exterior, 
    borde_exterior,
    ancho_pantalla - borde_exterior,
    alto_pantalla - borde_exterior,
    outline="black",
    fill= "#f7f7f6",
    width=2
)

# Dibujar el cuadrado de 11 cm de lado 0.5 cm debajo de la línea negra y 0.5 cm del borde izquierdo
canvas.create_rectangle(
    x1_cuadrado,
    y1_cuadrado,
    x2_cuadrado,
    y2_cuadrado,
    fill="red",  # Color de relleno del cuadrado
    outline="black",
    width=0
)

cam_video = tkinter.Label(root, bg="black")
cam_video.place(x=x1_cuadrado, y=y1_cuadrado)

# Abre la cámara (0 es usualmente la cámara predeterminada)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()


def iniciar():
    global frame
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo recibir el frame.")
        
    frame_recortado = recortar_frame(frame)
    frame_recortado = cv2.cvtColor(frame_recortado, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_recortado)
    img = img.resize((tamaño_cuadrado,tamaño_cuadrado - int(tamaño_cuadrado/8)))
    image = ImageTk.PhotoImage(image=img)
    cam_video.configure(image= image)
    cam_video.image = image
    cam_video.after(10,iniciar)

canvas.create_rectangle(
    x1_azul,
    y1_azul,
    x2_azul,
    y2_azul,
    fill="#7da3e0",  # Azul
    outline="black",
    width=2
)

# Función para dibujar el rectángulo pequeño en una posición específica
def dibujar_rectangulo_pequeno(x1, y1):
    y1 = y1 + cm_a_pixeles(0.4)
    # Dibujar la línea negra en la parte superior del rectángulo pequeño
    canvas.create_line(
        x1,
        y1,
        x1 + lado_largo_rectangulo_pequeño,
        y1,
        fill="black",
        width=2
    )
    # Rellenar el área encima de la línea negra con el color azul #A4BCE9
    canvas.create_rectangle(
        x1,
        y1,
        x1 + lado_largo_rectangulo_pequeño,
        y1 + tamaño_cuadrado/8.8 ,
        fill="#A4BCE9",  # Azul especificado
        outline="black"
    )
    # Dibujar el borde negro alrededor del rectángulo pequeño
    canvas.create_rectangle(
        x1,
        y1,
        x1 + lado_largo_rectangulo_pequeño,
        y1 + lado_corto_rectangulo_pequeno,
        outline="black",
        width=2
    )
    # Guardar las coordenadas para el texto
    return (x1+5, y1 + tamaño_cuadrado/16.16)

# Función para dibujar el rectángulo grande adicional
def dibujar_rectangulo_grande(x1, y1):
    # Dibujar la línea negra en la parte superior del rectángulo grande adicional
    canvas.create_line(
        x1,
        y1,
        x1 + lado_largo_rectangulo_grande,
        y1,
        fill="black",
        width=4
    )
    # Rellenar el área encima de la línea negra con el color azul #A4BCE9
    canvas.create_rectangle(
        x1,
        y1,
        x1 + lado_largo_rectangulo_grande,
        y1 + tamaño_cuadrado/10,
        fill="#A4BCE9",  # Azul especificado
        outline="black"
    )
    # Dibujar el borde negro alrededor del rectángulo grande adicional
    canvas.create_rectangle(
        x1,
        y1,
        x1 + lado_largo_rectangulo_grande, 
        y1 + int(lado_corto_rectangulo_pequeno + tamaño_cuadrado/10),
        outline="black",
        width=2
    )
    # Guardar las coordenadas para el texto
    return (x1, y1)

# Dibujar el primer rectángulo pequeño
texto1_coords = dibujar_rectangulo_pequeno(x1_interior, y1_interior)

# Dibujar el segundo rectángulo pequeño 2 cm debajo del primero
texto2_coords = dibujar_rectangulo_pequeno(x1_interior, y1_interior + lado_corto_rectangulo_pequeno + tamaño_cuadrado/16)

# Dibujar el tercer rectángulo pequeño 2 cm debajo del segundo
texto3_coords = dibujar_rectangulo_pequeno(x1_interior, y1_interior + 2 * (lado_corto_rectangulo_pequeno + tamaño_cuadrado/16))

# Dibujar el rectángulo grande adicional
texto4_coords = dibujar_rectangulo_grande(x1_grande, y1_grande)

# Dibujar el primer cuadrado de 1.5 cm de lado
def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

check_box = round_rectangle(
    x1_cuadrado_pequeño,
    y1_cuadrado_pequeño,
    x2_cuadrado_pequeño,
    y2_cuadrado_pequeño,
    25,
    fill="#eaeef7",
    outline="#eaeef7"
)
uncheck_box = round_rectangle(
    x1_cuadrado_pequeño + tamaño_cuadrado/4.7,
    y1_cuadrado_pequeño,
    x2_cuadrado_pequeño + tamaño_cuadrado/4.7,
    y2_cuadrado_pequeño,
    25,
    fill="#eaeef7",
    outline="#eaeef7"
)
# Crear un Frame para los botones en la esquina superior izquierda
frame_botones = Frame(root, bg="#7DA3E0")
frame_botones.place(x=lado_largo_rectangulo_grande + tamaño_cuadrado - tamaño_cuadrado/7, y=borde_exterior+1)  # Posicionarlo en la esquina superior izquierda

boton = tkinter.Button(
    frame_botones,
    border=0,
    background="#7DA3E0",
    foreground="WHITE",
    activebackground="#6d8cbd",
    activeforeground="RED",
    text= "⮾",
    font=exit_icon,
    command=cerrar
)

boton.pack(side=TOP, fill=X)
# Agregar textos al final

# Texto para el primer rectángulo para el nombre del colegio
canvas.create_text(
    texto1_coords[0],  # Ajuste para que el texto quede alineado a la izquierda
    texto1_coords[1],  # Ajuste vertical para centrar el texto
    text="Colegio",
    font=fuente,
    fill="#000000",  # Negro puro
    anchor="w"  # Alinea el texto a la izquierda
)
canvas.create_text(
    texto1_coords[0],  # Ajuste para que el texto quede alineado a la izquierda
    texto1_coords[1] + tamaño_cuadrado/9,  # Ajuste vertical para centrar el texto
    text="Cientifico del Atlantico",
    font=fuente_2,
    fill="#000000",  # Negro puro
    anchor="w"  # Alinea el texto a la izquierda
)
#//////////////////////////////////////////////////////////////////////////////////#

# Texto para el segundo rectángulo para el nombre del objeto
canvas.create_text(
    texto2_coords[0],  # Ajuste para que el texto quede alineado a la izquierda
    texto2_coords[1],  # Ajuste vertical para centrar el texto
    text="Nombre del objeto",
    font=fuente,
    fill="#000000",  # Negro puro
    anchor="w"  # Alinea el texto a la izquierda
)
your_text_id = canvas.create_text(
    texto2_coords[0],  # Ajuste para que el texto quede alineado a la izquierda
    texto2_coords[1] + tamaño_cuadrado/9,  # Ajuste vertical para centrar el texto
    text= "None",
    font=fuente_2,
    fill="#217bbb", 
    anchor="w"  # Alinea el texto a la izquierda
)

def init_nombre_obj():
    frame_recortado = recortar_frame(frame)
    bordes_preprocesados = detectar_bordes(frame_recortado)
    nombre_obj = detectar_formas(bordes_preprocesados, frame_recortado)
    canvas.itemconfig(your_text_id, text = nombre_obj)
    root.after(10, init_nombre_obj)

#//////////////////////////////////////////////////////////////////////////////////#

# Texto para el tercer rectángulo pequeño
canvas.create_text(
    texto3_coords[0],  # Ajuste para que el texto quede alineado a la izquierda
    texto3_coords[1],  # Ajuste vertical para centrar el texto
    text="Estado del objeto",
    font=fuente,
    fill="#000000",  # Negro puro
    anchor="w"  # Alinea el texto a la izquierda
)
canvas_id = canvas.create_text(
    texto3_coords[0],  # Ajuste para que el texto quede alineado a la izquierda
    texto3_coords[1] + tamaño_cuadrado/9,  # Ajuste vertical para centrar el texto
    text= "None",
    font=fuente_2,
    fill="#000000", 
    anchor="w"  # Alinea el texto a la izquierda
)

texto_revision = canvas.create_text(
    x1_cuadrado + lado_largo_rectangulo_grande + tamaño_cuadrado/4,
    y2_cuadrado + tamaño_cuadrado/10,  
    text="Revisión",
    font=fuente,
    fill="#000000",  
    anchor="w"
)
checker = x1_cuadrado_pequeño + tamaño_cuadrado/40
check = canvas.create_text(
    checker, 
    y2_cuadrado + tamaño_cuadrado/4,  
    text="✔",
    font=icon_font,
    fill="WHITE",  
    anchor="w"
)

uncheck = canvas.create_text(
    checker + tamaño_cuadrado/4.7, 
    y2_cuadrado + tamaño_cuadrado/4,  
    text="✗",
    font=icon_font,
    fill="WHITE",  
    anchor="w"  
)

def init_estados():
    # Recorta, convierte la imagen a blanco y negro cada frame, para luego encontrar su contorno
    frame_recortado = recortar_frame(frame)
    mascara = encontrar_y_dibujar_contornos(frame_recortado)
    # Aplica la máscara al frame recortado y obtiene los colores predominante
    frame_mascarado = cv2.bitwise_and(frame_recortado, frame_recortado, mask=mascara)
    hsv_recortado = cv2.cvtColor(frame_mascarado, cv2.COLOR_BGR2HSV)
    _, colores_predominantes = obtener_colores_predominantes(hsv_recortado)

    # Verifica si alguno de los colores predominantes está fuera del rango de grises
    for color in colores_predominantes:
        if color_cafe(color) == True:
            color_mal_estado = True
            break
        elif color_cafe(color) == False:
            color_mal_estado = False
        else:
            if color_mal_estado != "No obj":
                print("Buscando un objeto...")
            color_mal_estado = "No obj"   
    if color_mal_estado == True:
        estado ="Objeto en mal estado"
        color_mal_estado = True
        color = "#bb1921"
        canvas.itemconfig(uncheck_box, fill="RED")
        canvas.itemconfig(check,fill="#eaeef7")
        canvas.itemconfig(canvas_id, text=estado, fill=color)
    elif color_mal_estado == False:
        estado ="Objeto en buen estado"
        color = "#17a335"
        canvas.itemconfig(check_box, fill="GREEN")
        canvas.itemconfig(uncheck, fill="#eaeef7")
        canvas.itemconfig(canvas_id, text=estado, fill=color)
    else:
        estado =""
        color = "#ffffff"
        canvas.itemconfig(check,fill="#eaeef7")
        canvas.itemconfig(uncheck, fill="#eaeef7")
    root.after(10, init_estados)

#//////////////////////////////////////////////////////////////////////////////////#

# Texto para el rectángulo de colores predominantes
canvas.create_text(
    texto4_coords[0] + 4,  # Ajuste para que el texto quede alineado a la izquierda
    texto4_coords[1] + tamaño_cuadrado/20,  # Ajuste vertical para centrar el texto
    text="Colores Predominantes",  # Modifica este texto según sea necesario
    font=fuente,
    fill="#000000",  # Negro puro
    anchor="w"  # Alinea el texto a la izquierda
)

colores_pred = tkinter.Label(root, bg="black", borderwidth=2)
colores_pred.place(x=texto4_coords[0], y=texto4_coords[1] + tamaño_cuadrado/10)

def int_color_pred():
    global frame
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo recibir el frame.")

    # Recorta, convierte la imagen a blanco y negro cada frame, para luego encontrar su contorno
    frame_recortado = recortar_frame(frame)
    mascara = encontrar_y_dibujar_contornos(frame_recortado)

    # Aplica la máscara al frame recortado y obtiene los colores predominante
    frame_mascarado = cv2.bitwise_and(frame_recortado, frame_recortado, mask=mascara)
    hsv_recortado = cv2.cvtColor(frame_mascarado, cv2.COLOR_BGR2HSV)
    colores_brg, _ = obtener_colores_predominantes(hsv_recortado, 7)
    frame_recortado = mostrar_colores_predominantes(colores_brg,int(lado_corto_rectangulo_pequeno),int(lado_largo_rectangulo_grande/6))
    frame_recortado = cv2.cvtColor(frame_recortado, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_recortado)
    image = ImageTk.PhotoImage(image=img)
    colores_pred.configure(image= image)
    colores_pred.image = image
    colores_pred.after(1000,int_color_pred)

#//////////////////////////////////////////////////////////////////////////////////#

# Mostrar el codigo del colegio
folder = os.path.dirname(__file__)
folder  = os.path.join(folder,"Logo.png")
photo_image = Image.open(f"{folder}")
photo_image = photo_image.resize((int(tamaño_cuadrado-tamaño_cuadrado/5),int(tamaño_cuadrado- tamaño_cuadrado/5)))
photo_image = ImageTk.PhotoImage(photo_image)

image_label = tkinter.Label(root, wraplength = 230, bg="#f7f7f6",image=photo_image, borderwidth=0, compound="center",highlightthickness = 0,padx=0,pady=0)
image_label.place(x=x1_cuadrado+lado_largo_rectangulo_grande + tamaño_cuadrado/26, y=y1_cuadrado+tamaño_cuadrado/20)

iniciar()
init_nombre_obj()
init_estados()
int_color_pred()

root.bind("<Escape>", cerrar)
root.bind("q", cerrar)

root.mainloop()
