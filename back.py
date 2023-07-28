import numpy as np
import cv2

# Charger l'image et la convertir en niveaux de gris
image = cv2.imread("drepano3.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un seuillage adaptatif pour améliorer le contraste
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)

# Détecter les cercles dans l'image seuillée
circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Vérifier si des cercles ont été détectés
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    #Afficher le nombre de cercles detectes 
    print("Nombre de cercles detectes :", len(circles))
    # Dessiner les cercles sur l'image d'origine
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)

    # Afficher l'image avec les cercles détectés
    cv2.imshow("Output", image)
    cv2.waitKey(0)
else:
    print("Aucun cercle détecté.")