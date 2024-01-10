# from codrone_edu.drone import *
import speech_recognition as sr
import pyttsx3


# drone = Drone()
r = sr.Recognizer()


# Function to convert text to
# speech
while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ", MyText)
            SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")


# while True:
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak


# def straight_line():
#     drone.pair()
#     drone.takeoff()
#     # Drone goes up for 1 second with 50 power
#     drone.set_pitch(70)
#     drone.avoid_wall(50, 50)
#     drone.set_pitch(-70)
#     drone.turn_degree(180)
#     drone.set_pitch(70)
#     drone.move(4.5)
#
#     drone.land()
#
#     drone.close()
#
#
# def spiral():
#     drone.pair()
#     drone.takeoff()
#     # default spiral parameters (50, 5, 1)
#     drone.spiral(20, 5, 1)
#     drone.land()
#     drone.close()
#
# def figure_8():
#     drone.pair()
#     drone.takeoff()
#     drone.set_yaw(50)
#     drone.set_pitch(70)
#     drone.move(1.5)
#     drone.set_yaw(-100)
#     drone.move(3)
#     drone.set_yaw(100)
#     drone.move(2)
#     drone.set_yaw(50)
#     drone.move(1.5)
#     drone.set_yaw(-100)
#     drone.move(3)
#     drone.set_yaw(100)
#     drone.move(2)
#     drone.land()
#     drone.close()
#
#
# def loop():
#     drone.pair()
#     drone.takeoff()
#     # Drone goes up for 1 second with 50 power
#     drone.set_throttle(50)
#     drone.set_pitch(50)
#     drone.move(1.5)  # move command executes the movement for 1 second
#     drone.set_throttle(-50)
#     drone.set_pitch(-100)
#     drone.move(1.5)
#     drone.land()
#
#     drone.close()
#     user_input = input("What would you like to do?")
    # if user_input == "Figure 8":
    #     figure_8()
    # elif user_input == "Straight line":
    #     straight_line()
    # elif user_input == "Loop":
    #     loop()
    # elif user_input == "Spiral":
    #     spiral()

