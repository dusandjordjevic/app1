from readupdateCSV import *

korisnici = []
korisnici = readCsv('Podaci/korisnici.csv', korisnici)

def addUser(ime, prezime, korsnicko_ime, lozinka):
    korisnici.append({'korisnicko ime' : korsnicko_ime, 'lozinka' : lozinka, 'ime' :ime,
    'prezime' : prezime, 'uloga': 'kupac' })
    updateCsv('Podaci/korisnici.csv', korisnici)
"""
def delUser(korsnicko_ime):
    for i in range(len(korisnici)):
        if korisnici[i]["korisnicko ime"] == korsnicko_ime:
            del korisnici[i]
            updateCsv('Podaci/korisnici.csv', korisnici)
            break
"""
changeValue('korisnicko ime', 'marko1', 'uloga', 'menadzer', korisnici, 'korisnici')
delete('lristic','korisnicko ime', korisnici, 'korisnici')

