# W tym pliku będą znajdować się ważne funkcje dotyczące
# Symulatora Julki. Zrobiłem to po to by nie zaśmiecać
# głównego pliku wykonywalnego.
import json


configFilePath = "./config.json"
loopedAnsw = False
randomizeAnsw = False
stoppingKeywords = None
userCustomJulkaAnsw = None


def initConfig():
    global configFilePath

    fetchCustomResp(configFilePath)
    fetchLoopedVar(configFilePath)
    fetchRandomizeRespVar(configFilePath)
    fetchStoppingKeywords(configFilePath)

# Jak sama nazwa wskazuje w tej funkcji
# brane są customowe odpowiedzi Julki
# napisane przez użytkowników.
def fetchCustomResp(configFilePath):
    global userCustomJulkaAnsw

    try:
        config = open(configFilePath, 'r')
    except:
        print("Coś poszło nie tak. Ścieżka do pliku konfiguracyjnego jest nieprawidłowa lub takowy plik nie istnieje.")
        return False
    
    configData = json.load(config)
    
    if configData["customRespStatus"] == True:
        print("'customRespStatus' w pliku konfiguracyjnym jest równy: True!")
        userCustomJulkaAnsw = configData["customResp"]

    print(f"DEBUG INFO: userCustomJulkaAnsw == {userCustomJulkaAnsw}")
    

    config.close()

    # Kiedy wszystko pójdzie OK to funckja zwróci 'True'.
    # Dzięki temu zapobiegnie to trywialnym błędom i
    # będe mógł sprawdzić czy rzeczywiście wszystko poszło
    # dobrze z planem.
    return True


def fetchLoopedVar(configFilePath):
    global loopedAnsw

    try:
        config = open(configFilePath, 'r')
    except:
        print("Coś poszło nie tak. Ścieżka do pliku konfiguracyjnego jest nieprawidłowa lub takowy plik nie istnieje.")
        return False
    
    configData = json.load(config)

    loopedAnsw = configData["looped"]

    print(f"DEBUG INFO: loopedAnsw == {loopedAnsw}")
    

    config.close()

    # Kiedy wszystko pójdzie OK to funckja zwróci 'True'.
    # Dzięki temu zapobiegnie to trywialnym błędom i
    # będe mógł sprawdzić czy rzeczywiście wszystko poszło
    # dobrze z planem.
    return True

def fetchRandomizeRespVar(configFilePath):
    global randomizeAnsw

    try:
        config = open(configFilePath, 'r')
    except:
        print("Coś poszło nie tak. Ścieżka do pliku konfiguracyjnego jest nieprawidłowa lub takowy plik nie istnieje.")
        return False
    
    configData = json.load(config)

    randomizeAnsw = configData["randomizeResp"]

    print(f"DEBUG INFO: randomizeAnsw == {randomizeAnsw}")
    

    config.close()

    # Kiedy wszystko pójdzie OK to funckja zwróci 'True'.
    # Dzięki temu zapobiegnie to trywialnym błędom i
    # będe mógł sprawdzić czy rzeczywiście wszystko poszło
    # dobrze z planem.
    return True


def fetchStoppingKeywords(configFilePath):
    global stoppingKeywords

    try:
        config = open(configFilePath, 'r')
    except:
        print("Coś poszło nie tak. Ścieżka do pliku konfiguracyjnego jest nieprawidłowa lub takowy plik nie istnieje.")
        return False
    
    configData = json.load(config)

    stoppingKeywords = configData["stoppingKeywords"]

    print(f"DEBUG INFO: stoppingKeywords == {stoppingKeywords}")
    

    config.close()

    # Kiedy wszystko pójdzie OK to funckja zwróci 'True'.
    # Dzięki temu zapobiegnie to trywialnym błędom i
    # będe mógł sprawdzić czy rzeczywiście wszystko poszło
    # dobrze z planem.
    return True



# Funkcja wypluwająca z siebie losowo
# wybierane odpowiedzi aniżeli chodząca
# po kolei po tablicy.
#
# Zmienna 'actualJulkaAnsw' jest po to
# żeby funkcja wiedziała jaką aktualnie
# używa tablice do odpowiedzi Julki.
def randomResp(actualJulkaAnsw, looped=False):
    from random import randint

    actualJulkaAnswRNG = actualJulkaAnsw

    if looped == True:
        while True:
            actualRandNum = randint(0, (len(actualJulkaAnsw)-1))

            userInput = input("TY: ")

            if userInput in stoppingKeywords:
                break
            
            print("JULKA:", actualJulkaAnsw[actualRandNum])
    else:
        while True:
            if len(actualJulkaAnswRNG) <= 0:
                break

            actualRandNum = randint(0, (len(actualJulkaAnswRNG)-1))

            userInput = input("TY: ")

            if userInput in stoppingKeywords:
                break

            print("JULKA:", actualJulkaAnswRNG[actualRandNum])

            actualJulkaAnswRNG.pop(actualRandNum)

    
# Podobnie jak w przypadku funkcji 'randomResp',
# ale cóż... bez losowości.
def typicalResp(actualJulkaAnsw, looped=False):
    if looped == True:
        i = 0
    
        while True:
            if i < len(actualJulkaAnsw):
                userInput = input("TY: ")

                if userInput in stoppingKeywords:
                    break

                print("JULKA:", actualJulkaAnsw[i])

                i += 1
            else:
                i = 0
    else:
        for i in range(len(actualJulkaAnsw)):
            userInput = input("TY: ")

            if userInput in stoppingKeywords:
                break

            print("JULKA:", actualJulkaAnsw[i])
