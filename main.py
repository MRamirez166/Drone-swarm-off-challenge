# main.py
# desc: A program for a drone swarm off
# authors: Martin Ramirez, Naimur Abir, Eric Tavarez, Alejandro Bautista, Connor McGonigal
# created: 01/09/2024
from codrone_edu.drone import *

drone = Drone()


def straight_line():
    drone.pair()
    drone.takeoff()
    # Drone goes up for 1 second with 50 power
    drone.set_pitch(70)
    drone.avoid_wall(50, 50)
    drone.set_pitch(-70)
    drone.turn_degree(180)
    drone.set_pitch(70)
    drone.move(4.5)

    drone.land()

    drone.close()


def spiral():
    drone.pair()
    drone.takeoff()
    # default spiral parameters (50, 5, 1)
    drone.spiral(20, 5, 1)
    drone.land()
    drone.close()

def figure_8():
    drone.pair()
    drone.takeoff()
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
    drone.land()
    drone.close()

#SMALLER FIGURE EIGHT
def figure_eight():
    drone.pair()
    drone.takeoff()
    drone.set_yaw(70)
    drone.set_pitch(50)
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
    drone.land()
    drone.close()

def loop():
    drone.pair()
    drone.takeoff()
    # Drone goes up for 1 second with 50 power
    drone.set_throttle(50)
    drone.set_pitch(50)
    drone.move(1.5)  # move command executes the movement for 1 second
    drone.set_throttle(-50)
    drone.set_pitch(-100)
    drone.move(1.5)
    drone.land()
    drone.close()


def hover():
    drone.pair()
    drone.takeoff()
    drone.hover(3)
    drone.land()
    drone.close()

def xcoo():
    drone = Drone()
    drone.pair()
    drone.takeoff()
    print(drone.get_pos_y())
    drone.land()
    drone.close()

while True:
    user_input = input("What would you like to do?")
    if user_input == "Figure 8":
        figure_8()
    elif user_input == "Straight line":
        straight_line()
    elif user_input == "Loop":
        loop()
    elif user_input == "Spiral":
        spiral()
    elif user_input == "Hover":
        hover()
    elif user_input == "xcoo":
        xcoo()
    elif user_input == "eight":
        figure_eight()