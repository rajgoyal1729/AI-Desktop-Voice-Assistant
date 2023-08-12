import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import datetime
import webbrowser
import subprocess

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")


    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Harleen! How can i help you")    
  
    
def takeCommand():
    # it takes microphone input from user and return srtring output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)       
        print("Sorry! I didn't get you")
        return "None"
    return query

if __name__=="__main__":

    WishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  


        elif 'open google' in query:
            webbrowser.open("google.com")  

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")   

        elif 'play song' in query:
            subprocess.Popen(['start','','Spotify'],shell=True)

        elif 'open calculator' in query:
            subprocess.Popen(['start','Calculator'],shell=True)  

        elif 'time' in query:
            Time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{Time}")

        elif 'thank you' in query:
            speak("Your Welcome! It was nice talking to you")
            exit(0)           





    
    
        

