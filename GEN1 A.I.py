import win32com.client
import gem
import time
import webbrowser
import speech_recognition as sr
r = sr.Recognizer()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello I am gen1 A I how can i help you")
def takequerry():
 with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold =1
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio,language = "en-in")
        return text
    except Exception as e:
        return "Sorry,some error occurs."
lstweb = [["youtube","https://youtube.com"],["google",'https://google.com'],["wikipedia","https://wikipedia.com"],["chatgpt","https://chatgpt.com"],["github","https://github.com"]]
def response_loop():
 while True:
    query = takequerry()
    if "stop" in query.lower():
       speaker.Speak("Goodbye sir")
       break
    opened = False

    for task in lstweb:
        if (f"open {task[0]}") in query.lower():
            speaker.Speak(f"Opening {task[0]} sir")
            webbrowser.open(task[1])
            opened = True
            break
    if not opened :
     if "the time right now" in query.lower():
        lc = time.localtime()
        hours = time.strftime("%H",lc)
        mins = time.strftime("%M",lc)
        print(f"Sir its {hours}hours and {mins}minutes. ")
        speaker.Speak(f"sir its {hours}hours and {mins}minutes. ")
     elif "date" in query.lower() or "today's date" in query.lower():
        lc = time.localtime()
        year = time.strftime("%Y",lc)
        month = time.strftime("%m",lc)
        day = time.strftime("%d",lc)
        print(f"Sir the date is {day}-{month}-{year}.")
        speaker.Speak(f"sir the date is {day} {month} {year} ")
     else:
        print(gem.query(query))
        speaker.Speak(gem.query(query))
 speaker.Speak("Thank you for using me sir let me know if you need further information")
if __name__=="__main__":
    response_loop()
        