import time

from buildhat import Motor

motor = Motor('A')


def handle_motor(speed, pos, apos):
    """Motor data

    :param speed: Speed of motor
    :param pos: Position of motor
    :param apos: Absolute position of motor
    """
    print("Motor", speed, pos, apos)


motor.when_rotated = handle_motor
motor.set_default_speed(50)

print("Run for degrees 360")
motor.run_for_degrees(360)
time.sleep(3)