import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id )

def say(Text):
    print(" ")
    print(f"AIbot: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print(" ")