import numpy as np
import cv2

cascade = cv2.CascadeClassifier('./classifier/cascade.xml')

for i in range(1,10):
    name = './images/t'+str(i)+'.jpg'
    img = cv2.imread(name)
    img = cv2.resize(img, (450, 600))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    doors = cascade.detectMultiScale(gray, 1.5, 7, cv2.CASCADE_SCALE_IMAGE, (100,100), (600,600))
    maxx = 0
    maxy = 0
    for (x, y, w, h) in doors:
        if x > maxx:
            maxx = x
        if y > maxy:
            maxy = y
    if maxx != 0 and maxy != 0:
        cv2.rectangle(img, (maxx, maxy), (maxx + w, maxy + h), (255, 0, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
