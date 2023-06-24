

import speech_recognition as srn

def Listen(): # audio recognition
    q = srn.Recognizer()
    with srn.Microphone() as source:
        print("...")
        q.pause_threshold = 1
        audio = q.listen(source,0,5)

    try:
        print("...recognising...")    
        query = q.recognize_google(audio, language='eng-in')
        print(f"You said: {query}")

    except: 
        return " "

    query = str(query)
    return query.lower()

Listen()