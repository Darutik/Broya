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
image maintitle = ""
image bg blank = ""
image kevin shadow = ""

label start:

    #TITULO
#KRONI LINE
    pause 1.0
    "Yandrak45 presents..."
    pause .5
    "01000010 01110010 01101111 01111001 01100001"
    pause .5
    "More known as..."
    scene maintitle
    with Dissolve(2.0)
    pause 3.0
    scene bg blank
    with Dissolve(1.0)

    #INTRO
    pause 3.0
    show kevin shadow
    with Dissolve(.5)
    pause .5
    "Someone" "Hello."
    pause .5
    "You" "He-hello...?"
    pause .5
    "Someone" "Are you OK?"
    pause .5
#YANDRAK45 LINE
    menu:
        "1. Yes...":
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
        "2. Who are you?":
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
        "3. I'm dead...":
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
            

    return
