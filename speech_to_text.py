import speech_recognition as sr

from pydub import AudioSegment

recognizer = sr.Recognizer()  # sets the recognizer to a variable
recognizer.energy_threshold = 300  # sets the threshold in what I believe is decibles
mic = sr.Microphone()


def return_voice():
    with mic as source:
        print("Say something\n")
        recognizer.adjust_for_ambient_noise(source)  # adjust for noise
        print("ready to record\n")
        audio = recognizer.listen(source)  # listens to the person talking
        print("audio captured\n")
        try:
            text = recognizer.recognize_google(audio)  # sets the outcome to a variable to print
        except sr.UnknownValueError:  # incase we get an error
            print("could not understand")
        except sr.RequestError:
            print("could not understand")  # incase we get an error
        return text
