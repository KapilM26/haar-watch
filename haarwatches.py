#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:21:43 2019

@author: kapil
"""

import cv2
import numpy as np

watch_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

while True:
  ret,img = cap.read()
  grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  watches = watch_cascade.detectMultiScale(grey,2,3)
  for (x,y,w,h) in watches:
    cv2.rectangle(img, (x,y), (x+w,y+h),(255,255,0),2)
  cv2.imshow('img',img)
  if (cv2.waitKey(5) & 0xFF) == 27:
    break
cv2.destroyAllWindows()
cap.release()