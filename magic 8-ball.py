import random
while True:
    question=input("Ask the magic 8 ball a question: (press enter to quit) ")
    answer=random.randint(1,20)
    if question=="":
        print("Stopping the Game.")
        break
    if answer==1:
        print("For sure.")
    elif answer==2:
        print("For sure, no doubt.")
    elif answer==3:
        print("For sure, no cap.")
    elif answer==4:
        print("For sure, 100%.")
    elif answer==5:
        print("totes trust that, fam.")
    elif answer==6:
        print("Yasss, totally!")
    elif answer==7:
        print("Probz.")
    elif answer==8:
        print("Looking solid.")
    elif answer==9:
        print("Yas.")
    elif answer==10:
        print("The vibes are positive.")
    elif answer==11:
        print("bruh, not sure what you're saying. Try again.")
    elif answer==12:
        print("Try again later, fam.")
    elif answer==13:
        print("Nah, can't spill the tea just yet.")
    elif answer==14:
        print("idk rn.")
    elif answer==15:
        print("Focus and hit me back up later.")
    elif answer==16:
        print("Don't bet on it, fam.")
    elif answer==17:
        print("Nah, not happening.")
    elif answer==18:
        print("My vibes are telling me nah.")
    elif answer==19:
        print("Not looking good, fam.")
    elif answer==20:
        print("Major cap, frfr")