import sys
import random, pywhatkit, pyttsx3, datetime, sys, time, os, pyautogui, requests, wikipedia, pyjokes
from PyQt5.QtCore import QThread
import speech_recognition as sr
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import random
import sys
import time
import os
import os.path
import requests
import cv2  # pip install opencv-python
from requests import get  # pip install requests
# import pywhatkit as kit     #pip install opencv-python
import smtplib  # pip install secure-smtplib
import pyjokes  # pip install pyjokes
import pyautogui  # pip install pyautogui
# import PyPDF2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# import instaloader  # pip install instaloader
import operator  # for calculation using voice
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
# from jarvisUi import Ui_jarvisUi


from jarvisMainGUI import Ui_JarvisMainGUI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    ui.updateMovieDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


def wishings():
    ui.updateMovieDynamically("speaking")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        ui.terminalPrint("Jarvis: Good Morning BOSS")
        speak("Good Morning BOSS")
    elif hour >= 12 and hour < 17:
        ui.terminalPrint("Jarvis: Good Afternoon BOSS")
        speak("Good Afternoon BOSS")
    elif hour >= 17 and hour < 21:
        ui.terminalPrint("Jarvis: Good Evening BOSS")
        speak("Good Evening BOSS")
    else:
        ui.terminalPrint("Jarvis: Good Night BOSS")
        speak("Good Night BOSS")


class jarvisMainClass(QThread):
    def __init__(self):
        super(jarvisMainClass, self).__init__()

    def run(self):
        self.runJarvis()

    def takecommand(self):
        ui.updateMovieDynamically("listening")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            ui.updateMovieDynamically("loading")
            ui.terminalPrint("Recogninszing")
            cmd = r.recognize_google(audio, language='en-in')
            ui.terminalPrint(f"You just said: {cmd}\n")
    
        except Exception as e:
            # ui.terminalPrint(e)
            speak("Please tell me again")
            cmd = "none"
        return cmd
    
    def runJarvis(self):
        self.TaskExecution
        # wishings()
        # while True:
        #     self.query = self.commands()
        #     self.query.lower()
        #     if 'time' in self.query:
        #         strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #         speak(f"Sir, the time is {strTime}")

        #     elif 'open firefox' in self.query:
        #         speak("Opening Firefox Application sir...")
        #         os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        #     elif "wikipedia" in self.query:
        #         speak("Searching in Wikipedia")
        #         try:
        #             self.query = self.query.replace("wikipedia", "")
        #             results = wikipedia.summary(self.query, sentences=1)
        #             speak("According to Wikipedia,")
        #             ui.terminalPrint(results)
        #             speak(results)
        #         except:
        #             speak("No Results found Sir...")
        #             ui.terminalPrint("No results Found")

        #     elif 'play' in self.query:
        #         self.query = self.query.replace('play', '')
        #         speak('Playing' + self.query)
        #         pywhatkit.playonyt(self.query)

        #     elif 'type' in self.query:
        #         speak("Please tell me what should i write")
        #         while True:
        #             writeInNotepad = self.commands()
        #             if writeInNotepad == 'exit typing':
        #                 speak("Done sir")
        #             else:
        #                 pyautogui.write(writeInNotepad)

        #     elif 'joke' in self.query:
        #         joke = pyjokes.get_joke()
        #         ui.terminalPrint(joke)
        #         speak(joke)
        #     elif 'hi' in self.query:
        #         # joke = pyjokes.get_joke()
        #         # ui.terminalPrint(joke)
        #         speak("hi")

        #     elif 'exit program' in self.query:
        #         speak("I'm Leaving Sir, BYE!")
        #         quit()
    @property
    def TaskExecution(self) :
        wishings()
        while True :
            self.query = self.takecommand().lower()

            # logic building for tasks

            if "open notepad" in self.query :
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in self.query :
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query :
                os.system("start cmd")

            elif "open camera" in self.query :
                cap = cv2.VideoCapture(0)
                while True :
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(5)
                    if k == 2 :
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query :
                music_dir = "d:\\songs"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs :
                    if song.endswith('.mp3') :
                        os.startfile(os.path.join(music_dir, song))



            elif "ip address" in self.query :
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query :
                speak("searching wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query :
                speak("Akshali, what should i search on youtube")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")


            elif "open facebook" in self.query :
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query :
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query :
                speak("Akshali, what should i search on google")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")

                # url = "https://www.google.co.in/search?q=vr"
                # webbrowser.open(url)

            # elif "send whatsapp message" in self.query:
            #     kit.sendwhatmsg("+91 user_number", "your_message",4,13)
            #     time.sleep(120)
            #     speak("message has been sent")

            # elif "song on youtube" in self.query:
            #     kit.playonyt("see you again")

            # elif "email to vijay" in self.query:
            #     try:
            #         speak("what should i say?")
            #         content = takecommand()
            #         to = "EMAIL OF THE OTHER PERSON"
            #         sendEmail(to,content)
            #         speak("Email has been sent to user")

            #     except Exception as e:
            #         print(e)
            #         speak("sorry vijay, i am not able to sent this mail to user")

            elif "you can sleep now" in self.query or "sleep now" in self.query :
                speak("okay Akshali, i am going to sleep you can call me anytime.")
                sys.exit()
                gifThread.exit()
                # break



            # to close any application
            elif "close notepad" in self.query :
                speak("okay Akshali, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            # to set an alarm
            elif "set alarm" in self.query :
                nn = int(datetime.datetime.now().hour)
                if nn == 22 :
                    music_dir = 'd:\\song'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
            # to find a joke
            elif "tell me a joke" in self.query :
                joke = pyjokes.get_joke()
                speak(joke)

            # elif "shut down the system" in self.query:
            #     os.system("shutdown /s /t 5")

            # elif "restart the system" in self.query:
            #     os.system("shutdown /r /t 5")

            # elif "sleep the system" in self.query:
            #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "hello" in self.query or "hey" in self.query :
                speak("hello Akshali, may i help you with something.")

            elif "how are you" in self.query :
                speak("i am fine Akshali, what about you.")

            elif "wake up" in self.query :
                speak("Akshali, let me sleep ten minutes more, i will be there.")

            elif "thank you" in self.query or "thanks" in self.query :
                speak("it's my pleasure Akshali.")

            ###################################################################################################################################
            ###########################################################################################################################################

            elif 'switch the window' in self.query :
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")


            elif "tell me news" in self.query :
                speak("please wait Akshali, feteching the latest news")
                news()


            elif "email to Akshali" in self.query :

                speak("Akshali what should i say")
                self.query = self.takecommand()
                if "send a file" in self.query :
                    # email = 'vijaysonisir1@gmail.com'  # Your email
                    # password = 'aadarsh1vidhya@'  # Your email account password
                    send_to_email = 'jainakshali18@gmail.com'  # Whom you are sending the message to
                    speak("okay Akshali, what is the subject for this email")
                    self.query = self.takecommand()
                    subject = self.query  # The Subject in the email
                    speak("and Akshali, what is the message for this email")
                    self.query2 = self.takecommand()
                    message = self.query2  # The message in the email
                    speak("Akshali please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")  # The File attachment in the email

                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    # Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to user")

                else :
                    # email = 'your@gmail.com'  # Your email
                    # password = 'your_pass@123'  # Your email account password
                    send_to_email = 'jainakshali18@gmail.com'  # Whom you are sending the message to
                    message = self.query  # The message in the email

                    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
                    server.starttls()  # Use TLS
                    server.login(email, password)  # Login to the email server
                    server.sendmail(email, send_to_email, message)  # Send the email
                    server.quit()  # Logout of the email server
                    speak("email has been sent to Akshali!")


            ##########################################################################################################################################
            ###########################################################################################################################################

            elif "do some calculations" in self.query or "can you calculate" in self.query :
                r = sr.Recognizer()
                with sr.Microphone() as source :
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op) :
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                    }[op]

                def eval_binary_expr(op1, oper, op2) :
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                print(eval_binary_expr(*(my_string.split())))


            # -----------------To find my location using IP Address

            elif "where am i" in self.query or "where we are" in self.query :
                speak("wait Akshali, let me check")
                try :
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"Akshali i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e :
                    speak("sorry Akshali, Due to network issue i am not able to find where we are.")
                    pass

            # -------------------To check a instagram profile----
            elif "instagram profile" in self.query or "profile on instagram" in self.query :
                speak("Akshali please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Akshali here is the profile of the user {name}")
                time.sleep(5)
                speak("Akshali would you like to download profile picture of this account.")
                condition = takecommand()
                if "yes" in condition :
                    mod = instaloader.Instaloader()  # pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done Akshali, profile picture is saved in our main folder. now i am ready for next command")
                else :
                    pass

            # -------------------  To take screenshot -------------
            elif "take screenshot" in self.query or "take a screenshot" in self.query :
                speak("Akshali, please tell me the name for this screenshot file")
                sname = self.takecommand()
                print(sname)
                speak("please Akshali hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"d:/{sname}.png")
                speak("i am done Akshali, the screenshot is saved in our main folder. now i am ready for next command")


            # speak("vijay, do you have any other work")

            # -------------------  To Read PDF file -------------
            # elif "read pdf" in self.query :
            #     pdf_reader()

            # --------------------- To Hide files and folder ---------------
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query :
                speak("Akshali please tell me you want to hide this folder or make it visible for everyone")
                condition = takecommand()
                if "hide" in condition :
                    os.system("attrib +h /s /d")  # os module
                    speak("Akshali, all the files in this folder are now hidden.")

                elif "visible" in condition :
                    os.system("attrib -h /s /d")
                    speak(
                        "Akshali, all the files in this folder are now visible to everyone. i wish you are taking this decision in your own peace.")

                elif "leave it" in condition or "leave for now" in condition :
                    speak("Ok Akshali")


startExecution = jarvisMainClass()


class Ui_JARVIS(QMainWindow):
    def __init__(self):
        super(Ui_JARVIS, self).__init__()
        self.jarvisUI = Ui_JarvisMainGUI()
        self.jarvisUI.setupUi(self)

        self.jarvisUI.exitButton.clicked.connect(self.close)
        # self.jarvisUI.enterButton.clicked.connect(self.manualCodeFromTerminal)
        self.runAllMovies()

    def manualCodeFromTerminal(self):
        if self.jarvisUI.terminalInputBox.text():
            cmd = self.jarvisUI.terminalInputBox.text()
            self.jarvisUI.terminalInputBox.clear()
            self.jarvisUI.terminalOutputBox.appendPlainText(f"You typed-> {cmd}")

            if cmd == 'exit':
                ui.close()
            elif cmd == 'help':
                self.terminalPrint("I can perform various tasks which is programmed inside me by KARTIS sir.\n"
                                   "Examples are: Time, Wikipedia, Play music, minimize/maximize/close windows, open any system applications,"
                                   " Google search, screenshot, Joke, Play YouTube video, type anything you say, Sleep well or else i'll chit chat")

            else:
                pass

    def terminalPrint(self, text):
        self.jarvisUI.terminalOutputBox.appendPlainText(text)

    def updateMovieDynamically(self, state):
        if state == "speaking":
            self.jarvisUI.jarvisSpeakingLabel.raise_()
            self.jarvisUI.jarvisSpeakingLabel.show()
            self.jarvisUI.listeningLabel.hide()
            self.jarvisUI.loadingLabel.hide()
        elif state == "listening":
            self.jarvisUI.listeningLabel.raise_()
            self.jarvisUI.listeningLabel.show()
            self.jarvisUI.jarvisSpeakingLabel.hide()
            self.jarvisUI.loadingLabel.hide()
        # elif state == "loading":
        #     self.jarvisUI.loadingLabel.raise_()
        #     self.jarvisUI.loadingLabel.show()
        #     self.jarvisUI.jarvisSpeakingLabel.hide()
        #     self.jarvisUI.listeningLabel.hide()

    def runAllMovies(self):
        # self.jarvisUI.codingMovie = QtGui.QMovie("E:\\CODING\\Artificial_Intelligence\\Ultimate JARVIS with GUI YT  Playlist files\\gui_tools\\B.G_Template_1.gif")
        # self.jarvisUI.codingLabel.setMovie(self.jarvisUI.codingMovie)
        # self.jarvisUI.codingMovie.start()

        self.jarvisUI.listeningMovie = QtGui.QMovie(
            "mj_static.gif")
        self.jarvisUI.listeningLabel.setMovie(self.jarvisUI.listeningMovie)
        self.jarvisUI.listeningMovie.start()

        self.jarvisUI.speakingMovie = QtGui.QMovie(
            "mj.gif")
        self.jarvisUI.jarvisSpeakingLabel.setMovie(self.jarvisUI.speakingMovie)
        self.jarvisUI.speakingMovie.start()

        # self.jarvisUI.arcMovie = QtGui.QMovie(
            # "E:\\CODING\\Artificial_Intelligence\\Jarvis with GUI\\gui_tools\\techcircle.gif")
        # self.jarvisUI.arcLabel.setMovie(self.jarvisUI.arcMovie)
        # self.jarvisUI.arcMovie.start()

        # self.jarvisUI.loadingMovie = QtGui.QMovie(
        #     "idle_pia.gif")
        # self.jarvisUI.loadingLabel.setMovie(self.jarvisUI.loadingMovie)
        # self.jarvisUI.loadingMovie.start()

        startExecution.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_JARVIS()
    ui.show()
    sys.exit(app.exec_())
