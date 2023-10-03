import speech_recognition as sr

def record_and_transcribe_voice() -> str:
    """
    Record voice input from the user, transcribe it, and return the transcribed text.

    Returns:
        str: The transcribed text.
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as microphone:
        recognizer.adjust_for_ambient_noise(microphone)
        
        print("Escuchando... Por favor, habla.")
        audio = recognizer.listen(microphone)
        
        try:
            transcribed_text = recognizer.recognize_google(audio, language="es-ES")
            return transcribed_text
        except sr.UnknownValueError:
            return "No se entendió lo que dijiste"
        except sr.RequestError as e:
            return f"Error al realizar la solicitud de reconocimiento de voz: {e}"

if __name__ == "__main__":
    transcribed_phrase = record_and_transcribe_voice()
    
    with open('you_said_this.txt', 'w', encoding='utf-8') as file:
        file.write(transcribed_phrase)
        
    print("La última oración que dijiste se ha guardado en you_said_this.txt")

