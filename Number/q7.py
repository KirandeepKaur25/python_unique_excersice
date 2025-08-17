'''Write a program that asks the user to enter an angle between −180◦
and 180◦
. Using an
expression with the modulo operator, convert the angle to its equivalent between 0
◦
and
360'''
import math
def normalize_angle(angle):
    '''convert angle to equivalent between 0 and 360 '''
    return angle % 360
user_angle = float (input("enter an angle between -180 and 180:"))
if user_angle <-180 or user_angle >180:
    print("angle must be between -180 and 180")
else: 
    normalized = normalize_angle(user_angle)
    print(f"{user_angle} is equivalent to {normalized} between 0 and 360")
    