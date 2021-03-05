import julkalib

# Domyślne odpowiedzi
julkaAnsw = ["GÓWNO INCELU", "ZAMKNIJ SIĘ INCELU", "MĘŻCZYŹNI NIE POWINNI MIEĆ PRAW", "O my God... Musze posłuchać KPOPu, wkurwiles mnie Incelu", "Jajcooo", "KAPITALIZM POWODUJE NIERÓWNOŚCIIII SOCJALIZM NAJLEPSZY!!!"]


julkalib.initConfig()

#-----------------------------#
# Przed prawidzwym rozpoczęciem
input("TY: ")
print("JULKA: Hej!")
#-----------------------------#

if julkalib.userCustomJulkaAnsw != None:
    if julkalib.randomizeAnsw == True:
        julkalib.randomResp(julkalib.userCustomJulkaAnsw, julkalib.loopedAnsw)
    else:
        julkalib.typicalResp(julkalib.userCustomJulkaAnsw, julkalib.loopedAnsw)
else:
    if julkalib.randomizeAnsw == True:
        julkalib.randomResp(julkaAnsw, julkalib.loopedAnsw)
    else:
        julkalib.typicalResp(julkaAnsw, julkalib.loopedAnsw)

print("Julka rozłączyła się...")
