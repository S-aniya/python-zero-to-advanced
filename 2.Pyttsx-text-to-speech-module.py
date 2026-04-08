# import pyttsx3
# engine=pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()
import pyttsx3

engine = pyttsx3.init()
engine.save_to_file("Hello Chmkaa 😄", "output.mp3")
engine.runAndWait()