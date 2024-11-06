Para empezar el codigo importa las librerias: opencv, numpy y time. Las cuales son necesarias para el uso del codigo, por lo que es necesario tenerlas descargadas en el equipo.

NOTA: Se recomienda utilzar un venv para evitar errores que puedan surgir de mezclar librerias en el equipo.

El codigo esta dividido en funciones:

recortar_frame: Realiza un recorte y un reescalado al frame original para trabajar con menos imagen y obtener una mayor velocidad.

encontrar_y_dibujar_contornos:  A la imagen recortada se le realiza el metodo de umbralización y se deteminan los contornos de la misma, tomando como contorno principal el de mayor area y como contorno interno el que este dentro del principal y supere el area minima establecida

detectar_bordes: A la imagen reocrtada se la transforma a escala de grises y se le aplica el detector de bordes de canny y se cuentan los vertices que posee la figura y con esto se da el nombre al objeto: tornillos, tuercas y arandelas.

obtener_colores_predominantes: Se obtienen los colores que presenta el objeto analizado.

es_color_cafe: Verifica si se encuentra el color café en los colores obtenidos.

mostrar_colores_predominantes: Muestra todos los colores que se obtienen de la función anterior.

main: Es el codigo central y se ejecuta cada cierto tiempo, esta parte se encaraga de organizar todas las demás funciones y verificar el estado del objeto: "Mal estado" y "Buen estado", abriendo nuevas ventanas de información.

Las ventanas que se abren son: La gama de colores del objeto, la cámara que muestra el objeto, y el estado del objeto.

USO DEL CODIGO:

Para usar el codigo se necesitan primeramente la libreria necesaria, por lo que es necesario descargar Opencv de la siguiente manera:

pip install opencv-python

Ya luego de esto se puede simplemente correr el codigo y poner un objeto abajo de la camara y el codigo procedera a realizar la clasificación de los siguientes objetos: tornillos, tuercas y arandelas en buen o mal estado.

NOTA: Por favor colocar la cámara que se vaya a utilizar a una distancia en la que se logre enfocar bien al objeto.

Por otro lado, se incluira la carpeta "Otros codigos" en la que estaran otras versiones de este, uno con interfaz y otro utilizando IA.
