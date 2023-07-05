import pyttsx3


engine = pyttsx3.init()


engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)
print("Hey its me robo voice converter devloped by tasavvuf  ")
x = input("enter your text: ")

text = x
engine.say(text)
engine.runAndWait()


