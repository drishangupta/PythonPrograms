import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()
with sr.Microphone() as source2:
			
			r.adjust_for_ambient_noise(source2, duration=0.2)
            
			print("Please say something")
			
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			

			print("Did you say, ",MyText)