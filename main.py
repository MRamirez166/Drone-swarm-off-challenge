import speech_recognition as sr
from codrone_edu.drone import *
from pydub import AudioSegment

recognizer = sr.Recognizer()  # sets the recognizer to a variable
recognizer.energy_threshold = 300  # sets the threshold in what I believe is decibles
mic = sr.Microphone()

drone = Drone()

recognizer = sr.Recognizer()  # sets the recognizer to a variable
recognizer.energy_threshold = 300  # sets the threshold in what I believe is decibles
mic = sr.Microphone()
drone.pair()


def straight_line():
    # Drone goes up for 1 second with 50 power
    drone.set_pitch(70)
    drone.avoid_wall(50, 50)
    drone.set_pitch(-70)
    drone.turn_degree(180)
    drone.set_pitch(70)
    drone.move(4.5)




def spiral():
    # default spiral parameters (50, 5, 1)
    drone.spiral(20, 5, 1)


def figure_8():
    drone.set_yaw(50)
    drone.set_pitch(70)
    drone.move(1.5)
    drone.set_yaw(-100)
    drone.move(3)
    drone.set_yaw(100)
    drone.move(2)
    drone.set_yaw(50)
    drone.move(1.5)
    drone.set_yaw(-100)
    drone.move(3)
    drone.set_yaw(100)
    drone.move(2)


def loop():
    # Drone goes up for 1 second with 50 power
    drone.set_throttle(50)
    drone.set_pitch(50)
    drone.move(1.5)  # move command executes the movement for 1 second
    drone.set_throttle(-50)
    drone.set_pitch(-100)
    drone.move(1.5)


def hover():
    drone.hover(3)


def xcoo():
    drone = Drone()
    print(drone.get_pos_y())


while True:
    with mic as source:
        print("Say something\n")
        recognizer.adjust_for_ambient_noise(source)  # adjust for noise
        print("ready to record\n")
        audio = recognizer.listen(source)  # listens to the person talking
        print("audio captured\n")
        try:
            audio_captured = recognizer.recognize_google(audio)  # sets the outcome to a variable to print
            print(audio_captured)
            if audio_captured.upper() == "FIGURE 8":
                figure_8()
            elif audio_captured.upper() == "STRAIGHT LINE":
                straight_line()
            elif audio_captured.upper() == "LOOP":
                loop()
            elif audio_captured.upper() == "SPIRAL":
                spiral()
            elif audio_captured.upper() == "HOVER":
                hover()
            elif audio_captured.upper() == "xcoo":
                xcoo()
            elif audio_captured.upper() == "TAKE OFF":
                drone.takeoff()
            elif audio_captured.upper() == "LAND":
                drone.land()
            elif audio_captured.upper() == "STOP":
                drone.close()
        except sr.UnknownValueError:  # incase we get an error
            pass
        except sr.RequestError:
            pass  # incase we get an error

