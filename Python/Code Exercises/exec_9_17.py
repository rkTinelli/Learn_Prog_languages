# Get user data
reply = input('Are you feeling ill? ')
if (reply == "YES"):
    reply = input('Do you have a headache? ')
    if (reply == "YES"):
        reply = input('Do you have a funny tummy? ')
        if (reply == "YES"):
            reply = input('Were you sitting up all night watching Netflix? ' )
            if (reply == "YES"):
                print("Stop sitting up all night watching Netflix")
            else:
                print("Sorry, I have no idea... Go see a doctor!")
        else:
            print("Drink some milk and go see the nurse")
    else:
        print("Take two tablets and go home!")
else:
    print("Glad to hear that! Have a nice day!")
