from datetime import datetime , timedelta
import matplotlib.pyplot as plt


def Converter(string):
    li = list(string.split(';'))
    return li


rune_tid = []                   #Lager de forskjellige listene som skal brukes 
rune_tid_start = []
rune_trykk = []
rune_absolutt_trykk = []
rune_temperatur = []
sola_tid = []
sola_temperatur = []
sola_trykk = []
sola_super_liste = []
fortsetter = True
with open("trykk_og_temperaturlogg_rune_time.csv.txt" , encoding="UTF-8") as Andre_data:
    next (Andre_data)
    while (fortsetter == True):    
        try:
            for a in Andre_data: 
                a = a.replace("," , ".")       #Legger den relevante infoen i egene lister
                splitter = Converter(a)
                rune_tid.append(splitter[0])
                rune_tid_start.append(splitter[1])
                if splitter[2] == "":
                    rune_trykk.append(rune_trykk[-1])
                else:
                    rune_trykk.append(float(splitter[2])*10)
                rune_absolutt_trykk.append(float(splitter[3])*10)
                rune_temperatur.append(float(splitter[4]))
            fortsetter = False
        except:
                ValueError
                print("hihi")
fortsetter = True
with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt" , encoding="UTF-8") as Sola_data:
    next (Sola_data)
    while (fortsetter == True):    
        try:
            for a in Sola_data :
                a = a.replace("," , ".")
                splitter = Converter(a)
                splitter[4] = splitter[4].replace ("\n" ,' ')
                sola_tid.append((datetime.strptime(splitter[2],"%d.%m.%Y %H:%M")))
                sola_temperatur.append(float(splitter[3]))
                sola_trykk.append(float(splitter[4]))
            fortsetter = False
        except:
                ValueError
                break
                print("hoho")
i = 0
fortsetter = True
while fortsetter == True:                   #Fikser tidsformat fo
    try:
        for a in rune_tid: 
            if rune_tid[i].find("am") != -1:
                rune_tid[i] = datetime.strptime(a,"%m/%d/%Y %H:%M:%S %p")
                i = i + 1
            elif rune_tid[i].find("pm") != -1:
                rune_tid[i] = datetime.strptime(a,"%m/%d/%Y %H:%M:%S %p")
                if rune_tid[i].hour != 12:
                    rune_tid[i] = rune_tid[i] +timedelta(hours = 12)
                i = i + 1
            else:
                rune_tid[i] = datetime.strptime(a,"%m.%d.%Y %H:%M")
                i = i + 1
        fortsetter = False
    except:
        ValueError
        print(i)
        break

"""
 den første fila er det en god del svingninger som representerer støy i temperaturmålingene.
For å redusere dette så regner man ofte ut et gjennomsnitt av flere temperaturer og plotter
det. Lag en funksjon som tar inn et liste med tider, ei liste med temperaturer, og et tall n som
sier hvor mange verdier den skal regne ut gjennomsnittet for.

For hvert gyldig tidspunkt skal
den regne ut snittet av de n forrige målingene, den nåværende målingen, og de n neste
målingene. Gyldige tidspunkter er alle tidspunkter hvor du ikke havner utenfor lista ved å gå n
hakk bakover eller forover. Så skal funksjonen returnere lister med gyldige tidspunkter og
gjennomsnittsverdier. Plott gjennomsnittsverdiene for n=30 i samme plott som for
temperatur. Dette gir den oransje linja i øverste plott.
"""
ax = plt.subplot(2,1,1)
plt.plot(sola_tid , sola_temperatur , label = "Sola temperatur" )
plt.plot(rune_tid,rune_temperatur, label ="Temperatur")
plt.legend()

ax = plt.subplot(2,1,2)
plt.plot(rune_tid, rune_absolutt_trykk , label = "Absolutt trykk")
plt.plot(rune_tid, rune_trykk , label = "Barometrisk trykk")
plt.plot(sola_tid , sola_trykk , label ="Absolutt trykk MET")
plt.locator_params(axis='y', nbins=9)
plt.legend()

plt.xlabel("Tid")

plt.show()
    
    
    
    
    
