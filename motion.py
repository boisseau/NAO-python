import qi
import time
from math import *
session = qi.Session()
session.connect("192.168.0.158")
motionProxy = session.service('ALMotion')
motionProxy.setStiffnesses("Head",0.8)
tts = session.service('ALTextToSpeech')
names = ["HeadYaw","HeadPitch"]
fractionMaxSpeed= 0.2
pause=0.7

angles_et_mots = [
    ([0.0,-pi/4], 'haut'),
    ([0.0,pi/4], 'bas'),
    ([pi/4,0.0], 'gauche'),
    ([-pi/4,0.0], 'droite'),
    ([0.0,0.0], 'devant'),
]

for (angles, mot) in angles_et_mots:
    motionProxy.setAngles(names, angles, fractionMaxSpeed)
    tts.say(mot)
    time.sleep(pause)
