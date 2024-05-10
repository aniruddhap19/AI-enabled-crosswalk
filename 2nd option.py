import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import serial
import time
SerialObj = serial.Serial('ttyUSBx')
SerialObj.baudrate = 9600 
SerialObj.parity = 'N'
SerialObj.stopbits = 1
def senddata1():
    SerialObj.write(b'1')
    time.sleep(15)
def senddata2():
    SerialObj.write(b'2')
    time.sleep(15)

#if SerialObj.in_waiting > 0:
 #   if data_received = SerialObj.readline().decode().strip() == '3':
  #      if (c > 2) and (c < 4):
   #         senddata1()
    #        time.sleep(11)
     #   elif c<2:
      #      senddata2(6)
        

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)
# size = (800, int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# # size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# print(size)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'x264' doesn't work
# out = cv2.VideoWriter('./testing/res_t2.mp4',fourcc, 20.0,(980,498))  # 'False' for 1-ch instead of 3-ch for color



while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame,(980,498))
    # frame = imutils.resize(frame, width=800)
    rects, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    c=1
    for x, y, w, h in pick:
        cv2.rectangle(frame, (x, y), (w, h), (139, 34, 104), 2)
        cv2.rectangle(frame, (x, y - 20), (w,y), (139, 34, 104), -1)
        cv2.putText(frame, f'P{c}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        c += 1

    cv2.putText(frame, f'Total Persons : {c - 1}', (20, 450), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255,255), 2)
    cv2.imshow('output', frame)
    # out.write(frame)
    # cv2.resizeWindow('Car Detection System', 600, 600)

    if(c>4):
        senddata1()
        print("sent code 1")
        time.sleep(11)
    if SerialObj.in_waiting > 0:
        if SerialObj.readline().decode().strip() == '3':
            if (c > 2) and (c < 4):
                senddata1()
                print("sent code 1")
                time.sleep(11)
            elif c<2:
                senddata2()
                print("sent code 2")
                time.sleep(6)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

SerialObj.close()
cv2.destroyAllWindows()


    