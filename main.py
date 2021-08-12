print("Determination d'une année bissextile")
print("")
print("       ****************************************************    ")

number = int (input ("        Entrér une année et je vous dirai si elle est bissextile ou pas.\n    "))

if number % 4 != 0:
     print("L'annee n'est pas bissextile.")
elif number % 4 == 0 and number % 100 == 0:
    if number % 400 == 0:
        print("L'année est bissextile")
    else:
          print("L'année n'est pas bissextile.")
else: 
    print(" L*année est bissextile")
print("je vous remercie d'avoir participer á ce mini jeu.")
