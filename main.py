import qi

session = qi.Session()
session.connect("192.168.0.158")
tts = session.service('ALTextToSpeech')

for patate in ('1', '2', '3'):
    tts.say(patate)