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

angles1 = [0.0,-pi/4]
motionProxy.setAngles(names, angles1, fractionMaxSpeed)
tts.say('haut')
time.sleep(pause)
angles2 = [0.0,pi/4]
motionProxy.setAngles(names, angles2, fractionMaxSpeed)
tts.say('bas')
time.sleep(pause)
angles3 = [pi/4,0.0]
motionProxy.setAngles(names, angles3, fractionMaxSpeed)
tts.say('gauche')
time.sleep(pause)
angles4 = [-pi/4,0.0]
motionProxy.setAngles(names, angles4, fractionMaxSpeed)
tts.say('droite')
time.sleep(pause)
angles5 = [0,0]
motionProxy.setAngles(names, angles5, fractionMaxSpeed)
tts.say('devant')
#1=haut
#2=bas
#3=gauche
#4=droite
#5=normal