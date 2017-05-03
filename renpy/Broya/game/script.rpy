# BROYA (new try)
# Yandrak45 (2017)

#Characters
define pov = Character("[povname]")
define k = Character("Kevin")
define b = Character("Broya")
define t = Character("Takash")
define afm = Character("@KevinAFM")
define mr = Character("@Paco77")
define m = Character("Marlo Rekreff")

#Resources
#image maintitle = ""
#image bg blank = ""
#image kevin shadow = ""

label start:

    #TITULO
#KRONI LINE
    pause 1.0
    "Yandrak45 presents..."
    pause .5
    "01000010 01110010 01101111 01111001 01100001"
    pause .5
    "More known as..."
    #scene maintitle
    #with Dissolve(2.0)
    "SYS" "Comienzo titulo"
    pause 3.0
    "SYS" "fin titulo"
    #scene bg blank
    #with Dissolve(1.0)

    #INTRO
    pause 3.0
    #show kevin shadow
    #with Dissolve(.5)
    pause .5
    "Someone" "Hello."
    pause .5
    "You" "He-hello...?"
    pause .5
#YANDRAK45 LINE
    "Someone" "Are you OK?"
    pause .5
    menu:
        "Yes...":
            pause .5
            "You" "Yes..."
            pause .5
            "Someone" "Sure?"
            pause .5
            "You" "Yes, I'm right..."
            pause .5
            "Someone" "What's your name?"
            python:
                povidiot = False
                povname = renpy.input("What's your name?")
                povname = povname.strip()
                if not povname:
                    povidiot = True
                    povname = "The player who didn't remember to write"
            pause 1.0
            pov "I'm... [povname].\nPeople call me [povname]..."
            "Someone" "Okay, [povname]. I'm Kevin, and I've found you near the river, in the East.\nYou were unconcious, so I let you to rest on my house, inside the forest."
        "Who are you?":
            pause .5
            "You" "Who are you?"
            pause .5
            "Someone" "My name is Kevin. I've found you near the river, in the East.\nYou were unconcious, so I let you to rest on my house, inside the forest."
            k "So, you got it.\nNow let me ask you..."
            k "How should I call you?"
            python:
                povidiot = False
                povname = renpy.input("What's your name?")
                povname = povname.strip()
                if not povname:
                    povidiot = True
                    povname = "Who I am?"
            pause 1.0
            pov "I'm... [povname].\nPeople call me [povname]..."
        "I'm dead...":
            pause .5
            "You" "I'm dead..."
            "Someone" "Yes, and I am Bill Gates, the founder of Microsoft"
            pause .5
            "Someone (Bill Gates?)" "Then, if you're dead..."
            pause .1
            "Someone (no, he is not mister Gates)" "You are a ghost!"
            "Someone" "And I presume your name is Casper, right?"
            python:
                povidiot = False
                povname = renpy.input("What's your name?")
                povname = povname.strip()
                if not povname:
                    povidiot = True
                    povname = "Bill Gates"
            pause 1.0
            pov "I'm not Casper the ghost...\nI'm [povname]."
            "Someone" "Casper the FRIENDLY ghost*"
            pause 1.0
            "Someone" "Sorry, [povname], i'm not Bill Gates too."
            "Someone" "My name is Kevin. I've found you near the river, in the East.\nYou were unconcious, so I let you to rest on my house, inside the forest."
    #cosas de escena

    #LA MOCHILA
    "You are in the Kevin's house."
    pause 1.0
    "[povname] is lying in the white bed."
    "There is a backplack placed in an empty desk."
    "Kevin is sitting near [povname], in the bed."
    pause 1.0
    "[povname] recognises the backpack."
    pause .5
    pov "My backpack..."
    k "I've found it near you, down in the floor."
    k "Take"
    "Kevin gives [povname] the backpack."
    pov "Thanks..."
    pause 1.0
    "The backpack looks old and broken, maybe because of the wild in the forest."
    "Maybe..."
    pause 1.0
    "When [povname] tries to remember how was his backpack in the past, he realises that there was no backpack."
    pov "Wait..."
    "Well, at least not in his memory"
    pov "I didn't have any backpack"
    k "What?"
    pov "I don't remember any backpack in the past."
    pov "In fact...\nI don't remember what happened."
    "Kevin stares at [povname], understanding."
    k "It is normal to have some lost of memory in uncommon and probably dangerous scenes..."
    pause 1.0
    k "I've found you near the river, while I were walking thought the forest."
    k "I don't know what could exactly happened to you, it's not that usual to have some visit here..."
    "I have a lot of questions and missing data of what happened."
    "But my brain... is hurting so much..."
    pause .5
    pov "I can't think properly with this headache..."
    k "Don't worry, I'm here to help you."
    k "And also do not worry about the backpack, I didn't open it."
    "Open the backpack...\nSee it content..."
#YANDRAK45 LINE
    #play sound "" cremallera
    "[povname] opens the Backpack, and looks inside it."
    pause 1.0
    "There is nothing..."
    "Wait, there's a tag with a name inside!"
    pause 1.0
    pov "Broya..."
    k "Broya?"
    "Broya..."
    k "Who is Broya?"
    pause 1.0
    pov "Kevin..."
    k "Uh?"
    pov "When you found me..."
    pause .5
    pov "... I was alone?"
    pov "There was anyone there outside, except of me?"
    k "I didn't find any more than you and the backpack."
    pause 1.0
    k "But..."
    k "Who is Broya???"
    #THE DECISSION
    menu:
        "Broya...":
            $ Gender = "Male"
            jump male
        "Broya...":
            $ Gender = "Female"
            jump Female

label male:
    "pene"

label female:
    "ugh"


    return
