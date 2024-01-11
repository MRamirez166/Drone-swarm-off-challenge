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


# while True:
# user_input = input("What would you like to do?")
# if user_input == "Figure 8":
#     figure_8()
# elif user_input == "Straight line":
#     straight_line()
# elif user_input == "Loop":
#     loop()
# elif user_input == "Spiral":
#     spiral()
distance_difference = 150

drone.pair()
print(drone.get_bottom_range())
bottom_range = drone.get_bottom_range()
print(drone.get_bottom_range())
drone.takeoff()
print(drone.get_bottom_range())
drone.set_throttle(30)
print(drone.get_bottom_range())
if distance_difference == int(bottom_range):
    print(drone.get_bottom_range())
    drone.set_throttle(-30)
    print(drone.get_bottom_range())
drone.land()
print(drone.get_bottom_range())
drone.close()
print(drone.get_bottom_range())
