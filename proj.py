import cv2
import numpy as np
import os
# import pyglet
# import pygame
import winsound

# player = pyglet.media.Player()
# source = pyglet.media.load('Lakshya.wav',streaming=False)
# player.queue(source)
# player.play()
# player.volume=0.8

count_c = 0
count_o = 0
o_count = 0
c_count = 0

face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cas = cv2.CascadeClassifier('haarcascade_eye.xml')
open_palm_cas = cv2.CascadeClassifier('open_palm.xml')
closed_palm_cas = cv2.CascadeClassifier('closed_palm.xml')

cap = cv2.VideoCapture(cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    palm_o = open_palm_cas.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in palm_o:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    if len(palm_o)>0:
        count_o += 1

    palm_c = closed_palm_cas.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in palm_c:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
    if len(palm_c)>0:
        count_c += 1

    cv2.imshow('Image', frame)
    k = cv2.waitKey(1) & 0xFF

    if k == 27 or count_c == 10 or count_o == 10:
        break

cap.release()
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    o_palm = open_palm_cas.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in o_palm:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    if len(o_palm)>0:
        o_count += 1

    c_palm = closed_palm_cas.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in c_palm:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
    if len(c_palm)>0:
        c_count += 1

    cv2.imshow('Image2',frame)
    k = cv2.waitKey(1) & 0xFF

    if k == 27 or o_count == 10 or c_count == 10:
        break

cap.release()
cv2.destroyAllWindows()

def const():
    print("Brightness will remain constant !!")

def inc():
    winsound.PlaySound("Lakshya.wav",winsound.SND_ALIAS)
    #print('Inc')

def dec():
    winsound.PlaySound("IMA_Song.wav",winsound.SND_ALIAS)
    #print('Dec')

if count_c == 10 and o_count == 10:
    inc()
elif count_o == 10 and c_count == 10:
    dec()
else:
    const()