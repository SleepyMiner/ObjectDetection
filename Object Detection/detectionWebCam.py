from ultralytics import YOLO  
import cv2 

model = YOLO('yolov8s.pt')  


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

ret = True
while ret:
    ret, frame = cap.read()
    
    results = model.track(frame, persist=True)

    frame_ = results[0].plot()
    cv2.imshow('frame', frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

