import pywhatkit as pwk
from datetime import datetime
# using Exception Handling to avoid unexpected errors
time=datetime.now()
timeh=int(time.strftime("%H"))
timem=int(time.strftime("%M"))
uptimem=timem + 1  
print(timeh)
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     pwk.sendwhatmsg("+918905429708", "Hello how are you?",timeh,uptimem)
 
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")