import qi
import math
session = qi.Session()
session.connect("192.168.0.158")
postureProxy = session.service('ALRobotPosture')
motionProxy = session.service('ALMotion')
postureProxy.goToPosture("Stand", 1.0)
x  = 0
y  = 0
theta  = math.pi
motionProxy.moveTo(x, y, theta)
motionProxy.moveTo(x, y, theta)
postureProxy.goToPosture("Crouch", 1.0)