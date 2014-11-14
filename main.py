import sys

Ans = ""
Name = ""
Genre = ""
XBucle = False

print ""
print " BROYA by Darutik"
print " prerelease A (prA)"
print ""
print " It's not complete, so I deleted the unfinished answers."
print " If you don't like SPOILERS, you should close now..."
raw_input()

print ""
print " Darutik presents..."
print ""
print " 01000010 01110010 01101111 01111001 01100001"
print " More knowed as..."
print ""
print ""
print ""
print " :::::::::  :::::::::   ::::::::  :::   :::   :::     "
print " :+:    :+: :+:    :+: :+:    :+: :+:   :+: :+: :+:   "
print " +:+    +:+ +:+    +:+ +:+    +:+  +:+ +:+ +:+   +:+  "
print " +#++:++#+  +#++:++#:  +#+    +:+   +#++: +#++:++#++: "
print " +#+    +#+ +#+    +#+ +#+    +#+    +#+  +#+     +#+ "
print " #+#    #+# #+#    #+# #+#    #+#    #+#  #+#     #+# "
print " #########  ###    ###  ########     ###  ###     ### "
print ""
print ""
print ""
raw_input("")
print " When something like ==> apear, you must select a number."
raw_input("")
print ""

print ""
print " SOMEONE:"
print " Hello."
raw_input("")
print " YOU:"
print " He-hello...?"
raw_input("")
print "SOMEONE:"
print " Are you OK?"
print ""
print " 1. Yes..."
print " 2. Who are you?"
print " 3. I'm dead..."
while (XBucle != True):
    Ans = raw_input("==> ")
    if Ans == "1":
        print " YOU:"
        print " Yes..."
        raw_input("")
        print " SOMEONE:"
        print " Sure?"
        raw_input("")
        print " YOU:"
        print " Yes, I'm right..."
        raw_input("")
        print " SOMEONE:"
        print " What's your name?"
        Name = raw_input("==> ")
        print " " + Name + ":"
        print " I'm... " + Name + "."
        print " People call me " + Name + "..."
        raw_input("")
        print " SOMEONE:"
        print " Okay, " + Name + ". I'm Kevin, and I found you near the river, in the East."
        print " You were unconscious, so I let you in my house, inside the forest."
        XBucle = True
    elif Ans == "2":
        print " YOU:"
        print " Who are you?"
        raw_input("")
        print " SOMEONE:"
        print " I'm Kevin. I found you near the river, in the East."
        print " You were unconscious, so I let you in my house, inside the forest."
        raw_input("")
        print " KEVIN:"
        print " So, you got it. Now let me ask you..."
        print " How should I call you?"
        Name = raw_input("==> ")
        print " " + Name + ":"
        print " I'm... " + Name + "."
        print " People call me " + Name + "..."
        XBucle = True
    elif Ans == "3":
        print " YOU:"
        print " I'm dead..."
        raw_input("")
        print " SOMEONE:"
        print " Yes, and I am Bill Gates."
        print " So, how should I call you, ghost? Casper???"
        Name = raw_input("==> ")
        print " " + Name + ":"
        print " I'm not Casper. I'm " + Name + "."
        raw_input("")
        print " SOMEONE:"
        print " Sorry, " + Name + ", I'm not Bill Gates too."
        raw_input("")
        print " SOMEONE:"
        print " I'm Kevin. I found you near the river, in the East."
        print " You were unconscious, so I let you in my house, inside the forest."
        XBucle = True
    else:
        print " SYSTEM:"
        print " I don't like what you are saying..."
        raw_input("")
        XBucle = False
XBucle = False
raw_input("")
print " " + Name + " and Kevin are in a bedroom of the house of Kevin."
print " The walls of the room are colored with blue colors."
print " " + Name + " is lying in the white bed. His backpack is placed in an empty desk wich have a classical lamp."
print " Kevin is sitting near " + Name + " in the same bed."
raw_input("")
print " " + Name + ":"
print " My backpack..."
raw_input("")
print " Kevin gived the Backpack to " + Name + "."
raw_input("")
print " " + Name + ":"
print " Wait."
raw_input("")
print " " + Name + ":"
print " I didn't have any backpack..."
raw_input("")
print " There is a tag with the name of someone in the backpack."
raw_input("")
print " KEVIN:"
print " Who is Broya?"
raw_input("")
print " " + Name + ":"
print " Broya..."
raw_input("")
print " " + Name + ":"
print " When you find me..."
raw_input("")
print " " + Name + ":"
print " ...I was alone?"
print " There aren't anyone more outside?"
raw_input("")
print " KEVIN:"
print " I didn't find any more than you and this backpack."
print " But..."
raw_input("")
print " KEVIN:"
print " Who is Broya???"
print ""
print " 1. Broya..."
print " 2. Broya..."
while (XBucle != True):
    Ans = raw_input("==> ")
    if Ans == "1":
        Genre = "Male"
        print " " + Name + ":"
        print " Broya..."
        print " Broya is my friend..."
        raw_input("")
        print " KEVIN:"
        print " He was with you?"
        raw_input("")
        print " " + Name + ":"
        print " Let me think..."
        raw_input("")
        print " " + Name + ":"
        print " Yes..."
        print " He was with me..."
        raw_input("")
        print " " + Name + ":"
        print " I must help him!!!"
        raw_input("")
        print " KEVIN:"
        print " (Stopping " + Name + ")"
        print " Not now!"
        raw_input("")
        print " KEVIN:"
        print " It's dark outside, and you aren't ready for the dangers."
        print " Too dangerous for you now..."
        raw_input("")
        print " " + Name + ":"
        print " ..."
        raw_input("")
        print " KEVIN:"
        print " You can search him tomorrow."
        print " He'll be ok..."
        raw_input("")
        print ""
        print " " + Name + " is sleeping, when a computer sound wake him..."
        print ""
        raw_input("")
        print ""
        print " " + Name + ":"
        print " What..."
        print " What's this?"
        raw_input("")
        print ""
        print " ..."
        raw_input("")
        print ""
        print " ..."
        raw_input("")
        print ""
        print " " + Name +":"
        print " What should I do now?"
        print ""
        print " 1. Ignore it and sleep."
        print " 2. Go and see what's up there."
        print " 3. Sing a song loudly."
        while (XBucle != True):
            Ans = raw_input("==> ")
            if Ans == "1":
                print ""
                print " " + Name + ":"
                print " I should be sleeping."
                print " I need energy to find Broya tomorrow..."
                raw_input("")
                print ""
                print " " + Name + " go back to the bed, and close his eyes."
                raw_input("")
                print "..."
                raw_input("")
                print "..."
                raw_input("")
                print "..."
                raw_input("")
                print ""
                print " KEVIN:"
                print " Uf..."
                raw_input("")
                print ""
                print " KEVIN:"
                print " This was close..."
                XBucle = True
            elif Ans == "2":
                print "NO WAY"
                XBucle = False
            elif Ans == "3":
                print ""
                print " " + Name + ":"
                print " Para bailar la bamba!!!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Para bailar la bamba!"
                print " Se necesita"
                print " Una poca de gracia!!!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " Urg..."
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Una poca de gracia!"
                print " Pa mi pa ti"
                print " Ay y arriba y arriba!!!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " WTF?!!!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Yo no soy marinero!!!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " What are you doing???!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Yo no soy marinero!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " SHUT UP!!!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " ..."
                raw_input("")
                print "UNFINISHED"
                print " Here is a small jump in the story, because  think you wanted to hear " + Name + " singing..."
                XBucle = True
            else:
                print " SYSTEM:"
                print " I don't like what you are saying..."
                raw_input("")
                XBucle = False
        raw_input("")
        print ""
        raw_input("")
        print ""
        print " In the next day, " + Name + " and Kevin wake up."
        raw_input("")
        print ""
        print " As Kevin prepare the breakfast, " + Name + " wanted to ask somthing to him."
        raw_input("")
        print ""
        print " 1. What's out there, in the forest?"
        print " 2. Do you know how to touch a wall with an apple?"
        print " 3. Did you listen a strangle sound at night?"
        while (XBucle != True):
            Ans = raw_input("==> ")
            if Ans == "1":
                print ""
                print " " + Name + ":"
                print " What's out there, in the forest?"
                raw_input("")
                print "NO WAY"
                XBucle = True
            elif Ans == "2":
                print ""
                print " " + Name + ":"
                print " Do you know how to touch a wall with an apple?"
                raw_input("")
                print "NO WAY"
                XBucle = True
            elif Ans == "3":
                print ""
                print " " + Name + ":"
                print " Did you listen a strangle sound at night?"
                raw_input("")
                print "NO WAY"
                XBucle = True
            else:
                print " SYSTEM:"
                print " I don't like what you are saying..."
                raw_input("")
                XBucle = False
        XBucle = True
    elif Ans == "2":
        print "NO WAY"
        XBucle = False
    else:
        print " SYSTEM:"
        print " I don't like what you are saying..."
        raw_input("")
        XBucle = False
XBucle = False
raw_input("")
print "DEADLINE"
print "The code ends here..."
raw_input("")
