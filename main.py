import speech_recognition as sr
import pyttsx3
import os


def speak(text):
    print("Ассистент: ", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def recognize_command(audio):
    recognizer = sr.Recognizer()
    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        return command.lower()
    except sr.UnknownValueError:
        return "error"
    except sr.RequestError:
        return "error"


def process_command(command):
    if "привет" in command:
        speak("Привет! Чем могу помочь?")
    elif "как дела" in command:
        speak("У меня все отлично, спасибо! А у вас?")
    elif "включи музыку" in command:
        speak("Музыка включается...")
        os.system('2.mp3')
    elif "пока" in command:
        speak("До свидания!")
        exit()
    else:
        speak("Извините, не понял команду")


def main():
    speak("Привет! Я ваш голосовой ассистент.")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5)
            command = recognize_command(audio)
            if command != "error":
                process_command(command)
            else:
                speak("Произошла ошибка при распознавании команды.")
        except KeyboardInterrupt:
            speak("До свидания!")
            break
        except Exception as e:
            speak("Произошла ошибка: " + str(e))


if __name__ == "__main__":
    main()
