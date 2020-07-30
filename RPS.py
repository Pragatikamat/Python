from random import randint

moves = ["Rock", "Paper", "Scissors"]
cm = moves[randint(0, 2)]
cs = 0
ps = 0
rounds = int(input("How many rounds?"))

while (rounds != 0):

    pm = input("which one?")
    print("Comp puts", cm)
    if cm == "Rock" and pm == "Paper":
        ps = ps+1
    elif cm == "Rock" and pm == "Scissors":
        cs = cs+1
    elif cm == "Paper" and pm == "Scissors":
        ps = ps+1
    elif cm == "Paper" and pm == "Rock":
        cs = cs+1
    elif cm == "Scissors" and pm == "Rock":
        ps = ps+1
    elif cm == "Scissors" and pm == "Paper":
        cs = cs+1
    print("your score:", ps)
    print("Comp's score:", cs)
    rounds = rounds-1
