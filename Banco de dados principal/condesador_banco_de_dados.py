# formato de saída: utf-8
import csv
import pandas as pd
import re

base_TCC_fake = []

for i in range(1,6619,1):
    file = open('Fake/Fake_ ('+str(i)+')'+'.txt', 'r', encoding="utf-8")
    base_TCC_fake.append(file.read().replace("\n",""))
file.close()

base_TCC_true = []

for i in range(1,6056,1):
    file = open('True/True_ ('+str(i)+')'+'.txt', 'r', encoding="utf-8")
    base_TCC_true.append(file.read().replace("\n",""))
file.close()

#removendo instancias vazias
base_TCC_true_remove_vazio = []
for artigo in base_TCC_true:
    if artigo != '' and artigo != None and artigo != '  ':
        base_TCC_true_remove_vazio.append(artigo)

base_TCC_fake_remove_vazio = []
for artigo in base_TCC_fake:
    if artigo != '':
        base_TCC_fake_remove_vazio.append(artigo)

def limpa_texto(texto):
        texto = re.sub(";", " ", texto)
        texto = re.sub("\n", " ", texto)
        texto = re.sub('“', "", texto)
        texto = re.sub('”', "", texto)        
        texto = re.sub("  ", "", texto)
        
        return texto

dataSet_verdade = []
for artigo in base_TCC_true_remove_vazio:
    dataSet_verdade.append(limpa_texto(artigo))

dataSet_fake = []
for artigo in base_TCC_fake_remove_vazio:
    dataSet_fake.append(limpa_texto(artigo))


def dados_dataSet(artigo, classe):    
    datasett = pd.read_csv('base_TCC.csv', sep=';')    
    idd = len(datasett)
        

    # Atualização do dataset
    with open('base_TCC.csv', 'a', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')       
        spamwriter.writerow([idd, artigo, classe])        
        
for i in range(0,15600,1):
    dados_dataSet(dataSet_fake[i], 1)
    dados_dataSet(dataSet_verdade[i], 0)

with open('base_TCC.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['id', 'noticia', 'classificacao']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)