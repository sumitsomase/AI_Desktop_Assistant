import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import time
import requests
import re
import pyautogui


# initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# define assistant name
assistant_name = "Infoboat"


# define assistant speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define assistant greeting function
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("good morning sir !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good afternoon sir !")
    else:
        speak("Good Evening!")
        print("Good Evening sir !")
    speak(f"I am {assistant_name}. How can I assist you?")
    print(f"I am {assistant_name}. How can I assist you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('patilshailesh3314@gmail.com', 'fjvjpihipdrrthno')
    server.sendmail('shailu.patil2004@gmail.com', to, content)
    server.close()

# define assistant command function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


# Define a function to play rock-paper-scissors
def play_rps():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = ""
    while user_choice not in options:
        print("Choose rock, paper, or scissors:")
        user_choice = takeCommand()
    print("You chose", user_choice)
    print("computer choice is", computer_choice)
    engine.say("computer choice is", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
        engine.say("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        engine.say("You win!")
    else:
        print("You lose!")
        engine.say("You lose!")
    engine.runAndWait()


# Function to search for IPL match score on Google
def score():
    try:
        # Perform a Google search for current IPL cricket score
        query = "cricket score"
        response = requests.get(f"https://www.google.com/search?q={query}")

        # Extract the score from the search results using regular expressions
        pattern = r"([0-9]+/[0-9]+)"
        pattern1 = r"([0-9]+/[0-9]+)"
        
        matches = re.findall(pattern, response.text)
        matches = re.findall(pattern1, response.text)


        score = matches[0] if matches else "No score found"
        score1 = matches[1] if matches else "No score found"


        print(f"The current IPL cricket score of first inning is {score}")
        print(f"The current IPL cricket score of second inning is {score1}")
        speak(f"The current IPL cricket score of first inning is {score} and score of second inning is {score1}")
        if score > score1:
            print("First inning won the match ")
            speak(" and First inning won the match ")
        else:
            print("Second inning won the match")
            speak("and Second inning won the match")
    except Exception as e:
        speak("Sorry, I couldn't fetch the current IPL cricket score")


# Define a function to tell a joke
def tell_joke():
    jokes = [
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a shark? Frostbite!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What's the difference between a poorly dressed man on a trampoline and a well-dressed man on a trampoline? Attire!",
        "Why did the chicken cross the playground? To get to the other slide!"
    ]
    joke = random.choice(jokes)
    print("Here's a joke for you:", joke)
    engine.say(joke)
    engine.runAndWait()


# Function to fetch and read the latest news
def news():
    try:
        # Send a request to the news website
        url = "https://www.indianexpress.com/"
        response = requests.get(url)

        # Extract the news headlines using regular expressions
        pattern = r"<h2.*?>(.*?)<\/h2>"
        headlines = re.findall(pattern, response.text)

        # Read the headlines
        for i, headline in enumerate(headlines, start=1):
            speak(f"News {i}: {headline.strip()}")

    except Exception as e:
        speak("Sorry, I couldn't fetch the latest news")


def open_calendar():
    os.system("start outlook:calendar")


# Define a function to set an alarm
def set_alarm():
    alarm_time = ""
    while not alarm_time:
        print("What time do you want to set the alarm for? (Use the format hh:mm)")
        alarm_time = takeCommand()
        try:
            alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M')
        except:
            print("Sorry, I didn't understand that time. Please try again.")
            alarm_time = ""

    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == alarm_time.strftime('%H:%M'):
            print("Time's up!")
            engine.say("Time's up!")
            engine.runAndWait()
            break
        else:
            time.sleep(60) 

# main program loop
if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on user input
        if 'wikipedia' in query or 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

         # Command for opening youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        # Command for opening facebook
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        # Command for opening instagram
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

         # Command for opening whatsapp
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open saurav joshi vlog' in query:
            webbrowser.open("youtube.com/channel/UCjvgGbPPn-FgYeguc5nxG4A")

        # Command for opening snapchat
        elif 'open snapchat' in query:
            webbrowser.open("snapchat.com")

        # Command for opening tutorials point
        elif 'open tutorials point' in query:
            webbrowser.open("tutorialspoint.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        # Command for google
        elif 'open google' in query:
            webbrowser.open("google.com")

        # Command for google
        elif 'open chat gpt' in query:
            webbrowser.open("openai.com")

        # Command for opening stackoverflow
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif "play game" in query:
            play_rps()

        elif "joke" in query:
            tell_joke()

        elif "set alarm" in query:
            set_alarm()

        if 'how are you' in query:
            speak("I am absolutely fine sir ! what about you sir") 
            print("I am absolutely fine sir ! what about you sir") 

        if 'i am also fine' in query:
            speak("ok sir fine ! its Great to see u back can you tell me how ay i help you") 
            print("ok sir fine ! its Great to see u back can you tell me how ay i help you") 

        elif 'play music' in query:
            music_dir = 'D:\music'  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play song' in query:
            music_dir = 'D:\music'  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play songs' in query:
            music_dir = 'D:\music'  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'open code' in query:
            code_path ="C:\\Users\\shrikrushna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open word' in query or 'open world' in query:
            code_path ="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(code_path)

        elif 'close word' in query or 'close world' in query:
            os.system("taskkill /f /im WINWORD.EXE")
            speak("Closing the word application")

        elif 'open chrome' in query:
            code_path ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(code_path)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            speak("Closing the chrome application")

        elif 'open powerpoint' in query:
            code_path ="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(code_path)
         
        elif 'close powerpoint' in query or 'close PowerPoint' in query:
            os.system("taskkill /f /im POWERPNT.EXE")
            speak("Closing the application")

        elif 'open PowerPoint' in query:
            code_path ="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(code_path)
        
        elif 'open excel' in query:
             code_path ="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
             os.startfile(code_path)

        elif 'close excel' in query:
            os.system("taskkill /f /im EXCEL.EXE")
            speak("Closing the application")

        elif 'open setting' in query:
             code_path ="ms-settings:"
             os.startfile(code_path)

        # elif 'close setting' in query:
        #     os.system("taskkill /f /im ms-settings")
        #     speak("Closing the application")

        elif 'open microsoft edge' in query:
             code_path ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
             os.startfile(code_path)

        elif 'close microsoft edge' in query:
            os.system("taskkill /f /im msedge.exe")
            speak("Closing the application")

        elif 'open outlook' in query:
             code_path ="C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
             os.startfile(code_path)

        elif 'open onenote' in query:
            code_path ="C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
            os.startfile(code_path)

        elif 'open xmapp' in query:
            code_path ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\XAMPP"
            os.startfile(code_path)
        
        elif 'open c folder' in query:
            code_path ="C:\\"
            os.startfile(code_path)

        elif 'close c folder' in query or 'clothes see folder' in query:
            pyautogui.hotkey('alt', 'f4') 
            speak("Closing C folder")

        elif 'open notepad' in query:
            code_path ="C:\\Windows\\System32\\notepad"
            os.startfile(code_path)

        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")
            speak("Closing Notepad")

        elif 'open mail' in query or 'open email' in query:
            code_path ="mailto:"
            os.startfile(code_path)

        # elif 'close mail' in query or 'clothes gmail' in query:
        #    pyautogui.hotkey('alt', 'f4') 
        #    speak("Closing")


        elif 'close' in query:
           pyautogui.hotkey('alt', 'f4') 
           speak("Closing")



        elif 'open camera' in query:
            code_path ="microsoft.windows.camera:"
            os.startfile(code_path)
   

        elif 'open calculator' in query:
            code_path ="calc"
            os.startfile(code_path)



        elif 'open c ' in query:
            code_path ="C:\\"
            os.startfile(code_path)

        elif 'open outlook' in query:
            code_path ="C:\\Users\\shrikrushna\\OneDrive"
            os.startfile(code_path)

        elif 'open d folder' in query:
            code_path ="D:\\"
            os.startfile(code_path)

        elif 'close d folder' in query or 'clothes d drive' in query:
            pyautogui.hotkey('alt', 'f4') 
            speak("Closing d folder")

        elif 'open d ' in query:
            code_path ="D:\\"
            os.startfile(code_path)

        elif 'open python codes ' in query:
            code_path ="D:\\python codes"
            os.startfile(code_path)

        elif 'open desktop' in query:
            code_path ="C:\\Users\\shrikrushna\\Desktop"
            os.startfile(code_path)

        elif 'open download ' in query:
            code_path ="C:\\Users\\shrikrushna\\Downloads"
            os.startfile(code_path)

        elif 'open downloads ' in query:
            code_path ="C:\\Users\\shrikrushna\\Downloads"
            os.startfile(code_path)

        elif 'open images ' in query:
            code_path ="C:\\Users\\shrikrushna\\Pictures"
            os.startfile(code_path)

        elif 'open screenshot' in query:
            code_path ="C:\\Users\\shrikrushna\\Pictures\\Screenshots"
            os.startfile(code_path)

        elif 'open picture ' in query:
            code_path ="C:\\Users\\shrikrushna\\Pictures"
            os.startfile(code_path)

        elif 'open files' in query:
            code_path ="C:\\Users\\shrikrushna"
            os.startfile(code_path)

        elif 'open calendar' in query:
            open_calendar()

        elif 'open file ' in query:
            code_path ="C:\\Users\\shrikrushna"
            os.startfile(code_path)
        
        elif 'open pictures ' in query:
            code_path ="C:\\Users\\shrikrushna\\Pictures"
            os.startfile(code_path)

        elif 'open program files ' in query:
            code_path ="C:\\Program Files"
            os.startfile(code_path)

        elif 'open photos ' in query:
            code_path ="C:\\Users\\shrikrushna\\Pictures"
            os.startfile(code_path)

        elif 'open image ' in query:
            code_path ="C:\\Users\\shrikrushna\\Pictures"
            os.startfile(code_path)

        elif 'open videos' in query:
            code_path ="C:\\Users\\shrikrushna\\Videos"
            os.startfile(code_path)

        elif 'open video' in query:
            code_path ="C:\\Users\\shrikrushna\\Videos"
            os.startfile(code_path)

        elif 'open documents' in query:
            code_path ="C:\\Users\\shrikrushna\\Documents"
            os.startfile(code_path)

        elif 'open document' in query:
            code_path ="C:\\Users\\shrikrushna\\Documents"
            os.startfile(code_path)

        elif 'open music' in query:
            code_path ="C:\\Users\\shrikrushna\\Music"
            os.startfile(code_path)

        elif 'open song' in query:
            code_path ="C:\\Users\\shrikrushna\\Music"
            os.startfile(code_path)

        elif "score" in query or 'IPL' in query or 'ipl' in query:
            score()

        elif "news" in query:
            news()

        elif "thank you" in query:
            print("Its my pleasure to surve you information. so sir can u tell me how may i help you")
            speak("Its my pleasure to surve you information. so sir can u tell me how may i help you")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shailu.patil2004@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend shailu bhai. I am not able to send this email") 

        elif 'stop' in query:
            speak("sure sir and bye!")
            print("sure sir and bye!")
            break

        # else:
        #     print("I am really sorry sir ,The command you said does not match to any information in my datacenter")
        #     speak("I am really sorry sir ,The command you said does not match to any information in my datacenter")

             


