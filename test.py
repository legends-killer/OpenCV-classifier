import numpy as np
import cv2

cascade = cv2.CascadeClassifier('./temp/cascade.xml')

for i in range(1,7):
    name = './images/t'+str(i)+'.jpg'
    img = cv2.imread(name)
    img = cv2.resize(img, (600, 450))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    doors = cascade.detectMultiScale(gray, 10, 5, cv2.CASCADE_SCALE_IMAGE, (150,150), (600,600))

    for (x, y, w, h) in doors:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
