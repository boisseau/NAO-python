import qi

session = qi.Session()
session.connect("192.168.0.158")
tts = session.service('ALTextToSpeech')

for patate in range(1,11):
    tts.say(str(patate))