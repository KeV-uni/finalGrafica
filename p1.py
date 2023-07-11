import cv2
import pickle
import numpy as np

casillas = []
with open('casillas.pkl', 'rb') as file:
    casillas = pickle.load(file)

video = cv2.VideoCapture('jugadaAjedrez.mp4')
video.set(cv2.CAP_PROP_POS_MSEC, 36 * 1000)

while True:
    check, img = video.read()
    imgBN = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTH = cv2.adaptiveThreshold(imgBN, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgTH, 5)
    kernel = np.ones((5, 5), np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)

    for x, y, w, h in casillas:
        espacio = imgDil[y:y+h+10, x:x+w+10]
        count = cv2.countNonZero(espacio)
        cv2.putText(img, str(count), (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
        cv2.rectangle(img, (x-10, y-10), (x-w+10, y+h-30), (255,0,0), 1)
        if count < 900:
            cv2.rectangle(img, (x-10,y-10), (x-w+10, y+h-30), (0,255,0), 2)

    cv2.imshow('video', img)
    # cv2.imshow('video TH', imgTH)
    # cv2.imshow('video Median', imgMedian)
    # cv2.imshow('video Dilatada', imgDil)
    cv2.waitKey(10)