import random
import qi

session = qi.Session()
session.connect("192.168.0.158")
tts = session.service('ALTextToSpeech')

pas_fini = True
trouver_le_nombre=True
a_deviner=random.randint(1, 999)
mini= 1
maxi= 999
while trouver_le_nombre:
    nombre = int((mini + maxi)/2)
    tts.say(str(nombre))
    if nombre < a_deviner:
        mini = nombre 
        tts.say("c'est plusse")
    elif nombre > a_deviner:
        maxi = nombre 
        tts.say("c'est moins")
    else:
        trouver_le_nombre = False
        tts.say("c'est bon")