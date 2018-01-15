#Faccio fuori tutti i links che mi fan morire il bot
for k in c:
    #if k == 'http://www.hotnewsbreak.net/shameless-eu-politicians-will-veto-brexit-deal-if-uk-better-off-leaving-than-remaining/':
    if re.sub(r'http%', '', k):
       s=c.index(k)
       print(s)

       del c[s]


    #
    # elif k == 'http://thisisengland.org.uk/brexit-u-turn-video-bank-of-england-boss-says-europe-needs-to-fear-exit-as-uk-risk-subsides/':
    #     s = c.index(k)
    #     print(s)
    #     del c[s]
    # elif k == 'http://newschicken.com/eu-facing-bitter-reality-of-uk-exit-german-chief-says-soft-brexit-is-not-an-option/':
    #     s = c.index(k)
    #     print(s)
    #     del c[s]




       ###########Questo Metodo non è valido


       var2 = list()
       var2 = list(set(lnotr) - set(urls2))

       var3 = list()
       var3 = list(set(var2) - set(urls2))



m=list()
with open('C:/Users/mi.bellini/Desktop/tutorial/tutorial/entry.csv', "r", encoding="utf-8") as inputfile:
        for line in inputfile:
            #lines = re.sub(r'"""""""', '', line)
            #linesfin = re.sub(r'"".*', '', lines)
            m.append(lines.strip())

m[50]


###Modifica il file in out eliminando "




urls2=list()
with open('C:/Users/mi.bellini/Desktop/tutorial/tutorial/ris.json',"r", encoding="utf-8") as inputfile:
    for line in inputfile:
        lines = re.sub(r'.*RL": "','',line)
        lines = re.sub(r'".*','',lines)
        linefin = re.sub(r'%0A.*','',lines)
        urls2.append(linefin.strip())



#Scrivo il File come CSV

df = pd.DataFrame(urls2)
print(df.to_csv('prova2.csv',encoding='utf-8',index=False, header=False))

##############################################

#Apro il file dei risultati




# Elimino i sottocampi che non presentano i campi di selezione



#creo l'output file
#with open("Giro2.txt", "w", encoding="utf-8") as output:
 #   output.write(str(lnotr))
##



##Il file lo modifico manualmente, ovvero elimino manualmente le virgolette

# linesfin = re.sub(r'"".*', '', lines)

#reader = csv.reader(inputfile,delimiter=',')



###qui ottengo i links che sono ancora presenti in m privati da tutti i risultati
##no ngenerati dal bot in redirect
#Questa lista la rilancio: i links che sono redirect li estraggo dal log file.Quando il log file è abbastanza
#limitato per avere dei risultati decenti
#Alcuni elementi sono frutto della redirection: quindi in realtà non sono derivanti dalle sorgenti, rappresentano
#dei links in più che non sono presenti nell'originale.

#Invertendo i termini: ottengo solo i redirect.
#Essi possono essere estratti ed eliminati dalla lista di risultato del bot





#Sottoinsieme dei risultati tolti tutti i redirect

#var3=list(set(urls)-set(var2))
#len(var3)


###Rimuovo twitter selezionando la sola sottostringa,ignorando prima e dopo
##Da sistemare

with open('C:/Users/Administrator/Desktop/tutorial/domini.csv', "w", encoding="utf-8") as fileinput:
    for lix in urlsbb :
        urlsbb.append(lix.strip())


match = [k for k in urls6 if "twitter" in k]
s = urls6.index(match)
print(s)
del urls6[s]
