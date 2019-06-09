import pyttsx3
import pyaudio  # pyaudio installed through wheel file directly (.whl)
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

nameOfApplication = "David"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
engine.setProperty('rate', 200)     # setting up new voice rate


def speak(audio):
    '''
    The speak functionality of our program.
    '''
    engine.say(audio)
    engine.runAndWait()

def printAndSpeak(content):
    print(content + "..")
    speak(content)

def Greet():
    '''
    Wishes the user
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour <= 11:
        print("Good Morning Sir!")
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 15:
        print("Good Afternoon Sir!")
        speak("Good Afternoon Sir!")
    elif hour >= 16 and hour <= 22:
        print("Good Evening Sir!")
        speak("Good Evening Sir!")
    else:
        print("Hello Sir!")
        speak("Hello Sir!")
    print("This is " + nameOfApplication + ", how may I help you?")
    speak("this is " + nameOfApplication + ", how may I help you?")


def takeCommand():
    '''
    Takes the command from the user.
    '''
    r = sr.Recognizer()

    '''
    With the "With" statement, we get better syntax and exceptions handling.
    In addition, it will automatically close the file. The with statement provides
    a way for ensuring that a clean-up is always used.
    Note that we could have used,
    #source = sr.Microphone()
    '''
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("Recognising..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You asked to: {query} \n")

        except Exception as e:
            '''
            Not printing the error.
            '''
            # print(e)
            print("I didn't quite catch that, could you please repeat?")
            speak("I didn't quite catch that, could you please repeat?")
            return "None"
        return query


def sendEmail(to,content,subject):
    '''
    Sends email, contains SMTP settings, not sure if SMTP still functional
    '''

    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(
    from_addr, to, content)
    server.close()

'''
This function is designed to perform the tasks.
'''


def performTask(query):
    if nameOfApplication in query:
        query = query.replace(nameOfApplication, "")

    if 'wikipedia' in query:
        print("Searching..")
        speak("Searching..")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print("According to wikipedia " + results)
        speak("According to wikipedia " + results)

    elif "what is the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Sir, the time is {strTime}")
        speak(f"Sir, the time is {strTime}")

    elif "what is" in query:
        print("Searching..")
        speak("Searching..")
        query = query.replace("what is", "")
        results = wikipedia.summary(query, sentences=2)
        print("According to wikipedia " + results)
        speak("According to wikipedia " + results)

    elif "open program" in query:
        try:
            query = query.replace("open program ", "")
            file = 'C:\\Users\\MOHIT\\Desktop\\' + query + '.lnk'
            os.startfile(file)
            print("Opening " + query + "..")
            speak("Opening " + query)
        except Exception as error:
            printAndSpeak("I don't think I could find the file Sir.. There might have been some error..")
            print(error)

    elif "open mail" in query:
        print("Opening..")
        speak("opening..")
        webbrowser.open("https://mail.iitp.ac.in")

    elif "open" in query:
        print("Opening..")
        speak("opening..")
        query = query.replace("open ", "")
        webbrowser.open("https://" + query + ".com")

    elif "play favorites" in query:
        print("Playing..")
        speak("Playing..")
        webbrowser.open("https://gaana.com/myfavoritetracks")

    elif "play music on youtube" in query:
        print("Playing..")
        speak("Playing..")
        webbrowser.open(
            "https://www.youtube.com/watch?v=34Na4j8AVgA&list=RD34Na4j8AVgA&start_radio=1&t=3")

    elif "play music" in query:
        musicDirectory = 'E:\\music'
        songs = os.listdir(musicDirectory)
        # print(songs)
        os.startfile(os.path.join(musicDirectory, songs[0]))

    elif "send mail" in query:
        try:
            print("What should it say?")
            speak("What should it say?")
            content = takeCommand()
            print("And what email I.D. should it be addressed to?")
            speak("And what email I.D. should it be addressed to?")
            to = takeCommand()
            print("What should be the subject?")
            speak("What should be the subject?")
            subject = takeCommand()
            sendEmail(to,content,subject)
            print("Your mail has been sent.")
            speak("Your mail has been sent.")

        except Exception as error:
            print(error)
            speak("There has been some error Sir, Please look into this")

    else :
        print("Sir, I don't think I have that functionality yet..")
        speak("Sir, I don't think I have that functionality yet..")

'''
This is the main function which drives the program
'''
if __name__ == '__main__':
    '''
    Manually checked the working of the speak function we have created using pyttsx3.
    # speak("This is working.")
    '''

    '''
    Wishes the user
    '''
    Greet()
    while True:
        query = takeCommand().lower()
        if(query == "mischief managed"):
            print("Shutting down the assistant, thank you Sir!")
            speak("Shutting down the assistant, thank you Sir!")
            break
        performTask(query)

    exit()
