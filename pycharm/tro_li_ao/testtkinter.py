import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    print("Robot:....")
    try:
        you = robot_ear.recognize_google(audio)
        print("You: "+you)
    except:
        you = ""

    print("Robot: " + robot_brain)

    if you == "":
        robot_brain = "I can'n hear you,try again"
    elif "Hello" in you:
        robot_brain = "Hello bạn"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H:%M:%S")
    elif "bye" in you:
        robot_brain = "Goodbye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I don't understand you""'"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()














