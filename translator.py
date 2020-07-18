import pyttsx3
from googletrans import Translator

result=input("write a text you want to convert : ")
s=Translator()
print(result)
ch=input("in which language you want to convert: ")
k=s.translate(result,dest=ch)
print(k)
engine=pyttsx3.init()
engine.say(k)
engine.runAndWait()
    
