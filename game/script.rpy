define madison = Character('Madison', color="#c8ffc8")
define alex = Character("Alex")

   
play music "audio/summerbeachambience.mp3"

label start:    

    scene bg beach day with fade
    
    show madison angry 
    madison "Hey Alex!"
    madison "Did you bring beer and a frisbee?"
    madison "Where's Mattie? I heard her barking."
    madison "...Alex?"
    hide madison
    scene bg dogbeachsunset with vpunch
    show alex happy at right with moveinbottom
    alex "I'm over here!"
    show madison angry at left with moveinleft
    madison "Yikes... it's getting cold."
    alex "Do you want to leave?"
    madison "No way!"
    show madison sad
    madison "I think once I have a beer, I'll warm up."
    madison "Check out that beautiful sunset! Um, where's my phone?"
    alex "Forget about it! Let's just relax and enjoy the view. It's probably in the car"

   

menu:
    "Which way did Mattie go?"

    "Left":
        alex "Let's check out the trees on the left."
        $ is_lost = True
    "Right":
        madison "Ok, right works for me."
        $ is_lost = False
scene bg beach sunrise with Dissolve(3.0)
scene bg beach noon with Dissolve(3.0)
show madison sad at left with moveinleft
madison "We've been searching all night. Are you sure we're not lost?"
if is_lost:
    show alex sad at right with moveinleft
    alex "I hope not, but I have a bad feeling about this."
else:
    show alex happy at right with moveinleft
    alex "We're fine! Look! Over at the end of trees."
    alex "I'm the best scout around." 
               
play sound "audio/dogpanting.mp3"

return
