from readupdateCSV import readCsv, updateCsv

korisnici = []
korisnici = readCsv('Podaci/korisnici.csv', korisnici)

def addUser(ime, prezime, korsnicko_ime, lozinka):
    korisnici.append({'korisnicko ime' : korsnicko_ime, 'lozinka' : lozinka, 'ime' :ime,
    'prezime' : prezime, 'uloga': 'kupac' })
    updateCsv('Podaci/korisnici.csv', korisnici)



