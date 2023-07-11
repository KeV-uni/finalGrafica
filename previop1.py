import cv2
import pickle

img = cv2.imread('tablero.png')

casillas = []

for _ in range(32):
    espacio = cv2.selectROI('espacio', img, False)
    cv2.destroyWindow('espacio')
    casillas.append(espacio)

    for x, y, w, h in casillas:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 1)

with open('casillas.pkl', 'wb') as file:
    pickle.dump(casillas, file)