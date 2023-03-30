import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') ##to get the voices 
voices = engine.getProperty('voices')## to get the voice input from user 
print (voices[0].id)
engine.setProperty("voices", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():##this fuction allows the bot to wish the person according to time 
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak ("good morning")

    elif hour>=12 and hour<18:
        speak ("good afternoon")

    else:
        speak("good evening")

    speak ('hey boss this is jarvis how may i help you')
    

def takecommand():
    #it take microphone input from the user and returns the string output 

    r = sr.Recognizer()
    with sr.Microphone() as source: ##this is the source where bot will take the inputs and print the output 
        print('listening ....')
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n") 

    except Exception as e:
        #print(e)

        print('say that again')
        return"none"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login ("kondegalomkar123@gmail.com" ,"omkar@111999")
    server.sendmail('kondegalomkar123@gmail.com', to , content)
    server.close()


if __name__ == "__main__":
    wishme()
    #while True:
    if 1:
        query = takecommand().lower()##this lower helps you to get the website open for you as Google will be also open 
                                     ##by just writing google 

    #lets start writing the logic for the multple inputs we are going to fetch from the user 
        if "wikipedia" in query:
            print('searching wikipedia...')
            query = query.replace("wikipedia",'')
            results = wikipedia.summary(query, sentences=2)
            speak ("according to wikipedia")
            print(results)
            speak (results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open googel ' in query:
            webbrowser.open('google.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"boss the time is {strTime}")
            print(strTime)

        elif "open code " in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif " email to omkar" in query:
            try:
                speak ('what should i say')
                content = takecommand()
                to ="kondegalomkar2025@gmail.com"
                sendEmail (to,content)
                speak ('your email has been sent')

            except Exception as e:
                print(e)
                speak('sorry boss i am not able to sent the email ')

        