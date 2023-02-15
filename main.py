import random
import qi

session = qi.Session()
session.connect("192.168.0.158")
tts = session.service('ALTextToSpeech')

pas_fini = True
a_deviner=random.randint(1,999)
while pas_fini:
    nombre = int(input('Devine le nombre : '))
    if nombre < a_deviner:
        tts.say("c'est plusse")
    elif nombre > a_deviner  :
        tts.say("c'est moins")
    else:
        pas_fini = False
        tts.say("c'est bon")