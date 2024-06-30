import Jetson.GPIO as GPIO
import time

# Define the GPIO pins connected to the motor driver
# Motor A
ENA = 33  # PWM pin for speed control of motor A
IN1 = 35  # Direction control pin 1 of motor A
IN2 = 37  # Direction control pin 2 of motor A

# Motor B
ENB = 32  # PWM pin for speed control of motor B
IN3 = 36  # Direction control pin 1 of motor B
IN4 = 38  # Direction control pin 2 of motor B

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Set up PWM on the ENA and ENB pins with a frequency of 1 kHz
pwmA = GPIO.PWM(ENA, 1000)
pwmB = GPIO.PWM(ENB, 1000)
pwmA.start(0)  # Start PWM with 0% duty cycle
pwmB.start(0)  # Start PWM with 0% duty cycle

def set_motor_speed(motor, speed):
    """ Function to set motor speed and direction
    Args:
    motor (str): Motor identifier ('A' or 'B')
    speed (int): Speed of the motor (-100 to 100)
    """
    if motor == 'A':
        pwm = pwmA
        INx1 = IN1
        INx2 = IN2
    elif motor == 'B':
        pwm = pwmB
        INx1 = IN3
        INx2 = IN4
    else:
        raise ValueError("Motor should be 'A' or 'B'")

    if speed > 0:
        GPIO.output(INx1, GPIO.HIGH)
        GPIO.output(INx2, GPIO.LOW)
    elif speed < 0:
        GPIO.output(INx1, GPIO.LOW)
        GPIO.output(INx2, GPIO.HIGH)
    else:
        GPIO.output(INx1, GPIO.LOW)
        GPIO.output(INx2, GPIO.LOW)
    
    pwm.ChangeDutyCycle(abs(speed))

def move_forward(speed):
    set_motor_speed('A', speed)
    set_motor_speed('B', speed)

def move_backward(speed):
    set_motor_speed('A', -speed)
    set_motor_speed('B', -speed)

def turn_left(speed):
    set_motor_speed('A', -speed)
    set_motor_speed('B', speed)

def turn_right(speed):
    set_motor_speed('A', speed)
    set_motor_speed('B', -speed)

try:
    speed = 80  # Set the speed to 80
    while True:
        direction = input("Enter direction (w: forward, s: backward, a: left, d: right) or 'stop' to end: ").lower()
        if direction == 'stop':
            break
        
        if direction == 'w':
            move_forward(speed)
        elif direction == 's':
            move_backward(speed)
        elif direction == 'a':
            turn_left(speed)
        elif direction == 'd':
            turn_right(speed)
        else:
            print("Invalid input. Please enter 'w', 'a', 's', or 'd'.")

except KeyboardInterrupt:
    pass

finally:
    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()
