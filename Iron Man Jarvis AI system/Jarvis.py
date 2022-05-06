import google
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from googlesearch import search

from wikipedia import exceptions


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
# print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I'm Jarvice...  sir please tell me how may I help you.")


def takeCommand():
    """It takes microphone input from user and returns a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said : {query}\n ")
        speak(f"You said, {query}. ")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def send_email(to, content):
    speak("Sending your email..., please wait...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("nikhilsaraswat2605@gmail.com", "nikhilsaraswat")
    server.sendmail("nikhilsaraswat2605@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if "jarvis stop" in query or "stop" in query or 'quit' in query:
            print("Quiting...")
            speak("I am Quiting... Thank you for using me!")
            break

        elif "wikipedia" in query:
            try:
                print("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(f"According to Wkipedia {result} ")
            except Exception as e:
                print(e)
                speak(e)

        elif "open google" in query:
            webbrowser.open_new_tab("google.com")

        elif "open youtube" in query:
            webbrowser.open_new_tab("youtube.com")

        elif "open facebook" in query or "open fb" in query:
            webbrowser.open_new_tab("facebook.com")

        elif "play music" in query or "play song" in query:
            try:
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                print(songs)
                song_number = random.randint(0, len(songs)-1)
                os.startfile(os.path.join(music_dir, songs[song_number]))
            except Exception as e:
                print(e)
                speak(e)

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, the time is {strtime} ")

        elif "open code" in query:
            codepath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "send email to nikhil" in query:
            try:
                speak("What should I say...")
                content = takeCommand()
                to = "ramsevaksharma95@gmail.com"
                send_email(to, content)
                print("Email sent successfully...")
                speak("Email sent successfully...")
            except Exception as e:
                print(e)
                speak("Sorry bro... I couldn't send your email to nikhil!")

        elif "change voice" in query or "change the voice" in query:
            # print(engine.getProperty('voice'))
            # print(voices[0].id)
            if engine.getProperty('voice') == voices[0].id:
                engine.setProperty('voice', voices[1].id)
                speak("Hello sir...I am Alexa")
            else:
                engine.setProperty('voice', voices[0].id)
                speak("Hello sir...I am Jarvis")
            speak("The voice changed...Now enjoy with my voice.")


        elif "google" in query:
            if query == "":
                continue
            query = query.replace("google","")
            my_results_list = []
            print("Searching on google...")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                my_results_list.append(j)
            for i in my_results_list:
                print(i)
            webbrowser.open("https://google.com/search?q=%s" % query)

        elif "search on youtube" in query:
            if query == "":
                continue
            query = query.replace("search on youtube","")
            print("Searching on youtube...")
            webbrowser.open("https://youtube.com/search?q=%s" % query)
