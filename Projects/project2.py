print(r".eeeeee.eee......eee..eeeeee..eeeeeee..eeeeeeeee.eeeeeee..eeeeee..eeeeee..eeeeee....eeeeeeeee.eeeeee..eeeeee.eeeeeeeee.")
print(r"@@@@@@@:@@@@::::@@@@:@@@@@@@@:@@@@@@@@:@@@@@@@@@:@@@@@@@@:@@@@@@:@@@@@@@:@@@@@@@::::@@@@@@@@@:@@@@@@:@@@@@@@:@@@@@@@@@:")
print(r"%%%-----%%%%%--%%%%%-%%%--%%%-%%%--%%%----%%%----%%%--%%%-%%%----%%%-----%%%-----------%%%----%%%----%%%--------%%%----")
print(r"&&&&&&++&&&&&&&&&&&&+&&&&&&&&+&&&&&&&+++++&&&++++&&&++&&&+&&&&&++&&&&&&++&&&&&&++++++++&&&++++&&&&&++&&&&&&+++++&&&++++")
print(r"*||||||*|||*||||*|||*||||||||*||||||******|||****|||**|||*|||||***||||||**||||||*******|||****|||||***||||||****|||****")
print(r"====!!!=!!!==!!==!!!=!!!==!!!=!!!=!!!=====!!!====!!!==!!!=!!!========!!!=====!!!=======!!!====!!!========!!!====!!!====")
print(r":::::::#:::######:::#:::##:::#:::##:::####:::####:::##:::#::::::#:::::::#:::::::#######:::####::::::#:::::::####:::####")
print(r"......@@...@@@@@@...@...@@...@...@@...@@@@...@@@@...@@...@......@......@@......@@@@@@@@...@@@@......@......@@@@@...@@@@")
print(r"")

smarter = 0
dumber = 0
stupid = 0
answer1 = input ("What planet is closest to the Sun? Venus A, Earth B, Neptune C, Mercury D: ")
if answer1 == "D":
    smarter += 1
elif answer1 == "A": 
    print("wrong")
    dumber += 1
elif answer1 == "C": 
    print("wrong")
    dumber += 2
elif answer1 == "B": 
    print("wrong")
    dumber +=1
answer2 = input ("What is the cube root of eight? 4 A, 2 B, 8 C, 1 D: ")
if answer2 == "B":
    smarter += 2
elif answer2 == "A": 
    print("wrong")
    dumber += 1
elif answer2 == "C": 
    print("wrong")
    dumber += 1
elif answer2 == "D": 
    print("wrong")
    dumber +=2
answer3 = input ("who was the first president of the US? Glorp A, Michael Jackson B, Thomas Jefferson C, George Washington D: ")
if answer3 == "D":
    smarter += 1
elif answer3 == "A": 
    print("wrong")
    dumber += 1
elif answer3 == "C": 
    print("wrong")
    dumber += 2
elif answer3 == "B": 
    print("wrong")
    stupid +=100
answer4 = input ("When did columbus arrive in america? Yesterday A, 1492 B, 1521 C, none of them D: ")
if answer4 == "A" 'or' "B" 'or' "C":
        print("trick question")
        dumber += 10
elif answer4 == "D":
    smarter += 10  
  
if smarter > dumber and smarter > stupid:
    print("you are smarter than a fifth grader")
if dumber > smarter and dumber > stupid:
    print("you are not smarter than a fifth grader")
if stupid > dumber and smarter < stupid:
    print("you are not smarter than a fifth grader")
answer5 = input ("you want to retry? y/n")
if answer5 == "y":
    print("than do it")
if answer5 == "n":
    print("you dont have to")