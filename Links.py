# Mi collego al database Neo4j

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import urllib3.request
import urllib.request
import csv
from itertools import islice
import re
#Query news
db = GraphDatabase("http://localhost:7474", username="neo4j", password="mindbrexit")
q = 'MATCH(anything:News) RETURN anything'

results = db.query(q,returns=(client.Node))


#inizializzo la lista
a = list()
b = list()
c = list()

#Lista Nodi
for r in results:
    a.append(r[0])

#Lista Links
for s in a:
    b.append(s["url"])

#creo una sottolista per esportare il file e rendere leggibile di scrapy i links
i=len(b)

for t in b[150001:250000]:
    c.append(t)
#SCrivere un csv mi porta a un accelerazione del processo

    df = pd.DataFrame(c)
    print(df.to_csv('C:/Users/Administrator/Desktop/PythonProject/tutorial/Dati/entry.csv', encoding='utf-8', index=False,
                    header=False, sep='\n'))
    #
    #with open("Giro2.csv", "w", encoding="utf-8") as output:
    #  output.write(str(lines))


