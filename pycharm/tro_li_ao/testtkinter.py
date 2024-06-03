import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)
    print("You said:")
    try:
        you = robot_ear.recognize_google(audio)
        print(you)
    except:
        you = ""


    print("Robot: "+robot_brain)

    if you == "":
        robot_brain = "I can'n hear you,try again"
    elif you == "Hello":
        robot_brain = "Hello bạn"
    elif you == "today":
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")

    else:
        robot_brain = "I don't understand you""'"

print("Robot: "+robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()













