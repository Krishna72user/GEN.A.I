import win32com.client
import gem
import time
import webbrowser
import speech_recognition as sr
r = sr.Recognizer()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def takequerry(vt):
   if vt=='voice':
         with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold =1
            audio = r.listen(source)
            try:
               text = r.recognize_google(audio,language = "en-in")
               print(f"You said: {text}")
               return text
            except Exception as e:
               return "Sorry,some error occurs."
   elif vt=='text':
         text = input("Enter your query: ")
         return text
lstweb = [["youtube","https://youtube.com"],["google",'https://google.com'],["wikipedia","https://wikipedia.com"]
         ,["chatgpt","https://chatgpt.com"],["github","https://github.com"]]
def voice_response_loop():
 date = time.strftime("%d-%m-%Y")
 times = time.strftime("%H:%M")
 while True:
    query = takequerry(voit)
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
     if "what is the time right now" in query.lower() or "time right now" in query.lower() or "time" in query.lower():
        lc = time.localtime()
        hours = time.strftime("%H",lc)
        mins = time.strftime("%M",lc)
        text = (f"Sir its {hours}hours and {mins}minutes. ")
        speaker.Speak(f"sir its {hours}hours and {mins}minutes. ")
        with open("Output.txt","w") as f:
            f.write("Output: "+ text)
        with open("History.txt","a") as f:
            f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
     elif "what is today's date" in query.lower() or "today's date" in query.lower() or"date" in query.lower():
        lc = time.localtime()
        year = time.strftime("%Y",lc)
        month = time.strftime("%m",lc)
        day = time.strftime("%d",lc)
        text = (f"Sir the date is {day}-{month}-{year}.")
        speaker.Speak(f"sir the date is {day} {month} {year} ")
        with open("Output.txt","w") as f:
            f.write("Output: "+ text)
        with open("History.txt","a") as f:
            f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
     else:
        text = (gem.query(query))
        speaker.Speak(gem.query(query))
        with open("Output.txt","w") as f:
            f.write("Output: "+ text)
        with open("History.txt","a") as f:
             f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
        with open("History.txt","a") as f:
            f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
 with open("History.txt","a") as f:
            f.write("Session Ended.")
 speaker.Speak("Thank you for using me sir let me know if you need further information")
def text_response_loop():
 date = time.strftime("%d-%m-%Y")
 times = time.strftime("%H:%M")
 while True:
    query = takequerry(voit)
    if "stop" in query.lower():
       print("Goodbye sir.")
       break
    opened = False

    for task in lstweb:
        if (f"open {task[0]}") in query.lower():
            print(f"Opening {task[0]} sir")
            webbrowser.open(task[1])
            opened = True
            break
    if not opened :
     if "what is the time right now" in query.lower() or "time right now" in query.lower() or "time" in query.lower():
        lc = time.localtime()
        hours = time.strftime("%H",lc)
        mins = time.strftime("%M",lc)
        text = (f"Sir its {hours}hours and {mins}minutes. ")
        with open("Output.txt","w") as f:
            f.write("Output: "+ text)
        with open("History.txt","a") as f:
            f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
     elif "what is today's date" in query.lower() or "today's date" in query.lower() or"date" in query.lower():
        lc = time.localtime()
        year = time.strftime("%Y",lc)
        month = time.strftime("%m",lc)
        day = time.strftime("%d",lc)
        text = (f"Sir the date is {day}-{month}-{year}.")
        with open("Output.txt","w") as f:
            f.write("Output: "+ text)
        with open("History.txt","a") as f:
            f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
     else:
        text = (gem.query(query))
        with open("Output.txt","w") as f:
            f.write("Output: "+ text)
        with open("History.txt","a") as f:
             f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
        with open("History.txt","a") as f:
            f.write("Date:"+date+"\n"+"Time: "+times+"\n"+"Output: "+text+"\n")
 with open("History.txt","a") as f:
            f.write("Session Ended.")
 print("Thank you for using me sir let me know if you need further information")
if __name__=="__main__":
   voit = input("Enter 'voice' for voice communication and 'text' for text communication: ").lower()
   if voit =="voice":
      speaker.Speak("Hello I am gen1 A I how can i help you")
      voice_response_loop()
   elif voit =="text":
       print("Hello i am GEN1.A.I how can i help you?")
       text_response_loop()
   else:
      print("Invalid input.")
   
        