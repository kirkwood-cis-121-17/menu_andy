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
                        print("Your random angle is ", choice, ".", sep = '')
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
        return distanceX,distanceY,distance

def get_Exact(exact_X,exact_Y,angle,distance): #HAHAHAHAHA THIS IS DISGUSTING WHAT AM I EVEN DOING???
        string = str(angle)
        dist = str(distance)
        
        if exact_X == "0" or exact_Y == "0":
                if exact_X == "0":
                        exact_X = dist + "cos("+string+")"
                else:
                        exact_X += "+" + dist + "cos("+string+")"
                if exact_Y == "0":
                        exact_Y = dist + "sin("+string+")"
                else:
                        exact_Y += "+" + dist + "sin("+string+")"
        else:
                exact_X += "+" + dist + "cos("+string+")"
                exact_Y += "+" + dist + "sin("+string+")"
        
        lyst_X = []
        lyst_Y = []
        get_out = 0
        thing = exact_X
        while get_out != 1:
                try:
                        in_S = thing.index("(")
                        in_E = thing.index(")")
                        lyst_X.append(thing[(in_S + 1):(in_E)])
                        thing = thing[(in_E + 2):]
                        if len(thing) < 2:
                                get_out = 1
                except ValueError:
                        get_out = 1
        
        get_out = 0
        thingy = exact_Y
        while get_out != 1:
                try:
                        in_S = thingy.index("(")
                        in_E = thingy.index(")")
                        lyst_Y.append(thingy[(in_S + 1):(in_E)])
                        thingy = thingy[(in_E + 2):]
                        if len(thingy) < 2:
                                get_out = 1
                except ValueError:
                        get_out = 1
        
        big_counter_max = len(lyst_X) - 1
        big_counter = 0
        little_counter = 1
        little_counter_max = len(lyst_X)
        temp_list = exact_X.split("+")
        join_X = 0

        while big_counter < big_counter_max:
                while little_counter < little_counter_max:
                        base = int(lyst_X[big_counter])
                        compare = int(lyst_X[little_counter])
                        if base - 180 == compare or base + 180 == compare:
                                temp_big = str(temp_list[big_counter])
                                temp_little = str(temp_list[little_counter])
                                big_index = temp_big.index("c")
                                little_index = temp_little.index("c")
                                big_num = int(temp_big[:big_index])
                                little_num = int(temp_little[:little_index])
                                if big_num > little_num:
                                        temp_list[big_counter] = str(big_num - little_num) + str(temp_big[big_index:])
                                        del temp_list[little_counter]
                                        join_X = 1
                                elif little_num > big_num:
                                        temp_list[little_counter] = str(little_num - big_num) + str(temp_little[little_index:])
                                        del temp_list[big_counter]
                                        join_X = 1
                                else:
                                        if big_counter > little_counter:
                                                del temp_list[big_counter]
                                                del temp_list[little_counter]
                                                join_X = 1
                                        elif little_counter > big_counter:
                                                del temp_list[little_counter]
                                                del temp_list[big_counter]
                                                join_X = 1
                                big_counter = big_counter_max
                                little_counter = little_counter_max
                        elif base == compare:
                                temp_list=exact_X.split("+")
                                temp_big = str(temp_list[big_counter])
                                temp_little = str(temp_list[little_counter])
                                big_index = temp_big.index("c")
                                little_index = temp_little.index("c")
                                big_num = int(temp_big[:big_index])
                                little_num = int(temp_little[:little_index])
                                temp_list[big_counter] = str(big_num + little_num) + str(temp_big[big_index:])
                                del temp_list[little_counter]
                                join_X = 1
                                big_counter = big_counter_max
                                little_counter = little_counter_max
                        little_counter += 1
                big_counter += 1
                little_counter = big_counter + 1
        
        if join_X == 1:
                exact_X = "+".join(temp_list)
        
        big_counter_max = len(lyst_Y) - 1
        big_counter = 0
        little_counter = 1
        little_counter_max = len(lyst_Y)
        join = 0
        temp_list = exact_Y.split("+")
        
        while big_counter < big_counter_max:
                while little_counter < little_counter_max:
                        base = int(lyst_Y[big_counter])
                        compare = int(lyst_Y[little_counter])
                        if base - 180 == compare or base == compare - 180:
                                
                                temp_big = str(temp_list[big_counter])
                                temp_little = str(temp_list[little_counter])
                                big_index = temp_big.index("s")
                                little_index = temp_little.index("s")
                                big_num = int(temp_big[:big_index])
                                little_num = int(temp_little[:little_index])
                                if big_num > little_num:
                                        temp_list[big_counter] = str((big_num - little_num)) + str(temp_big[big_index:])
                                        del temp_list[little_counter]
                                        join = 1
                                elif little_num > big_num:
                                        temp_list[little_counter] = str(little_num - big_num) + str(temp_little[little_index:])
                                        del temp_list[big_counter]
                                        join = 1
                                else:
                                        if big_counter > little_counter:
                                                del temp_list[big_counter]
                                                del temp_list[little_counter]
                                                join = 1
                                        elif little_counter > big_counter:
                                                del temp_list[little_counter]
                                                del temp_list[big_counter]
                                                join = 1
                                big_counter = big_counter_max
                                little_counter = little_counter_max
                        elif base == compare:
                                temp_list=exact_Y.split("+")
                                temp_big = str(temp_list[big_counter])
                                temp_little = str(temp_list[little_counter])
                                big_index = temp_big.index("s")
                                little_index = temp_little.index("s")
                                big_num = int(temp_big[:big_index])
                                little_num = int(temp_little[:little_index])
                                temp_list[big_counter] = str(big_num + little_num) + str(temp_big[big_index:])
                                del temp_list[little_counter]
                                join = 1
                                big_counter = big_counter_max
                                little_counter = little_counter_max
                        little_counter += 1
                big_counter += 1
                little_counter = big_counter + 1
                
        if join == 1:
                exact_Y = "+".join(temp_list)
        
        if exact_X == "":
                exact_X = "0"
        if exact_Y =="":
                exact_Y = "0"
                
        return exact_X,exact_Y
        
def angle_menu(angle):
        go_back = False
        while go_back != True:
                print("Do you want to turn to a specific angle or add on to the current angle?")
                print("1) Specific angle")
                print("2) Add to current angle")
                print("3) Go back")
                choice = input("Make your choice: ")
                if choice == "1":
                        print("Input an amount of degrees to turn or type 'random': ",end="")
                        angle = get_angle()
                        while angle >= 360:
                                angle = angle - 360
                        while angle < 0:
                                angle = angle + 360
                        print("Your angle is now ",angle," degrees.",sep = '')
                        go_back = True
                elif choice == "2":
                        print("Input an amount of degrees to turn or type 'random': ",end="")
                        add_angle = get_angle()
                        angle = angle + add_angle
                        while angle >= 360:
                                angle = angle - 360
                        while angle < 0:
                                angle = angle + 360
                        print("Your angle is now ",angle," degrees.",sep = '')
                        go_back = True
                elif choice == "3":
                        print("Your angle is still ",angle," degrees.",sep = '')
                        go_back = True
                else:
                        print("Make a valid choice of I'll lick you.")
                        print("")
        return angle

def move(choice):
        angle = choice
        enrage = 0
        position_X = 0
        position_Y = 0
        exact_X = "0"
        exact_Y = "0"
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
                        angle = angle_menu(angle)
                elif choice == "2":
                        distance_X,distance_Y,distance = get_distance(angle)
                        position_X,position_Y = position_X+distance_X,position_Y+distance_Y
                        print("Your coordinates are (",position_X,",",position_Y,").",sep = '')
                        exact_X,exact_Y = get_Exact(exact_X,exact_Y,angle,distance)
                elif choice == "3":
                        print("Your coordinates are (",position_X,",",position_Y,").",sep = '')
                        print("Your angle is ",angle," degrees.",sep = '')
                        print("Your distance from the origin is ",math.sqrt(position_X**2 + position_Y**2),".",sep = '')
                elif choice == "4":
                        print("Your exact coordinates are (",exact_X,",",exact_Y,").",sep = '')
                        print("Your angle is ",angle," degrees.",sep = '')
                elif choice == "5":
                        reset = True
                elif choice == "6":
                        sys.exit()
                else:
                        print("Make a valid choice or I'll lick you.")
                        print("")
        start()
if __name__ == "__main__":
    start()
