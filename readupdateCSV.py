import csv

def readCsv(csv_fajl, lista):
    with open(csv_fajl, 'r') as read_csv:
        reading_csv = csv.DictReader(read_csv, delimiter=",")
        lista = []

        for line in reading_csv:
            lista.append(line)
    return lista

def updateCsv(csv_fajl, lista):
    with open(csv_fajl, 'w', newline="") as f:  
        keys = lista[0].keys()
        writer = csv.DictWriter(f, fieldnames=keys)

        writer.writeheader()
        for i in lista:
            writer.writerow(i)

def changeValue(kolona, ime, vrednost, nova_vrednost, lista, csv_fajl):
    for i in lista:
        if i[kolona] == ime: 
            i[vrednost] = nova_vrednost
    update = "Podaci/" + csv_fajl + ".csv"
    updateCsv(update, lista)

def delete(ime, kolona, lista, csv_fajl):
    for i in range(len(lista)):
        if lista[i][kolona] == ime:
            del lista[i]
            update = 'Podaci/' + csv_fajl + '.csv'
            updateCsv(update, lista)
            break




