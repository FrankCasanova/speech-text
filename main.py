import speech_recognition as sr

def record_voice():
    microphone = sr.Recognizer()
    with sr.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        
        print("Estoy intentando escucharte...")
        audio = microphone.listen(live_phone)
        
        try:
            phrase = microphone.recognize_google(audio, language="es-ES")
            return phrase
        
        except sr.UnknownValueError:
            return "No entiendo lo que dijiste"
    
if __name__ == "__main__":
    phrase = record_voice()
    with open('you_said_this.txt', 'w', encoding='utf-8') as file:
        file.write(phrase)
        print("La última oración que dijiste se ha guardado en you_said_this.txt")
