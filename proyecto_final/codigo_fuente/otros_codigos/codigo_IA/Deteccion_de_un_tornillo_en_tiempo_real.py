import cv2
from ultralytics import YOLO


modelo = YOLO("best.pt") 


captura = cv2.VideoCapture(0) 
if not captura.isOpened():
    print("Error al abrir la cámara.")
    exit()


umbral_confianza = 0.3 

while True:

    ret, frame = captura.read()
    if not ret:
        print("Error al capturar el frame.")
        break


    resultados = modelo(frame)


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

                   
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                  
                    cv2.putText(frame, f"{etiqueta} ({confianza:.2f})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    cv2.imshow("Deteccion de un tornillo en tiempo real", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
