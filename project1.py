#project manager, umoznuje pridavat a mazat ukoly a zobrazit seznam, 
# chybove vstupy by mely byt osetreny, aby program vzdy vedel, co delat
ukoly = []

def pridat_ukol ():
#fce umoznuje pridat ukoly na seznam, bez ohledu na to, jestli je plny nebo prazdny    
    nazev_ukolu = input(f"Zadejte název úkolu: ")
    while len(nazev_ukolu) == 0:
    #smycka bezi dokud nedostane platny vstup
        nazev_ukolu = input(f"Zadejte název úkolu: ")
          
    popis_ukolu = input (f"Zadejte popis úkolu: ")
    while len(popis_ukolu) == 0:
    #smycka bezi dokud nedostane platny vstup
        popis_ukolu = input (f"Zadejte popis úkolu: ")
   
    print (f"Úkol: {nazev_ukolu} byl přidán.")
    #vypise hlasku o pridani a ukol spolu s popisem uklada na konec seznamu  
    nazev_ukolu = " - ".join([nazev_ukolu,popis_ukolu])
    ukoly.append(nazev_ukolu)

def zobrazit_ukoly ():
#umoznuje zobrazit ukoly, pokud nejake jsou, pokud ne, vraci upozorneni
    if len(ukoly) != 0:
        print ("Seznam úkolů:")
        for ukol in ukoly:
            poradi = ukoly.index(ukol)+1
            print (f"{poradi}. {ukol}") 
    else:
        print("Seznam je prázdný.")

def odstranit_ukol (): 
#maze ukol ze seznamu, pokud tam nejaky je
    while True:
        #podminka while overuje, jestli zadana hodnota je cislo, pokud ne, vetev except vrati chybu a jede na start fce
        if len(ukoly) != 0:
        #podminka kontroluje jestli je na seznamu alespon jeden ukol, pokud ano, tiskne seznam 
        #a pta se, co smazat a vstup se predava na vetev try
            print ("\nSeznam úkolů:")
            for ukol in ukoly:
                print (f"{ukoly.index(ukol)+1}. {ukol}") 
            mazany_ukol = input("Zadejte číslo úkolu, který chcete odstranit: \n")
            
        else:
        #pokud je seznam prazdny pise hlasku a vraci se na hlavni menu
            print ("Seznam je prázdný. ")
            break
        try: 
        #pokud je zadana hodnota cislo, smycka try ho prevede ze str na int    
            mazany_ukol = int(mazany_ukol)   
            while mazany_ukol > len(ukoly):
            #pokud hodnota mazaneho presahuje delku seznamu ukolu, fce si vyzada zadani cisla ze seznamu, 
            #vraci se na start fce pro novy input
                print ("\nVyber úkol na seznamu! ")
                break                 
            while mazany_ukol <= 0 :
            #pokud hodnota mazaneho prvku je mensi nez nula vcetne, vraci se na zacatek fce pro novy input
                print ("\nNepovolené hodnoty, vyberte číslo ze seznamu! ")
                break

            if (mazany_ukol <= len(ukoly)) and (mazany_ukol > 0):
            #pokud mazany ukol je na seznamu, odstrani ukol na danem indexu, vypise potvrzeni o odstraneni ukolu
            #a konci funkci, vrací se na hlavni menu                           
                odebrany = str(ukoly.pop(mazany_ukol-1)) 
                #určí index mazaneho ukolu podle cisla seznamu -1, vrati hodnotu ukolu, 
                #split pak oseka o popis a vypise jen nazev ukolu           
                print (f"\nÚkol {odebrany.split(" - ")[0]} byl odstraněn.")
                return
            
        except ValueError:
            #pokud je zadany jiny znak nez cislo, vraci chybovou hlasku, jde na strart fce pro novy input
            print ("Musíte zadat číslo! ")                


def hlavni_menu ():       
#fce bezi dokud neni ukoncena, platne vstupy postupuji do dalsich funkci, neplatne vraci dotaz na opravu vstupu        
    while True:
        print ("\nSprávce úkolů - hlavní menu:\n 1. Přidat nový úkol\n 2. Zobrazit všechny úkoly\n 3. Odstranit úkol \n 4. Konec programu")
        volba = input("\nVyberte možnost 1. - 4.: \n")
        try:
            volba = int(volba)
            
            if volba == 1:
                pridat_ukol ()
            elif volba == 2:
                zobrazit_ukoly ()
            elif volba == 3:
                odstranit_ukol ()
            elif volba == 4:
                print ("Konec programu.")
                return                    
            elif (0 >= volba) or (volba > 4):
                print ("\nVyberte si možnost z menu. ")
                
        except ValueError:
            print ("\nMusíte zadat číslo! ")
                


hlavni_menu ()