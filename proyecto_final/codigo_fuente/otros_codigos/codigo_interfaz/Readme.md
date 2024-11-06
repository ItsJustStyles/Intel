Aclaraciones:
El archivo que se debe ejecutar para lograr que funcione el código es el llamado interfaz.py

En este archivo de interfaz debido a que las pantallas tienen diferentes dimensiones, se puede cambiar el tamaño de la interfaz aumentando y disminuyendo el numero de la variable valor_principal para ampliar y disminuir el tamaño de lo que se muestra en pantalla. 
La variable para su fácil localización se encuentra remarcada por barras inclinadas y barras inclinadas invertidas a modo se separador.
Este método de adaptación tiene sus limitantes y puede que en cierto tipo de pantallas no llegue a encajar todo muy bien.
Para cerrar la ventana de la interfaz se puede hacer desde el boton en la esquina superior izquierda o tambien con las teclas o "esc" o "q".

Posibles mejoras: 
Si se pudiera conocer el tamaño del monitor en donde será ejecuta el código las proporciones y posiciones de los elementos podrían ser corregidas fácilmente.
También si en vez de Python y Tkinter se utilizara un método o lenguaje de esquematización dedicado, podría llegar a ser compatible con múltiples dispositivos.
Se intento implementar una función que cambiara el valor_principal al recibir el evento de presionar una tecla como - o + pero debido a la forma de creación de ventanas que tiene Tkinter y a que no se contempló desde un principio no se logró terminar, pero si se rehiciera la interfaz esta función podría ser implementada.
