import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female
engine.setProperty('rate', 150)            # speed of speech
engine.say("Hey I am good, how are you?. I am fine.how about you?   What is your name?  My name is Jarvis. I am your personal AI assistant. I am here to help you with your tasks. Let's get started!")
engine.runAndWait()

