import sys

def main():
        while quit != True:
                new_game()

def new_game():
        print("")
        print("In this world, in this program on your hard drive, you are a god. The future is yours to create.")
        print("In the endless expanse of data, a virtual world is created. The people in this world have only just begun to create civilization.")
        print("It was not long before clans clashed and wars were fought. Lives were ended needlessly; pointlessly. And you ask yourself:")
        print("Is this the path I want for these people? Or shall I guide them back to the light?")
        print("")
        print("1) I should give them another chance.")
        print("2) I must discipline them.")
        handle_one()

def choose():
        choice = 0
        while choice != 1 or choice != 2 or choice != 9:
                try:
                        choice = input("Make your choice: ")
                        choice = int(choice)
                        if choice == 1 or choice == 2 or choice == 9:
                                pass
                        else:
                                raise ValueError()
                        break
                except ValueError:
                        print("Enter a number - 1, 2 to choose or 9 to quit.")
        return choice
        
def handle_one():
        choice_one = choose()
        
        if choice_one == 1:
                print("")
                print("In your benevolence, you tell the people that you shall give them another chance. They have committed greivous mistakes, but")
                print("you still believe that they can strive towards a better future. And so you wait.")
                branch_A()
        elif choice_one == 2:
                print("")
                print("You deliver your message, and your judgement, from the sky. You scorch the land with the light of the sun and drown")
                print("them with torrential rain. But you leave the people alive, and tell them to never stray from the light again.")
                branch_B()
        elif choice_one == 9:
                sys.exit()
                
def branch_A():
        print("")
        print("Millenia pass. And the people still continue their warring ways. They have developed tools of copper and iron, and the first")
        print("kingdoms have been established. History runs red with blood and chaos, and treachery and deceit plague civilization as whole.")
        print("Once more you ask: Is this the path these people shall walk, or will you take matters into your own hands?")
        print("")
        print("1) This is their path - they will walk it.")
        print("2) This is not the path I wanted - I will fix it.")
        choice_one = 1
        handle_two(choice_one)

def branch_B():
        print("")
        print("Your message rings true with the people, at least for a time. But eventually, tales of the chaos you brought up on the")
        print("land faded to a myth. The people returned to their violent, warring ways, and developed better and better methods for")
        print("killing. Clans became kingdoms, and stones were replaced by cold steel. Looking upon the world, you ask yourself:")
        print("The people cannot rule themselves - so will I let the chaos continue, or rule them myself?")
        print("")
        print("1) I will let the chaos continue.")
        print("2) I must become their ruler.")
        choice_one = 2
        handle_two(choice_one)
        
def handle_two(choice_one):
        choice_two = choose()
        
        if choice_one == 1 and choice_two == 1:
                print("")
                print("With a remorseful gaze, you watched the people continue to kill themselves. Some periods were graced by lack of war,")
                print("but it was never a peace brought about by the goodness of people, but fear of retaliation. Inevitably, however,")
                print("the cycle of carnage would begin anew.")
                branch_AA()
        elif choice_one == 1 and choice_two == 2:
                print("")
                print("You descended upon the land, becoming a beacon of light in the sky. From there, you guided the people towards a better")
                print("future, and warned the world of your judgement should they continue their warring ways. From the sky you watched, ever")
                print("quick to spot and prevent all manner of injustices, guiding the world to a golden age.")
                branch_AB()
        elif choice_one == 2 and choice_two == 1:
                print("")
                print("With a remorseful gaze, you watched the people continue to kill themselves. Some periods were graced by lack of war,")
                print("but it was never a peace brought about by the goodness of people, but fear of retaliation. Inevitably, however,")
                print("the cycle of carnage would begin anew.")
                branch_AA() # path AA and BA converge to one point
        elif choice_one == 2 and choice_two == 2:
                print("")
                print("With an iron fist you descend, demonstrating your power to the entire world. No longer would you let the people continue")
                print("their destructive ways. You would be eternally vigilant, a purveyor of justice. As forced as the peace may be, someday the")
                print("people would come to appreciate it. Of that, you were sure.")
                branch_BB()
        elif choice_two == 9:
                sys.exit()
                
def branch_AA():
        print("")
        print("Eventually, the people began to explore and colonize new planets. Their destruction changed targets from themselves to life on other planets.")
        print("They would mine planets dry of resources and abandon them at speeds faster than light. If they were to stop, then the people would surely")
        print("die. Their home planet, after all, was already broken. The only thing leftto them was among the stars. Finally, you came to a realization.")
        print("The people would destroy the universe if you didn't stop them. And so you were left with one more choice:")
        print("")
        print("1) Let the people prosper until they destroy themselves and the universe.")
        print("2) Destroy the people, and let other worlds survive.")
        handle_three()

def branch_AB():
        print("")
        print("Under your guidance, the people advanced faster than ever before. War and crime were nonexistent. It was not long before the people had")
        print("to travel to outer space to find the resources needed to feed themselves. It was then that you realized that you had made a fatal error.")
        print("In trying to keep the people in check, you let them outsource the destruction you loathed to other planets and their civilizations.")
        print("You were left with one more choice: would you sacrifice other worlds for the people, or the people for the others?")
        print("")
        print("1) Even if it brings harm elsewhere, I cannot kill an entire civilization. I will sacrifice other worlds for the people.")
        print("2) I cannot let the people kill countless others. I will sacrifice the people and trade one civilization for countless others.")
        handle_three()

def branch_BB():
        print("")
        print("Under your rule, you crushed any potential for war and crime, yet your rule left the people unable to develop new technology, as")
        print("the people feared your rule and you judgement. The people prospered in a strict sense, but the world was only so large. The people")
        print("grew to the point where the world could no longer feed them. But when you looked up at the stars, you saw that you could still save")
        print("the people, at the cost of life beyond the stars. So you were left with one more choice: would you free the people, or let them die?")
        print("")
        print("1) I cannot let the people die. I will let them go, even if it destroys other planets and their people.")
        print("2) If I let the people go free, they will return to their destructive ways and destroy the universe. I must let them die.")
        handle_three()
        
def handle_three():
        choice_three = choose()
        
        if choice_three == 1:
                print("")
                print("The people prospered for millenia. Outer space was, after all, vast and seemingly unending. But as new planets became")
                print("harder to find, resources rose in price. The people's poor began to starve. Finally, when there was nothing left to")
                print("exploit, and no more alien life forms to kill, the last of the people died. Across the vast universe, no planet remained")
                print("untouched. In the end, the people could not escape their destructive tendencies and as a result brought about the end of the")
                print("universe. The steps that lead to this result felt nearly irrelevant. No matter what path you took, no matter how many times")
                print("you reset the world, the people, and all species, were destined to be cut short by your hand or live long enough to end the") 
                print("world. After traveling through the alien planets, you come to a realization. If the people didn't destroy the universe,")
                print("someone else would have. The universe would have come to and end one way or another. With this knowledge in hand, you must")
                print("one more decision.")
                end1()
        elif choice_three == 2:
                print("")
                print("You whispered your apologies before you ended the world. From the heavens, you called upon a storm that exceeded every")
                print("measure of destruction the people had - a storm that only a god could create. You bathed the world in cleansing rain,")
                print("driving the people to extinction. Every trace of their existence was drowned beneath the sea, leaving their planet as a clean")
                print("slate. Looking out to the stars, you think of all the life that you had just saved. At the same time, you know that they will")
                print("never realize just how much you did for them. As you walk among the stars, you see the budding civilizations on alien panets,")
                print("and realize something. They very well may repeat the mistakes of those you had just killed. Some day, you may have to wipe out")
                print("these alien life forms, too, unless you end them now. And so you must make one more decision.")
                end2()
        elif choice_three == 9:
                sys.exit()

def end1():
        print("")
        print("Will you leave the universe dead, or bring it back to life?")
        print("1) Leave it dead")
        print("2) Give it life")
        
        choice_four = choose()
       
        if choice_four == 1:
                print("")
                print("The universe was given life. And because it was given life, it was destined to die. Perhaps life itself was an anomaly;")
                print("a blip in the nothingness of the universe that would eventually drive itself towards death. And as such, the universe has")
                print("now returned to its normal form. With nothing left to watch, you take your leave.")
                print("")
                print("Play again?")
                print("1) Yes")
                print("2) No")
                
                choice_five = choose()
                
                if choice_five == 1:
                        pass
                else:
                        sys.exit()
                        
        elif choice_four == 2:
                print("")
                print("The universe was created. And because it was created, it was destined to be destroyed. Such a pattern could be observed")
                print("throughout time. A pot would eventually shatter, no matter how well it was made. And yet, the fact that it all ends is what")
                print("gives meaning. The universe will never truly end. And without something that does end, there will never be meaning. And so")
                print("you give life to the universe, knowing full well that it will die, and resume your vigil.")
                print("")
                print("Play again?")
                print("1) Yes")
                print("2) No")
                
                choice_five = choose()
               
                if choice_five == 1:
                        pass
                else:
                        sys.exit()
        elif choice_four == 9:
                sys.exit()
                
def end2():
        print("")
        print("Will you end all life, or leave it be?")
        print("1) Leave it be")
        print("2) End it all")
        
        choice_four = choose()
        
        if choice_four == 1:
                print("")
                print("You believe. You believe, that somewhere, somehow, that someone will find a way to live without destroying. So you continue")
                print("your watch, and search for another planet, another race, to watch over and guide. Perhaps it will end the same way as before,")
                print("but you believe. And so you descend upon another planet and its people, and begin your watch anew.")
                print("")
                print("Play again?")
                print("1) Yes")
                print("2) No")
                
                choice_five = choose()
                
                if choice_five == 1:
                        pass
                else:
                        sys.exit()
        elif choice_four == 2:
                print("")
                print("Nothing. That was all the universe ever was in the beginning. It was only fitting that it would return to nothing.")
                print("Something came from nothing. Surely nothing can come from something as well. And so, you bring it all to an end.")
                print("")
                print("Play again?")
                print("1) Yes")
                print("2) No")
                
                choice_five = choose()
                                
                if choice_five == 1:
                        pass
                else:
                        sys.exit()
        elif choice_four == 9:
                sys.exit()
        
main()