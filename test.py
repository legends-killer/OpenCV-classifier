import numpy as np
import cv2
cascade = cv2.CascadeClassifier('./classifier/cascade.xml')

for i in range(1,10):
    name = './images/t'+str(i)+'.jpg'
    img = cv2.imread(name)
    img = cv2.resize(img, (550, 800))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    doors = cascade.detectMultiScale(gray, 1.1, 7, cv2.CASCADE_SCALE_IMAGE, (100,100), (800,800))
    maxx = 0
    maxy = 0
    ww = 0
    hh = 0
    for (x, y, w, h) in doors:
        if x > maxx:
            maxx = x
            ww = w
        if y > maxy:
            maxy = y
            hh =h
    ansx = max(maxx+ww,400)
    ansy = max(maxy+hh,500)
    print(str(ansx)+' '+str(ansy))
    if maxx != 0 and maxy != 0:
        cv2.rectangle(img, (maxx, maxy), (ansx, ansy), (255, 0, 0), 2)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
