# importing python modules
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from datetime import date
import webbrowser
from time import sleep
import smtplib
from email.message import EmailMessage
import pyjokes
from googletrans import Translator
import os

# calling functions from speech reconition and assigning it to a variable
recognizer = sr.Recognizer()
microphone = sr.Microphone()

engine = pyttsx3.init()  # initializing the text to speech function
# prepare the email list of your friends so that it could be used later
Email_list = {'college': 'email id', 'friend 1': 'email id', 'dad': 'email id'}


# defining the functions
def take_command():
    # from speech recognition module
    with microphone as source:
        print("Listening...")
        speak("Listening")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        recognizer.adjust_for_ambient_noise(source)
        print("Recognizing...")
        speak("Recognizing")
        try:
            # Taking the command from the user
            command = recognizer.recognize_google(audio, language='en-in')
            print('User said:' + command)
        except Exception as e:
            # If the assistant cannot recognize the voice it will execute this
            speak('Sorry unable to recognize your voice please try again')
            return "None"
        return command


def take_ta():
    with microphone as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        recognizer.adjust_for_ambient_noise(source)
        print("Recognizing...")
        try:
            # Taking command from user in language tamil here , you can mention any language by mentioned by the google
            command = recognizer.recognize_google(audio, language='ta')
            print('User said:' + command)
        except Exception as e:
            speak('Sorry unable to recognize your voice please try again')
            return "None"
        return command.lower()


def wish_me():
    # from module datetime
    hour = int(datetime.datetime.now().hour)  # take time as int
    # Making assistant to wish me according to the time
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour <= 15:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")

    time = datetime.datetime.now().strftime('%I:%M %p')  # Assistant tells time in A.M. or P.M.
    speak(time)
    print(time)
    speak("Now what can i help you sir")


# defining an important function so that the assistant can take command and deliver the speech by Text to speech package pyttsx3
def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 169)  # assigning the assistant speed of speech


# Defining send email function
def send_email(receiver, subject, content):
    # using SMTP server we are send our email
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Which is the server for gmail.com
    server.ehlo()  # its like a identifer which identifies the another server who we have to send with our server
    server.starttls()  # to start the server
    server.login('your email id', 'password')  # login your email with id and password
    email = EmailMessage() # EmailMessage module we calling EmailMessage to send our email in definite email structure
    email['From'] = 'your email id'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


# This method is to translate words or sentence to tamil
def translate_to_tamil(command):
    p = Translator()  # Translator method from googletrans module
    k = p.translate(command, dest='ta')  # Here you can mention any language given by google translator
    translated = str(k.text)
    print(translated)
    speak("Sorry i don't know to speak tamil as of now , but i can understand")


# This method is to translate words or sentence to english from tamil
def translate_to_english(command):
    s = Translator()  # Translator method from googletrans library
    p = s.translate(command, dest='en')  # Here i am mentioning en because i am translating to english
    translate = str(p.text)
    print(translate)
    speak(translate)


# Starting the main method the program always starts or runs the main method first
if __name__ == '__main__':
    wish_me()  # calling wish_me() method so that my assistant wish me at starting
    # Starting while loop so that the assistant take or listen our command continuosly until we stop
    while True:
        command = take_command().lower()  # calling take_command() method in lowercase so that the assistant take our command will be in lower case
        if 'play in youtube' in command:
            video = command.replace('play in youtube', '')  # replacing the word play in youtube from our command
            speak('playing' + video + 'in youtube')
            print('playing' + video)
            pywhatkit.playonyt(
                video)  # from the library pywhatkit we calling the playonyt method will play video from youtube

        elif ' in wikipedia' in command:
            try:
                speak('Searching wikipedia...')
                person = command.replace('in wikipedia', '')
                print(person)
                result = wikipedia.summary(person,2)  # from wikipedia library it will search and say what we want, mention the lines do you want to say by the assistant
                speak("According to wikipedia")
                print(result)
                speak(result)
            except:
                speak('Sorry,Not found in wikipedia')
                pass

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')  # from datetime library
            print(time)
            speak('Current time is ' + time)

        elif 'date' in command:
            today = date.today()  # from datetime library we are calling date class
            d = today.strftime('%B %d, %Y %A')  # from date class we are calling strftime method()
            print(d)
            speak('Today the date is' + d)
        # To open websites we can use webbrowser module by calling open new tab method and passing the website url of what we want as a parameter
        elif 'open google' in command:
            webbrowser.open_new_tab("http://www.google.com")
            speak("Google chrome is opening now")
            sleep(5.0)

        elif 'open youtube' in command:
            webbrowser.open_new_tab("http://www.youtube.com")
            speak('youtube is opening now')
            sleep(5.0)


        elif 'open gmail' in command:
            webbrowser.open_new_tab("http://www.gmail.com")
            speak('gmail is opening now')
            sleep(5.0)

        elif 'google search' in command:
            command = command.replace('google search', '')
            speak('Opening now on google chrome for what' + command + 'you searched')
            webbrowser.open_new_tab("https://www.google.com/search?q=" + command + "")

        elif 'open wikipedia' in command:
            speak('opening wikipedia')
            webbrowser.open_new_tab("http://www.wikipedia.com")

        elif 'gmail' in command or 'email' in command or 'send mail' in command:
            try:
                speak('To whom i want to send sir')
                speak("Tell from the email contacts you have mentioned")
                name = take_command().lower()  # calling take_command so that assistant can take our command
                receiver = Email_list[name]
                speak('what is the subject of your email')
                subject = take_command().lower()
                speak('tell me what should i want to send')
                content = take_command().lower()
                speak('Check the message sir')
                print(content)
                command = take_command().lower()
                if 'yes' in command:  # if the message we want to send is correct
                    speak('Your message will be sent')
                    send_email(receiver, subject, content)
                    speak('Your email has been sent to' + name)
                else:  # if the message we want to send is incorrect, so we have to type the message
                    speak('Type your message here sir because sometimes i cant understand what you have said')
                    subject = input()
                    msg = input()
                    send_email(receiver, subject, msg)
                    speak('Your email has been sent to' + name)

            except:  # if any error occurs this block will execute
                speak('Sorry could not send your email')
                pass

        elif 'search' in command:
            import wikipedia as googleScrap  # importing wikipedia module and named as googleScrap

            command = command.replace('search', '')
            speak('This is what i found')
            pywhatkit.search(command)  # from pywhatkit module calling the search method
            # Assistant will Scrap data from the website and can speak about it for 3 lines
            try:
                answer = googleScrap.summary(command, 3)
                speak(answer)

            except:  # if there is an unspeakable data in website this block will execute
                speak("Sorry there is no speakable data")
                pass
        #  opening instagram website using webbrowser module
        elif 'open instagram' in command:
            speak('opening instagram')
            webbrowser.open_new_tab("https://www.instagram.com")
            sleep(20.0)
            speak('I think you are enjoying memes, so i will leave this with you')
            speak('I will be back in five minutes because you need not waste your time there')
            sleep(300.0)
            speak('i am back sir tell me what i want to do')
        # assistant will tell us jokes when we are bored by using pyjokes module
        elif 'joke' in command or 'i am bored' in command:
            joke = pyjokes.get_joke()  # calling get_joke method from pyjokes module
            print(joke)
            speak(joke)
            speak('Do you like my joke can i continue sir')
            command = take_command().lower()
            try:
                if "yes" in command or "ok" in command or 'continue' in command:
                    speak(" Ok sir, Press 5 to stop me")
                    while True:
                        print("Enter any:")
                        a = int(input())
                        if a == 5:
                            speak("Ok sir i will continue my joke next time now tell me what can i do")
                            break
                        else:
                            joke = pyjokes.get_joke()
                            print(joke)
                            speak(joke)
                            pass

                elif 'no' in command or "don't want" in command or 'stop' in command:
                    speak('Ok sir tell me now what i can do')
            except:
                speak("Sorry for the inconvience now tell me what can i do")

        # Opening facebook using webbrowser module
        elif 'open facebook' in command:
            speak('opening facebook')
            webbrowser.open_new_tab("http://www.facebook.com")

        # opening the softwares in our pc using os module while calling startfile()method passing the softwares or applications paths in your pc
        elif 'open pycharm projects' in command:
            speak('Opening Pycharm projects')
            os.startfile("C:\\Users\\DELL\\PycharmProjects")

        elif 'open telegram' in command:
            speak('Opening telegram')
            os.startfile("C:\\Users\\DELL\\Desktop\\Telegram.lnk")

        elif 'open whatsapp' in command:
            speak('Opening whatsapp')
            os.startfile("C:\\Users\\DELL\\Desktop\\WhatsApp.lnk")

        elif 'open WPS pdf' in command:
            speak('Opening WPS')
            os.startfile("C:\\Users\\DELL\\Desktop\\WPS PDF.lnk")



        elif 'translate in tamil' in command:
            speak('Tell your sentence to translate')
            command = take_command().lower()
            translate_to_tamil(
                command)  # calling translate_to_tamil()function by passing our english sentence or word as a command

        elif 'translate in english' in command:
            speak('Tell your sentence to translate')
            command = take_ta()  # assistant will take tamil language from user as a command so calling take_ta()
            translate_to_english(
                command)  # calling translate_to_english()function by passing our tamil sentence or word as a command

        # I mentioned this because i did'nt program my assistant to translate in other languages except english and tamil if u want to translate in other languages you can mention the language code given by google translate
        elif 'translate in' in command:
            speak("Do you know that language if yes its ok keep it with you or search in google you lazy")

        # If you want to stop the assistant from taking command for a while
        elif "don't listen" in command or "stop listening" in command or "do not listen" in command or 'sleep' in command:
            try:
                speak('for how many seconds do you want me to sleep')
                sec = int(take_command())
                speak('ok sir got it')
                sleep(sec)  # using time module we calling sleep method
                speak(str(sec) + 'seconds completed now you can ask me anything')
            except:  # if any error occurs while taking command as a integer this block will execute
                speak('Tell in seconds or check your mic and speak again')
                speak('for how many seconds do you want me to sleep')
                sec = int(take_command())
                speak('ok sir got it')
                sleep(sec)
                speak(str(sec) + 'seconds completed now you can ask me anything')
                pass
        #  Certain words that we use to our assistant are programmed here u can add more to it
        elif 'hello' in command or 'hi' in command or 'good morning' in command or 'good afternoon' in command or 'good evening' in command:
            speak('Hello sir i am desperate to help you tell me how can i help you sir')

        elif 'thanks' in command or 'good job' in command or 'ok fine' in command:
            speak("That's my pleasure sir")

        elif 'describe about yourself' in command or 'who are you' in command or 'tell me about yourself' in command:
            speak("I am julie personal ai assistant created by sharath")
            speak(
                "I can search any thing you want, i can play any videos and songs, i can open any softwares, i can send emails and lots of things that you command")

        # Using exit() if we command exit the assistant will close the program
        elif 'exit' in command or 'bye julie' in command or 'close' in command or 'stop' in command:
            speak('Closing now and i am waiting for you to comeback sir....byeee')
            exit()
