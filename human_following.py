import cv2
import imutils
import threading
import numpy as np
import serial
import time
def send_object():
        global position
        position = "Center"
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            frame = imutils.resize(frame,width=1000)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                frame_center_x = frame.shape[1] // 2
                face_center_x = x + w // 2
                frame_center_y = frame.shape[1] // 2
                face_center_y = y + h // 2
                if face_center_x < frame_center_x - 50:
                    position = "Left"
                elif face_center_x > frame_center_x + 50:
                    position = "Right"
                else:
                    position = "Center"
                # if face_center_y < frame_center_y - 200:
                #     positiony = "TOP"
                # elif face_center_y > frame_center_y + 50:
                #     positiony = "BOTTOM"
                # else:
                #     positiony = "Center"        
                cv2.putText(frame, position, (x, y - 27), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                # cv2.putText(frame, positiony, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            cv2.imshow('Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
def send_data():
        ser = serial.Serial('COM11', 115200)
        while True:
            if position == 'Left':
                ser.write(b'Left')
            elif position == 'Right':
                ser.write(b'Right')
            else:
                ser.write(b"Center")
            data = ser.readline()
            print("Received:", data.decode())
        ser.close() 
thread1 = threading.Thread(target=send_object)
thread2 = threading.Thread(target=send_data)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Threads have finished executing.")