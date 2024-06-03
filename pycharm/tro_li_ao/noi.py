import pyttsx3

robot_brain = "Hello, I am a robot. What is your name?"


robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

