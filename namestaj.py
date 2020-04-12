from readupdateCSV import *

namestaj = []
namestaj = readCsv('Podaci/namestaj.csv', namestaj)
"""
def changeValue(sifra, vrednost, nova_vrednost):
    for i in namestaj:
        if i['sifra'] == sifra:
            i[vrednost] = nova_vrednost
    updateCsv('Podaci/namestaj.csv', namestaj)
"""
changeValue('sifra', 'or1', 'cena', '19000', namestaj, 'namestaj')

delete('or1', 'sifra', namestaj, 'namestaj')



