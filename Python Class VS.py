x=input("what is your name? ")
print("welcome to Python!")
d=input("Do you want to go east, to the dangerous lion, or west, to the harsh winter tundra? ")
if d=="west":
    d=input("West it is, you will have to survive on your own with few materials. Your materials are wood, metal, and wool. Are you up for it? ")
    if d=="No":
         print("Wrong choice player, you will spend you whole life here!")
         print("You have completed the game!")
    elif d=="Yes":
        print("Woopsie! You have ran out of all of your materials!")
        d=input("Will you survive without any materials? ")
        if d=="yes":
            print("Well done! Even from scarcity of material, you have escaped the tundra!")
            print("You have completed the game!")
else:
    d=input("Great choice trailblazer! You have chose the path of the lion. You will have to build you own materials. Are you ready? ")
    if d=="Yes!":
            print("Oh no, you have ran out of your metals to build your weapons. Now, you will have to build it by scratch.")
            print("Well done, player, you have defeated the lion with few materials only! Congratulations!")
    if d=="No":
            print("Well, well, well. You have chosen the wrong choice player. Now you will be in this place forever!")
    else:
            print("You have completed the game!")


    

