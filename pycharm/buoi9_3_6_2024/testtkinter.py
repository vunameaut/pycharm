import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 1 represents a female voice
engine.say("vãi ò")
engine.runAndWait()












