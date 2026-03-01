# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Odus")


# The game starts here.

label start:

    scene bg room1

    "The Doctor" "You have worsening symptoms consistent with Lewy-Body Dementia. Please inform your family and loved ones."
    "The Doctor" "Do you live with someone who can suppport you? With someone with you?"
    "Odus" "...."
    "The Doctor" "Do you have local family?"
    "Odus" "...."
    "You just end up leaving the doctor's office, much to Doctor A's dismay. Talking about your daughter makes you upset..for reasons you actually can't really remember."

    "You wake up... after a long night of little sleep."
    "Do you decide to take your medicine or not?"
    
    "Mr.Pickles" "*meoww*"
    "Odus" "Mr.Pickles?..Where are you?"
    "You begin to feel a great sense of joy, like something you lost for so long finally came back.."
    "Mr. Pickles!..Mr. Pickles?.."

    "The day fades away. You keep searching for Mr. Pickles..certain he's just hiding somewhere, or perhaps just tired or sleeping."

label choices:
"Odus" "Do you take your medicine?"

menu:
    "Do you take your medicine?":
    "take the medicine"
        jump choices1_a
    "Dont take the medicine"
        jump choices1_b


label choices1_a:
    "You slowly begin to see more clearly. You feel less groggy about the night and feel more alert and prepared to take on the next day."
    jump choices1_c
label choices1_b:
    Odus "..What am I even taking this medicine for, anyway? I feel fine.."
    "You begin to hear some faint meowing."
        #scene bg room2 with fade in

    Your phone rings from your daughter Maria
"Odus" "Marina.. I haven't heard from her in months.. only calls when she needs something anyway."
    jump choices1_d
     
    


label choices1_c:
    "You answer the phone"
    “Marina” “Dad im happy you answered...Is everything okay? Im sorry I havent visited...but can you come to Virginia beach with me? My beach house is really cozy, and I just bought it with Micheal. You haven’t seen me in 4 months. Come on, I know that was where your last trip with mom was.. But it can be special. You know?”

“Odus” “....” 

“Marina” “You need to get out of the house, the isolation is killing you.” 

“Odus” “....” 

“Marina” ‘“Come on, its her death anniversary, we should honor her by going to the old beach house.” 

“Odus” “.. Okay..” 
jump choices2_a

label choices1_d:
    "You answer the phone"
    “Marina” “Dad im happy you answered...Is everything okay? Im sorry I havent visited...but can you come to Virginia beach with me? My beach house is really cozy, and I just bought it with Micheal. You haven’t seen me in 4 months. Come on, I know that was where your last trip with mom was.. But it can be special. You know?”

“Odus” “....” 

“Marina” “You need to get out of the house, the isolation is killing you.” 

“Odus” “....” 

"Marina" "Come on, its her death anniversary, we should honor her by going to the old beach house.” 

“Odus” “.. Okay..” 
jump choices2_b


#Walk Scene Chose No
label choices2_b:
“As you tremble along the stairs, walking down gripping the wooden railing. You hear a loud rapid knock on your door.” 

“Ms.???” “Ah it's nice to see you Odus, I hope all is well. We didn't have you at David’s dinner. How come?”
“Odus” “I.. I dont remember..”
“Mrs. ???” “Have you seen a doctor yet? Odus, its not healthy to go unchecked. You could have some form of.. Forgetfulness?” 
“Odus” “... How would you know?..” 
“Mrs. ???” “You know, Mr Goldstein has Alzheimer's, you kind of remind me of him.” 
“Odus” “... Goldstein..?” 
“Mrs. ???” “You know? The guy who lives a few blocks down..”
“Odus” “Huhhhh???”
“Mrs. ???” “The guy with the cowboy hat and runs alot?” 
“Odus” “....” 
“Mrs. ???” “Odus?” 
“Odus” “.....”
“Mrs. ???” “Odus? What year is it?”
“Odus” “Goldstein…” 
You feel an uncontrollable amount of anger at the name of /Goldstein/ and begin to stumble away irritably. 
“Mrs. ???” “Ms.???” “Odus!” 
“After immense emotional pressure, you find yourself at home after a blurry hour.”
“You choose to sleep off the horrible day…for reasons you..can’t actually remember right now.”
jump choices3_a

  
#Walk Scene Chose Yes
label choices2_a:
"As you tremble along the stairs, walking down gripping the wooden railing. You hear a loud rapid knock on your door.”
"Mrs. Clover” “Ah it's nice to see you Odus, I hope all is well. We didn't have you at David’s dinner. How come?”
"Odus” “What day was it? I don’t even remember this.”
"Mrs. Clover” “3 days ago, July 31st.. You told us yes last week?”
"Odus” “It's May."
"Mrs. Clover” “What year is it? Gosh are you okay? You’ve been in your house for days, canceled your monthly steak dinners for 3 months straight. I haven’t seen you leave the house."
"Odus" "Its the big 25.." 
jump choices3_b
  
"Your shuffling gait had led you to fall flat on your face, and a harsh bruise on your right knee."


#Vacation Scene Chose No: Bad Ending
label choices3_a:
“Marina” “We’re here, Dad.” 

“Odus” “...” 

“Michael” “Hey, nice to see you again Mr. Odus.”

“Odus” “Oh.. hello Michael.. Are you her.. Boyfriend?..” 

“Michael” “No, you never came to the wedding.” 
 
“Odus” “Wedding?..” 

“Michael” “Yeah, it happened last spring, we had it in Los Angeles. Marina’s favorite.”  

“Odus” “Why.. Why wasn't I invited?.. I.. I didn't.. I.. I would remember.. I wouldn't miss my daughter’s  wedding..” 

“Marina” “Dad are you okay?” 

“Odus” “Marina.. Michael… the wedding was just last June.. Your mother hates spring weddings..”  

“Michael” “The wedding was in the spring, Josephine has been dead for 2 years.. Mr Odus..” 

“Marina” “We gave you the invitation to the wedding, but you tore it up thinking it was a bank statement.. Sorry dad..” 

“Odus” “Don’t be ridiculous! I saw Josephine just yesterday morning with me in the kitchen.  I saw her flowers in the garden, with that lovely smell of daffodils in the spring…she’s been planting recently! Josephine was tending to them all last afternoon. And don't wish ill on your mother!”

“Marina” “Dad—“

“You see Josephine in the water. A great joy slowly begins to wash over you, and then overtake you all at once, and a great grin breaks out on your face.”

”Josephine” “….”

”Odus” “JOSEPHINE! There you are! See? …Why are you so far out in the water anyway?…And…how are you so far out..?”

”Josephine” “….”

“Josephine walks towards the horizon of the ocean.”

”Odus” “Josephine..?”

”Marina” “Dad? What’s going on.. Are you OK?”

”Odus” “JOSEPHINE!”

“Odus rushes in after her, in a rash attempt to save her.”

”Odus begins to flounder, and his hands begin to shake. He keeps swimming nonetheless with increased vigor, as  he realizes his love is leaving.”

”Odus” “JOSEPHINE-Don’t..don’t leave me, please! Not again..Never again! Please..”

”Michael” “MR. ODUS! SOMEBODY HELP, PLEASE!”

“Marina” “THATS MY FATHER! GET A LIFEGUARD! CALL 911!”

”Marina and Michael both begin to jump in and swim after Odus, but to no avail..”

”Odus loses energy quickly, and can barely keep his head above water.”

“Odus” “Josephine! JOSEPHINE! Josephine, please..where are you?”

”Odus’ vision grows increasingly spotty...”

”Odus’ struggling slowly relaxes, and his panic slowly fades..He sees Josephine once again, hand outstretched like his saving grace..”

“And Josephine slowly fades away..and his consciousness goes black, as he slowly floats to the bottom of the sea floor.”

return

#Vacation Scene Chose Yes 
label choices3_b:
“Marina” “We’re here, Dad.” 

“Odus” “...” 

“Michael” “Hey, nice to see you again Mr. Odus.”

“Odus” “Oh.. hello Michael.. Are you her.. boyfriend?..” 

“Michael” “No, you never came to the wedding.” 
 
“Odus” “Wedding?..” 

“Michael” “Yeah, it happened last spring, we had it in Los Angeles. Marina’s favorite.”  

“Odus” “Why.. Why wasn't I invited?.. I.. I didn't.. I.. I would remember.. I wouldn't miss my dearest  wedding..” 

“Marina” “Dad are you okay?” 

“Odus” “Marina.. Michael… the wedding was in June.. Your mother hated spring weddings..”  

“Michael” “The wedding was in the spring, Josephine has been dead for 2 years.. Mr Odus..” 

“Marina” “We gave you the invitation to the wedding, but you tore it up thinking it was a bank statement.. Sorry Dad..” 

“Odus” “Don’t be ridiculous! I saw Josephine just yesterday morning with me in the kitchen.  I saw her flowers in the garden, with that lovely smell of daffodils in the spring…she’s been planting recently! Josephine was tending to them all last afternoon. And don't wish ill on your mother!”
 
“Marina” “Dad—“

“You see Josephine in the water. A great joy slowly begins to wash over you, and then overtake you all at once, and a great grin breaks out on your face.”

”Josephine” “….”

Odus” “JOSEPHINE! There you are! See? …Why are you so far out in the water anyway?…And…how are you so far out..?”

”Josephine” “….”

“Josephine walks towards the horizon of the ocean.”

”Odus” “Josephine..?”

”Marina” “Dad? What’s going on.. Are you OK?”

“Odus starts to go after Josephine..” 

“Odus begins to pause his footsteps, much to his daughter’s increasing confusion.”

“Odus” “You’re not really here, are you? Are they..Are they telling the truth, Josephine?”

“Josephine” “...” 

“Odus” “Thought so. I guess, somewhere along the way of you not being here..I forgot about you too. I never thought that would happen. Events, yes, information, maybe.. but how could I forget that it was YOU who always smelled like daffodils, not the garden you always swapped flowers for every 3 months?”

“Josephine” “…”

”Odus” “I think..I think this means I need to let you go, Josephine.”

”Josephine” “…” *CHANGE CHARACTER SPRITE TO SMILING ONE HERE”

”Josephine, whether her spirit, soul, hallucination, or something else entirely…eventually is gone from your view. She slowly walks away, but not before giving you a final nod. Perhaps your own subconsciousness provides you your own validation of your decision, perhaps a sign from the other side, perhaps Josephine yourself entirely, you do not know.”

“You smile back nonetheless, and turn back to Marina, firmly taking her hand, without shaking, and walk alongside her to the restaurant where you met Josephine.”

“Time moves on, you move on, yet still think of Josephine. Sometimes you still see her, but never chase her…not anymore. And she smiles and nods every time, which you reciprocate like the first time you met her, like a test of sorts to see if you remember the first time you saw her and also the last time, and eventually goes away.”

“Years later..”

”Marina” “I’ll be out of his room in a few minutes, Michael..”

”Michael” “We need to leave soon, through. Lucas, Roland, and Mabel can’t be left alone for long at this age..you know this!”

”Marina smiles to herself, and slowly fades as she looks around her late father’s old bedroom.”

“She’s nearly done sorting through his things, save for one little bottom drawer on the right side of the bed.”

”She opens the drawer, only to find empty prescription bottles. Her heart rate spikes. She didn’t know he was ill before he passed.”

”She sees the names, one by one…”

”Rivastigmine. Donepize...eventually finding remaining pills of Meematine…”

”She makes a mental note to look up the prescription names, but both worry and curiosity overtake her and she drops the bottles, picking up her phone instead to look up the names.”

“She realizes these were to solve hallucinations..memory issues..and comes to a horrifying realization her father was actively suffering from dementia.”

“She begins to write his eulogy, tears streaming down her face, yet she knows she owes this much to her father.”

”A few weeks pass by..”

”Marina sees herself standing above the community who showed up for Odus’ passing. After he saw Josephine on the water, while his health still declined, he no longer severely struggled with believing his hallucinations, and seeing her once more brought out the old Odus—the one who showed up for others, and bonded his community together since Josephine and him had moved there so many decades ago. She takes a breath, asking for strength from her father from beyond, and slowly begins to speak, voice shaking nonetheless..”

return