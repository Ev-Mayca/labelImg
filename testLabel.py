# -*- coding:UTF-8 -*-
#########################################################################
# File Name: testLabel.py
# Author: Ev
# mail: wang2011yiwei@sina.com
# Created Time: Thu Jan 16 17:39:09 2020
#########################################################################
#!/usr/bin/python
try:
    from PyQt5.QtGui import QImage
except ImportError:
    from PyQt4.QtGui import QImage

import os.path
import cv2 as cv
import sys
from libs.yolo_io import YoloReader
from libs.yolo_io import TXT_EXT

#folderPath='/mnt/d/work/parking/picture/guan'
folderPath='/mnt/d/work/parking/picture/pic_label/chewei2/'
images = []
for root,dirs,files in os.walk(folderPath):
    for file in files:
        if file.lower().endswith('png'):
            relativePath = os.path.join(root,file)
            path = (os.path.abspath(relativePath))
            images.append(path)

images.sort()
for image in images:
    img = cv.imread(image)
    print(image[-9:-4])
    txtPath = os.path.splitext(image)[0] + TXT_EXT
    if os.path.isfile(txtPath) is False:
        break
    qimg = QImage()
    qimg.load(image)
    yoloParseReader = YoloReader(txtPath,qimg)
    shapes = yoloParseReader.getShapes()
    for shape in shapes:
        #print(shape[0])
        #break
        if 'car' in shape[0]:
            #print(shape[1])
            cv.line(img,shape[1][0],shape[1][1],(0,0,255),3)
            cv.line(img,shape[1][1],shape[1][2],(0,0,255),3)
            cv.line(img,shape[1][2],shape[1][3],(0,0,255),3)
            cv.line(img,shape[1][3],shape[1][0],(0,0,255),3)
    cv.imshow("hello",img)
    key = cv.waitKey(100)&0xff
    if key == 27:
        cv.destroyAllWindows()
        break

