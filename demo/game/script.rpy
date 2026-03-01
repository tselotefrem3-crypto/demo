# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Odus")


# The game starts here.

label start:
    "Doctor A." "You have worsening symptoms consistent with Lewy-Body Dementia. Please inform your family and loved ones."
    "Doctor A." "Do you live with someone who can suppport you? With someone with you?"
    "Odus" "...."
    "Doctor A." "Do you have local family?"
    "Odus" "..."
    "You just end up leaving the doctor's office, much to Doctor A's dismay. Talking about your daughter makes you upset..for reasons you can't really remember."
    "You wake up... after a long night of little sleep."
    "Do you decide to take your medicine or not?"
    
    "Mr.Pickles" "*meoww*"
    "Odus" "mr.pickles?..Where are you?"
    "You begin to feel a great sense of joy, like something you lost for so long finally came back.."
    "Ill /eeee/ wrhy"

label choices:
    Odus "question?"

menu:
    "Take meds":
        jump choices1_a:
    "Dont take meds":
        jump choices1_b:


label choices1_a:
     "You slowly begin to see more clearly. You feel less groggy about the night and feel more alert and prepared to take on the next day."
label choices1_b:
    Odus "..What am I even taking this medicine for, anyway? I feel fine.."





    return