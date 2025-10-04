import speech_recognition as sr
import webbrowser
import pyttsx3
import musicc
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi ="b65c3a8fa5624f3daa7e77d3a43b97a8"

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()
def aiprocess(command):
    client = OpenAI(
    api_key="AIzaSyBpQoift-LKZjMzS1Pp2LazLJbNL5IXdxE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    completion = client.chat.completions.create(
        model="gemini-flash-latest",   # <-- Pick a model from the printed list
        messages=[
            {"role": "system", "content": "You are Jarvis skilled in general tasks like Alexa and Google Cloud"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicc.music_dir[song]
        webbrowser.open(link)
    elif "news" in c.lower() or "headline" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            data= r.json()
            articles = data.get('articles',[])
            if articles:
                for article in articles:
                    # print("Speaking:", article['title'])  
                    speak(article['title'])
            else:
                speak("Sorry,No news found.!")

    else:
        output = aiprocess(c)
        speak(output)

if __name__ =="__main__":
    speak("Intializing Jarvis.....")
    while True:
        #Listen for the word Coco
        #obtian audi from microphone
        r = sr.Recognizer()
        print("Recognizing")
        #pip install sphinx
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=5,phrase_time_limit=7)
            word= r.recognize_google(audio)
            print("Heard:", word)
            if word.lower() == "jarvis":
                speak("Yes Sir")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis is active....")
                    audio = r.listen(source, timeout=5, phrase_time_limit=7)
                    command= r.recognize_google(audio)
                    print("Command heard:", command)


                    processcommand(command)

        except Exception as e :
            print(f"error: {e}")
