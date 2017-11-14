#I made a second project that's a bit more technical and stuff. Why? Because I can.

import random
import sys
import math

def main():
        start()
                
def start():
        print("Input a starting angle or type 'random' for a random angle.")
        choice = input("Make your choice: ")
        try:
                choice = int(choice)
                while choice >= 360:
                        choice = choice - 360
                move(choice)
        except ValueError:
                if choice == "random":
                        choice = random.randint(0,360)
                        print("Your random angle is", choice, ".")
                        move(choice)
                else:
                        print("You need to input a number or 'random.'")
                        start()
                        
def turn():
        choice = input("Input an amount of degrees to turn or type 'random': ")
        try: 
                choice = int(choice)
                while choice > 360:
                        choice = choice - 360
                while choice < 0:
                        choice = choice + 360
                return choice
        except ValueError:
                        if choice == "random":
                                choice = random.randint(0,360)
                                print("Your random angle is ", choice, ".")
                                return choice 
                        else:
                                print("You need to input a number or 'random.'")

def distX(distance,angle):
        if angle >= 0 and angle < 90:
                posNeg = 1
        elif angle <= 270 and angle >= 90:
                posNeg = -1
        elif angle <= 360 and angle > 270:
                posNeg = 1
        elif angle == 90 or angle == 270:
                posNeg = 0
                
        x = float(distance) * math.cos(angle)
        
        return x
        
def distY(distance,angle):
        if angle > 0 and angle < 180:
                posNeg = 1
        elif angle > 180 and angle < 360:
                posNeg = -1
        elif angle == 0 or angle == 180:
                posNeg = 0
        
        y = float(distance) * math.sin(angle) * float(posNeg)
        
        return y
        
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
                        add_angle = turn()
                        angle = angle + add_angle
                        while angle > 360:
                                angle = angle - 360
                        while angle < 0:
                                angle = angle + 360
                        print("Your angle is now",angle,"degrees.")
                elif choice == "2":
                        distance = input("How far will you walk: ")
                        try:
                                int(distance)
                                radians = math.radians(angle)
                                distanceX = float(distance) * math.cos(radians)
                                distanceY = float(distance) * math.sin(radians)
                                positionX = positionX + distanceX
                                positionY = positionY + distanceY
                                print("Your coordinates are (",positionX,",",positionY,").")
                        except ValueError:
                                print("You must input an integer distance.")
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
                        if enrage < 3:
                                print("Enter a number from 1 to 5.")
                        elif enrage >= 3 and enrage < 5:
                                print("I said ENTER A NUMBER FROM 1 TO 5.")
                        elif enrage >=5 and enrage < 10:
                                print("YOU INCOMPETENT @%#$ ENTER A NUMBER FROM 1 TO 5!")
                        else:
                                print("AJHLBNKJSAIJAWADASGTASMLAMAQWUOIEUOAKNBLADUYTAUSHDLASGBALKSJDGASKYHFVHBASJKDBASKJBVASLDYIASFAUWGHALKBHABKLVAJSNXCASUOIGALJKSRJ")
        main()
        
main()