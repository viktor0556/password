felhasznalo_nev = ""
jelszó = ""
pinkód = 9031

Próba = 3

while True:
    fiók = input("Létezik már fiókod? (igen/nem): ")


    if fiók.lower() == "nem":
        felhasznalo_nev += input("Válassz felhasználónevet: ")
        jelszó += input("Válassz jelszót: ")
    elif fiók.lower() == "nem":
        print("Helytelen (igen/nem)-et használj")
    if fiók == "igen":
        felhasznalo_nev1 = input("Add meg a felhasználóneved: ")
        jelszó1 = input("Add meg a jelszvad: ") 
        if felhasznalo_nev == felhasznalo_nev1 and jelszó == jelszó1:
            print("Sikeres bejelentkezés")
            break


        else:
           print(f"Hibás jelszó vagy felhasználónév, próbáld újra. Ennyi próbálkozásod van még: {Próba} ")
        Próba -= 1
        if  Próba < 0:
            print("RENDSZER LEZÁRVA")
            pinkód1 = int(input("Írja be a pinkódot vagy ezesetben le lesz tiltva!: "))
            if pinkód1 == pinkód:
                print("Sikeres Belépés!")
            else:
                print("Letiltva!")
            break


  
            




