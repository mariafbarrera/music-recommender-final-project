# MVP: Music Recommender

print("What type of music genre do you like?")
print("")
print("")
print("Choose a number, based on what you like!")
user_choice = input('''
    1. Hip Hop
    2. Rock
    3. Pop 
    4. Jazz 
    5. Classic 
    6. K-pop
    7. Country 
    8. Electronic
    ''')

if user_choice == "1":
    print("I would suggest to listen to:")
    print("")
    print("Started From The Bottom - Drake")
elif user_choice == "2":
    print("Why don't you listen to this?")
    print("")
    print("Don't Stop Believin - Journey ")
elif user_choice == "3":
    print("I know you will like this song:")
    print("")
    print("Feeling Good - Michael Bublé")
elif user_choice == "4":
    print("This a nice song!:")
    print("")
    print("The Girl From Ipanema - Stan Getz & Joao Gilberto ")
elif user_choice == "5":
    print("Have you listened to this song?")
    print("")
    print("Gramophone Waltz - Eugen Doga")
elif user_choice == "6":
    print("You may want to dance to this one!")
    print("")
    print("How You Like That - BLACKPINK")
elif user_choice == "7":
    print("You may like this one:")
    print("")
    print("Wagon Wheel - Darius Rucker")
elif user_choice == "8":
    print("What about this one?")
    print("")
    print("Animals - Martin Garrix")
else:
    print("I don't think that is an option...")