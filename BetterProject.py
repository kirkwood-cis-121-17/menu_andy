#I made a second project that's a bit more technical and stuff. Why? Because I can.

import random
import sys
import math

def start():
        choice = get_angle()
        move(choice)
                

def get_angle():
        proceed = False
        while proceed == False:
                choice = input()
                if choice == "random":
                        choice = random.randint(0,360)
                        print("Your random angle is", choice, ".")
                        proceed = True
                        return choice
                else:
                        try:
                                choice = int(choice)
                                while choice >= 360:
                                        choice = choice - 360
                                while choice < 0:
                                        choice = choice + 360
                                proceed = True
                                return choice
                        except ValueError:
                                choice = 0
                                print("You need to input a number or 'random.'")
                                print("Input an angle or 'random': ",end="")
                                
def get_distance(angle):
        proceed = False
        while proceed == False:
                try:
                        distance = int(input("Input distance moved: "))
                        proceed = True
                except ValueError:
                        print("You need to input an integer.")
        radians = math.radians(angle)
        distanceX = float(distance) * math.cos(radians)
        distanceY = float(distance) * math.sin(radians)
        return distanceX,distanceY
        
def move(choice):
        angle = choice
        enrage = 0
        positionX = 0
        positionY = 0
        reset = False
        while reset != True:
                print("Choose an option:")
                print("1) Turn")
                print("2) Walk")
                print("3) Get position")
                print("4) Start over")
                print("5) Quit")
                choice = input("Make your choice: ")
                if choice == "1":
                        print("Input an amount of degrees to turn or type 'random': ",end="")
                        add_angle = get_angle()
                        angle = angle + add_angle
                        while angle >= 360:
                                angle = angle - 360
                        while angle < 0:
                                angle = angle + 360
                        print("Your angle is now",angle,"degrees.")
                elif choice == "2":
                        distanceX,distanceY = get_distance(angle)
                        positionX,positionY = positionX+distanceX,positionY+distanceY
                        print("Your coordinates are (",positionX,",",positionY,").")
                elif choice == "3":
                        print("Your coordinates are (",positionX,",",positionY,").")
                        print("Your angle is",angle,"degrees.")
                        print("Your distance from the origin is",math.sqrt(positionX**2 + positionY**2))
                elif choice == "4":
                        reset = True
                elif choice == "5":
                        sys.exit()
                else:
                        enrage = enrage + 1
                        pepe_the_frog(enrage)
                        
def pepe_the_frog(enrage):
        if enrage < 3:
                print("Enter a number from 1 to 5.")
        elif enrage >= 3 and enrage < 5:
                print("I said ENTER A NUMBER FROM 1 TO 5.")
        elif enrage >=5 and enrage < 10:
                print("YOU INCOMPETENT @%#$ ENTER A NUMBER FROM 1 TO 5!")
        else:
                print("RRRRRRREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        start()
        
start()