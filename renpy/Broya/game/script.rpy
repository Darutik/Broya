# BROYA (new try)
# Yandrak45 (2017)

#Characters
define pov = Character("[povname]")
define k = Character("Kevin")

#Resources
image maintitle = ""
image bg blank = ""

label start:

    #TITULO
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
    "Someone" "Hello."
    "You" "He-hello...?"
    "Someone" "Are you OK?"
    menu:
        "1. Yes...":
            "You" "Yes..."
            "Someone" "Sure?"
            "You" "Yes, I'm right..."
            python:
                povidiot = False
                povname = renpy.input("Someone: What's your name?")
                povname = povname.strip()
                if not povname:
                    povidiot = True
                    povname = "The player who didn't remember to write"
            pov "I'm... [povname].\nPeople call me [povname]..."
            "Someone" "Okay, [povname]. I'm Kevin, and I found you near the river, in the East.\nYou were unconcious, so I let you to rest on my house, inside the forest."
#YANDRAK45 LINE
        "2. Who are you?":
        "3. I'm dead...":

    return
