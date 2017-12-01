#I made a second project that's a bit more technical and stuff. Why? Because I can.

import random
import sys
import math

def start():
        print("This program will allow you to calculate your position on a unit plane based on an")
        print("inputted angle and inputted distance traveled. Please enter your starting angle or")
        print("type 'random' to get a random starting angle. Angles above 360 degrees or below 0")
        print("degrees are automatically converted to be between 0 and 359 degrees.")
        print("")
        print("Input an amount of degrees or type 'random': ", end="")
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

def get_Exact(exact_X,exact_Y,angle): #HAHAHAHAHA THIS IS DISGUSTING WHAT AM I EVEN DOING???
        lyst_X = []
        lyst_Y = []
        string = str(angle)
        length = len(string)
        if exact_X == "0" or exact_Y == "0":
                if exact_X == "0":
                        exact_X = "cos("+string+")"
                else:
                        exact_X += "cos("+string+")"
                if exact_Y == "0":
                        exact_Y = "sin("+string+")"
                else:
                        exact_Y += "sin("+string+")"
        else:
                exact_X += " + cos("+string+")"
                exact_Y += " + sin("+string+")"
        
        loops = 0
        exact_X_Length = len(exact_X)
        loops_max_X = round(len(exact_X)/(5 + length))
        while loops != loops_max_X:
                lyst_X.append(int(exact_X[5 + exact_X_Length * loops:(5+length) + exact_X_Length * loops]))
        
        loops = 0
        exact_Y_Length = len(exact_Y)
        loops_max_Y = round(len(exact_Y)/(5 + length))
        while loops != loops_max_Y:
                lyst_Y.append(int(exact_Y[5 + exact_Y_Length * loops:(5+length) + exact_Y_Length * loops]))
        
        big_counter_max = len(lyst_X)
        big_counter = 0
        little_counter_base = 1
        little_counter = 1
        little_counter_max = len(lyst_X)
        
        while big_counter > big_counter_max:
                while little_counter > little_counter_max:
                        base = lyst_X[big_counter]
                        compare = lyst_X[little_counter]
                        if base == compare or base - 180 == compare or base == compare - 180:
                                temp_list=exact_X.split(" + ")
                                del temp_list[big_counter]
                                del temp_list[little_counter]
                                exact_X = " + ".join(temp_list)
                                        
        if exact_X == "":
                exact_X = "0"
        if exact_Y =="":
                exact_Y = "0"
                
        return exact_X,exact_Y
        
def move(choice):
        angle = choice
        enrage = 0
        position_X = 0
        exact_X = "0"
        exact_Y = "0"
        position_Y = 0
        reset = False
        while reset != True:
                go_back = False
                print("Choose an option:")
                print("1) Turn")
                print("2) Move")
                print("3) Get a decimal position")
                print("4) Get an exact position.")
                print("5) Start over")
                print("6) Quit")
                choice = input("Make your choice: ")
                if choice == "1":
                        while go_back != True:
                                print("Do you want to turn to a specific angle or add on to the current angle?")
                                print("1) Specific angle")
                                print("2) Add to current angle")
                                print("3) Go back")
                                choice = input("Make your choice: ")
                                if choice == "1":
                                        print("Input an amount of degrees to turn or type 'random': ",end="")
                                        angle = get_angle()
                                        print("Your angle is now",angle,"degrees.")
                                        go_back = True
                                elif choice == "2":
                                        print("Input an amount of degrees to turn or type 'random': ",end="")
                                        add_angle = get_angle()
                                        angle = angle + add_angle
                                        while angle >= 360:
                                                angle = angle - 360
                                        while angle < 0:
                                                angle = angle + 360
                                        print("Your angle is now",angle,"degrees.")
                                        go_back = True
                                elif choice == "3":
                                        print("Your angle is still",angle,"degrees.")
                                        go_back = True
                                else:
                                        print("You need to make a valid choice.")
                                        print("")
                elif choice == "2":
                        distance_X,distance_Y = get_distance(angle)
                        position_X,position_Y = position_X+distance_X,position_Y+distance_Y
                        print("Your coordinates are (",position_X,",",position_Y,").")
                        exact_X,exact_Y = get_Exact(exact_X,exact_Y,angle)
                elif choice == "3":
                        print("Your coordinates are (",position_X,",",position_Y,").")
                        print("Your angle is",angle,"degrees.")
                        print("Your distance from the origin is",math.sqrt(position_X**2 + position_Y**2))
                elif choice == "4":
                        print("Your exact coordinates are (",exact_X,",",exact_Y,").")
                        print("Your angle is",angle,"degrees.")
                elif choice == "5":
                        reset = True
                elif choice == "6":
                        sys.exit()
                else:
                        print("You need to make a valid choice.")
                        print("")
        start()
start()