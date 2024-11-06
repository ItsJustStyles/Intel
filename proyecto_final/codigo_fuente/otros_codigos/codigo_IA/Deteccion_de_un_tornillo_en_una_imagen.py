import cv2
from ultralytics import YOLO

modelo = YOLO("best.pt")  


ruta_imagen = "tornillo.jpg" 


umbral_confianza = 0.3

imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print("Error al cargar la imagen.")
    exit()


resultados = modelo(imagen)


for resultado in resultados:
    boxes = resultado.boxes 
    probs = resultado.boxes.conf  
    names = resultado.names  

    if boxes is not None and probs is not None:

        for i in range(len(boxes.xyxy)):
            box = boxes.xyxy[i]
            prob = probs[i]
            if prob.max() >= umbral_confianza:
                x1, y1, x2, y2 = map(int, box)
                etiqueta = names[int(prob.argmax())]  
                confianza = prob.max()

              
                cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.putText(imagen, f"{etiqueta} ({confianza:.2f})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


cv2.imshow("Deteccion de un tornillo", imagen)


cv2.waitKey(0)
cv2.destroyAllWindows()
