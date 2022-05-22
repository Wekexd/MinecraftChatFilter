import time
import os.path

global tryb
global costam


def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == "__main__":
    isdirexist = os.path.exists("chat")
    if not isdirexist:
        os.makedirs("chat", exist_ok=False)
    print("---------")
    print("0 - Filtracja uzytkownika")
    print("1 - Sprawdzanie czy gracz dropnal 633 (TRYHC)")
    print("2 - Wszystkie dropy (specjalne) (TRYHC)")
    print("---------")
    tryb = input("Wybierz tryb: ")
    if(tryb == "0"):
        costam = input("Wpisz filtracje: ")
    if(tryb == "1"):
        costam = "magiczny kilof"
    if(tryb == "2"):
        costam = "otworzył"
    nazwapliku = input("Wpisz nazwe pliku do ktorego ma byc zapisywany tekst (jezeli nie to enter nacisnij): ")
    if nazwapliku:
        pliczek = open("chat/"+nazwapliku+".txt","w+")
    logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
    loglines = follow(logfile)
    for line in loglines:
        if "[Client thread/INFO]: [CHAT]" in line:
            if costam.lower() in line.lower():
                strline = line[40:line.__len__()]
                print(strline)
                if nazwapliku:
                    pliczek.write(strline)
                    pliczek.flush()
