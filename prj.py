import random
ma_varbl=random.randint(0,100)
gess= int(input('entrez un chiffre:'))
deviner=0
while deviner==0:
        if ma_varbl<gess:
            gess=int(input('le nombre que vpous avez choisi et trés grand'))
        elif ma_varbl==gess:
            gess=int(input('Congts vous avez deviner le chiffre'))
            deviner=1
            print('le nombre que vpous avez choisi et trés petit')
        else:
             ma_varbl==gess
             gess=int(input('Congts vous avez deviner le chiffre'))
             deviner=1
#min et max 
maximum=int(input("Choisir la brone supperieur : "))
print("\nLes bornes que vous avez choisi sont ",minimum, "et", maximum ,".\n")
if maximum<minimum:
    print("Euh, ton max est inferieur a ton min...")
    print("Euh, ton max est inferieur a ton min...\n")
    idiot=1
#choix du "mode" de jeu (limite / illimite)
infinity_mode=0
print("Voulez vous jouer avec des nombres de tentatives limites ou illimites ?  \n")
print("Saisir 0 : tentatives limites (a 7 essaie) ")
print("Saisir 1 : tentatives illimites ")
choise_limit=int(input())

if choise_limit == 1:
    infinity_mode = 1
elif choise_limit == 0:
    infinity_mode = 0
else:
    print("Tu sais pas compter ? ")
if idiot == 0 :
    infinity_mode=0
    print("Voulez vous jouer avec des nombres de tentatives limites ou illimites ?  \n")
    print("Saisir 0 : tentatives limites (a 7 essaie) ")
    print("Saisir 1 : tentatives illimites ")
    choise_limit=int(input())

    if choise_limit == 1:
        infinity_mode = 1
    elif choise_limit == 0:
        infinity_mode = 0
    else:
        print("Tu sais pas compter ? ")


#generation du nombre a deviner
val_random = random.randint(minimum,maximum)

#premiere tentative
user_guess = int(input("Choisir un nombre : " ))
#generation du nombre a deviner
val_random = random.randint(minimum,maximum)

#premiere tentative
user_guess = int(input("Choisir un nombre : " ))
#generation du nombre a deviner
val_random = random.randint(minimum,maximum)

#premiere tentative
user_guess = int(input("Choisir un nombre : " ))

completed = 0 
try_numbre= 0

if infinity_mode == 1 :
    try_numbre = -999999
    completed = 0 
    try_numbre= 0

    if infinity_mode == 1 :
        try_numbre = -999999

while completed == 0 and try_numbre < 7: 
    if user_guess > val_random : 
        print("Essayer plus petit")
        user_guess = int(input("Choisir un autre nombre : " ))
        try_numbre= try_numbre+1

    elif user_guess < val_random : 
        print("Essayer plus grand")
        user_guess = int(input("Choisir un autre nombre : " ))
        try_numbre= try_numbre+1
    while completed == 0 and try_numbre < 7: 
        if user_guess > val_random : 
            print("Essayer plus petit")
            user_guess = int(input("Choisir un autre nombre : " ))
            try_numbre= try_numbre+1

        elif user_guess == val_random:
            print("Gagner !")
            completed = 1
            score_file = open("Score.txt", "w")
            content_file=content_file+1
            score_file.write(f"{content_file}")
            score_file.close()
        elif user_guess < val_random : 
            print("Essayer plus grand")
            user_guess = int(input("Choisir un autre nombre : " ))
            try_numbre= try_numbre+1

    if try_numbre == 7 : 
        print("Too bad, vous avez essayer beaucoup trop de fois, la prochaine essayer en moins de 7 essaies :) ")


        if  try_numbre == 7 : 
            print("Too bad, vous avez essayer beaucoup trop de fois, la prochaine essayer en moins de 7 essaies :) ")
