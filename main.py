import speech_recognition


def record_voice():
    microphone = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        
        print ("I'm triying to hear you: ...")
        audio = microphone.listen(live_phone)
        
        try:
            
            phrase = microphone.recognize_google(laudio, language="es-ES")
            return phrase
        
        except speech_recognition.UnknownValueError:
            return " I dont understand what you said"
        
    
    if __name__ == "__main__":
        phrase = record_voice()
        with open('you_said_this.txt', 'w') as file:
            file.write(phrase)
            
            print("The last sentence you spoke was saved in you_said_this.txt")