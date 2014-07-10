import sys

Ans = ""
Name = ""
XBucle = False

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
Ans = raw_input("==> ")
while (XBucle != True):
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
        print " How I call you?"
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
        print " So, how I should call you, ghost? Casper???"
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
