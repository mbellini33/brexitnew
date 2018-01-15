import re
import pandas as pd
import requests

#Importo il Json Modificato e creo la seconda lista
urls = list()

with open('C:/Users/Administrator/Desktop/ris1d3.json',"r", encoding="utf-8") as inputfile:
    for line in inputfile:
        lines = re.sub(r'.*": "','',line)
        linesfin = re.sub(r'".*','',lines)
        urls.append(linesfin.strip())

del urls[0]
del urls[-1]
#Visualizzazione del file


print(dff.to_csv('urls.csv', encoding='utf-8', sep=',', index=False, header=False))


m=list()
with open('C:/Users/Administrator/Desktop/PythonProject/tutorial/DatiTesiFinal/entry1d3.csv', "r", encoding="utf-8") as inputfile:
    for liss in inputfile:
         m.append(liss.strip())
#################################################CRAWLER CON SCRAPY######################################################
###Calcolo le differenze tra i due files: ovvero i links che non sono contenuti nel file ma neanche coloro che sono risultati di redirect

lnotr=list()
lnotr=list(set(m)-set(urls)) #Il set cambia poco la numerica


len(lnotr)
len(m)
len(urls)

#Dopo questa operazione stampo in un file csv, anche se ho delle entrate doppie: le ricopio nel file e eliminerò i risultati doppi

####ELABORAZIONE SECONDI GIRI (RIMANE IDENTICO PER TUTTI)
df = pd.DataFrame(lnotr)
print(df.to_csv('entry1d3GIRO2.csv',encoding='utf-8',sep=',',index=False, header=False))

################################################################




urls4=list()


with open('C:/Users/Administrator/Desktop/PythonProject/tutorial/ris.json',"r", encoding="utf-8") as inputfile:
    for line in inputfile:
        riga = re.sub(r'.*RL": "', '', line)
        righe = re.sub(r'".*', '', riga)
        urls4.append(righe.strip())


urls5 = list()


with open('C:/Users/Administrator/Desktop/PythonProject/tutorial/ris.json', "r", encoding="utf-8") as fileinput:
    for linesss in fileinput:
            linessss = re.sub(r'.*us": ', '', linesss)
            linesssss = re.sub(r'}.*', '', linessss)
            urls5.append(linesssss.strip())


########Cambio la sottoselezione dei risultati

df = pd.DataFrame(list(zip(urls4,urls5)),
                  columns=['link','status'])


#Seleziono la prima riga
df.iloc[47264]

#N di righe
g=47269

#eliminazione della prima e dell'ultima riga
df.drop(df.index[[0]])

df.iloc[0]


#Seleziono unicamente i casi in cui ho uno status pari a 200



df2=df.loc[df['status'] == '200']

#Selezioni i domini dei links,
urls6=list()
df3= df.iloc[:,0]
for righe in df3:
    rigs = re.sub(r'.*://', '', righe)
    rigss = re.sub(r'/.*', '', rigs)
    urls6.append(rigss.strip())
urlsb=list()


#Riduco a un insieme univoco serve per avere differenti domini e creare gli schemi
urlsb=set(urls6)

#Per scriverlo in un file lo trasformo in una lista
urlsbb=list()

urlsbb=list(urlsb)



df3.count
#Parser Html. Prima effettuo una richiesta http per connettermi
#1.faccio una richiesta alla pagina
index=0

for index, row in df2.iterrows():
    response = requests.get(row['link'])
    contenuto = response.text
    filename = str("C:/Users/Administrator/Desktop/Fileshtml/filename") + str(row) + str(".html")
    file= open(filename,"w", encoding="utf-8")
    file.write(contenuto)
    file.close()


###Reading Json
pd.read_json("C:/Users/Administrator/Desktop/PythonProject/tutorial/Dati/risultatifinali.json")


######WRITE FILE FROM LIST
df = pd.DataFrame(b)
print(df.to_csv('C:/Users/Administrator/Desktop/entry.csv',encoding='utf-8',sep=',',index=False, header=False))

#######################################################################################
#Query per i Tweets


q = 'MATCH(anything:Tweet) RETURN anything'

resultweet = db.query(q,returns=(client.Node))

for r in resultweet:
d.append(r[0])

print(resultweet[1])

#Converto il tipo query.QuerySequence in una struttura dati più adatta per l'elaborazione

session.close()




#creazione del bot


#Salvataggio dei risultati



#caricamente su Neo4j
