

import speak
import datetime
import wikipedia
import pywhatkit
from listen import Listen

def Time():
    time = datetime.datetime.now().strftime("%H : %M : %S")
    speak.say(time)
    
def Date():
    date = datetime.date.today()
    speak.say(date)
    
def withoutInput(query):
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
        
def InputExecute(tag, query) :
    if "wikipedia" in tag:
        name = str(query).replace("what is", "").replace("about", "").replace("who is", "").replace("quora", "")
        r = wikipedia.summary(name)
        speak.say(r)
    
    elif "google" in tag:
        name = str(query).replace("search", "").replace("please search", "")
        pywhatkit.search(query)
        
    elif "whatsapp" in tag:
        speak.say("what should I convey!")
        wp = Listen()
        speak.say("Please enter number and by when should I convey message")
        pywhatkit.sendwhatmsg("+91"+input(),f"{wp}", int(input()), int(input()))
        speak.say("message sent")
    
    elif "email" in tag:
        speak.say("Please enter valid Email Id")
        sender = input()
        speak.say("Please enter password")
        password = input()
        speak.say("What is the subject")
        subject = Listen()
        speak.say("What is the content")
        content = Listen()
        speak.say("Please enter receiver's Email Id")
        receiver = input()
        pywhatkit(sender.islower(),password,subject,content,receiver)
    
    elif "youtube" in tag:
        speak.say("What should I play for you")
        yt = Listen()
        pywhatkit.playonyt(f"{yt}")
        speak.say("Now playing" + f"{yt}")
        
        