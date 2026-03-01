# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Odus")


# The game starts here.

label start:

    scene bg room1

    "The Doctor" "You have worsening symptoms consistent with Lewy-Body Dementia. Please inform your family and loved ones."
    "The Doctor" "Do you live with someone who can suppport you? With someone with you?"
    "Odus" "...."
    "The Doctor" "Do you have local family?"
    "Odus" "..."
    "You just end up leaving the doctor's office, much to Doctor A's dismay. Talking about your daughter makes you upset..for reasons you actually can't really remember."

    "You wake up... after a long night of little sleep."
    "Do you decide to take your medicine or not?"
    
    "Mr.Pickles" "*meoww*"
    "Odus" "Mr.Pickles?..Where are you?"
    "You begin to feel a great sense of joy, like something you lost for so long finally came back.."
    "Mr. Pickles!..Mr. Pickles?.."

label choices:
"Odus" "Do you take your medicine?"

menu:
    "Do you take your medicine?":
        jump choices1_a:
    "Dont take the medicine":
        jump choices1_b:
    "Take the medicine"


label choices1_a:
     "You slowly begin to see more clearly. You feel less groggy about the night and feel more alert and prepared to take on the next day."
label choices1_b:
    Odus "..What am I even taking this medicine for, anyway? I feel fine.."
    "You begin to hear some faint meowing."
        scene bg room2 with fade in

    Your phone rings from your daughter Maria
     "Odus" "Marina.. I haven't heard from her in months.. only calls when she needs something anyway."
    
menu:
"Do you accept the call?"
        jump choices1_c:
     "Accept the call"

        jump choices1_d:
     "Decline the call"

label choices1_c:
    "You answer the phone. "
label choices1_d:
    "You choose not to answer the phone. And yet your phone keeps on ringing, and you are forced to answer."
   "Marina" "Dad.. how are you?'

    
    label choices 
    scene bg room2 with fade

    return