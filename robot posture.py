import qi
import math
import time
session = qi.Session()
session.connect("192.168.0.158")
postureProxy = session.service('ALRobotPosture')
motionProxy = session.service('ALMotion')
tts = session.service('ALTextToSpeech')   
names  = ["HeadYaw", "HeadPitch"]
angles  = [0.0, 0.0]
fractionMaxSpeed  = 0.2
motionProxy.setAngles(names, angles, fractionMaxSpeed)
tts.say("Salut,moi c'est Nao")
postureProxy.goToPosture("Stand", 1.0)
x  = 0.9
y  = 0
theta  = 0
motionProxy.moveTo(x, y, theta)
postureProxy.goToPosture("StandZero", 1.0)
postureProxy.goToPosture("Stand", 1.0)
tts.say("Il fait beau aujourd'hui")
x  = 0
y  = 0
theta  = math.pi/2
motionProxy.moveTo(x, y, theta)
x  = 0.5
y  = 0
theta  = 0
motionProxy.moveTo(x, y, theta)
postureProxy.goToPosture("Crouch", 1.0)
tts.say("C'est pas très propre ici")
time.sleep(1.0)
postureProxy.goToPosture("Stand", 1.0)
x  = 0
y  = 0
theta  = math.pi/2
motionProxy.moveTo(x, y, theta)
tts.say("Il y pas beaucoup de monde dans le coin")
x  = 0.3
y  = 0
theta  = 0
motionProxy.moveTo(x, y, theta)
tts.say("Je croie que je me suis perdu")
x  = 0
y  = 0
theta  = math.pi/2
motionProxy.moveTo(x, y, theta)
x  = 0.4
y  = 0
theta  = 0
motionProxy.moveTo(x, y, theta)
x  = 0
y  = 0
theta  = math.pi/-2
motionProxy.moveTo(x, y, theta)
tts.say("Cool j'ai retrouvé mon chemin")
x  = 0.6
y  = 0
theta  = 0
motionProxy.moveTo(x, y, theta)
x  = 0
y  = 0
theta  = math.pi
motionProxy.moveTo(x, y, theta)
tts.say("Je suis fatigué,je vais m'assoir un peu")
postureProxy.goToPosture("SitRelax", 1.0)
