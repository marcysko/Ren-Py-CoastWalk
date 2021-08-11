# The script of the game goes in file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define madison = Character("Madison")
define alex = Character("Alex")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    madison "Hey Alex!"
    madison "Did you bring beer and a frisbee?"
    madison "Where's Mattie? I heard her barking."
    madison "...Alex?"
    alex "I'm over here!"
    madison "Yikes... it's getting cold."
    alex "Do you want to leave?"
    madison "No way!"
    madison "I think once I have a beer, I'll warm up."
    madison "Check out that beautiful sunset! Um, where's my phone?"
    alex "Forget about it! Let's just relax and enjoy the view. It's probably in the car"

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    return
