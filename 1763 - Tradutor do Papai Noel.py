paises = dict()
paises["brasil"] = "Feliz Natal!"
paises["alemanha"] = "Frohliche Weihnachten!"
paises["austria"] = "Frohe Weihnacht!"
paises["coreia"] = "Chuk Sung Tan!"
paises["espanha"] = "Feliz Navidad!"
paises["grecia"] = "Kala Christougena!"
paises["estados-unidos"] = "Merry Christmas!"
paises["inglaterra"] = "Merry Christmas!"
paises["australia"] = "Merry Christmas!"
paises["portugal"] = "Feliz Natal!"
paises["suecia"] = "God Jul!"
paises["turquia"] = "Mutlu Noeller"
paises["argentina"] = "Feliz Navidad!"
paises["chile"] = "Feliz Navidad!"
paises["mexico"] = "Feliz Navidad!"
paises["antardida"] = "Merry Christmas!"
paises["canada"] = "Merry Christmas!"
paises["irlanda"] = "Nollaig Shona Dhuit!"
paises["belgica"] = "Zalig Kerstfeest!"
paises["italia"] = "Buon Natale!"
paises["libia"] = "Buon Natale!"
paises["siria"] = "Milad Mubarak!"
paises["marrocos"] = "Milad Mubarak!"
paises["japao"] = "Merii Kurisumasu!"

while True:
    try:
        pais = str(input())
        print(paises[pais])
    except KeyError:
        print("--- NOT FOUND ---")
    except:
        break
