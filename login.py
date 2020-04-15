from getpass import getpass
from korisnici import korisnici, addUser
from namestaj import namestaj
from usluge import usluge
from readupdateCSV import updateCsv
import copy

def login():
    x = input("Da li ste novi korisnik ili ste vec registrovani?(Napisite: novi ili stari): ")
    while x != 'stari' and x != 'novi':
        print("Molim vas unesite novi ili stari.")
        x = input("Da li ste novi korisnik ili ste vec registrovani?(Napisite: novi ili stari): ")
    if x == 'novi':
        ime = input("Unesite vase ime: ")
        prezime = input("Unesite vase prezime: ")
        korisnicko_ime = ime[0].lower() + prezime[0:].lower()
        print("Vase korisnko ime je: ", korisnicko_ime)
        sifra1 = getpass('Unesite sifru: ')
        sifra2 = getpass("Ponovite sifru: ")
        while sifra1 != sifra2:
            print("Sifre se ne poklapaju. Pokusajte ponovo")
            sifra1 = getpass('Unesite sifru: ')
            sifra2 = getpass("Ponovite sifru: ")
        sifra = sifra1
        uloga = "kupac"
        addUser(ime, prezime, korisnicko_ime, sifra)
        return uloga
    if x == 'stari':
        y = 0
        while True:
            korisnicko_ime = input("Unesite vase korisnicko ime: ")
            sifra = getpass("Unesite vasu sifru: ")
            for i in range(len(korisnici)):
                if korisnici[i]['korisnicko ime'] == korisnicko_ime and korisnici[i]['lozinka'] == sifra:
                    print('Uspesno ste se ulogovali')
                    uloga = korisnici[i]['uloga']
                    y = 1 
            if y == 1:
                return uloga
            else:
                print("Pogresili ste. Pokusajte ponovo")             

uloga = login()
korpa = []
def kupovina():
    x = input("Da li zelite da odmah kupite proizvod ili zelite da pogledate katalog?(Napisite: kupovina ili pregled): ")
    while x != 'kupovina' and x != 'pregled':
        print("Molim vas da unesete kupovina ili pregled.")
        x = input("Da li zelite da odmah kupite proizvod ili zelite da pogledate katalog?(Napisite: kupovina ili pregled): ")
    if x == 'kupovina':
        y = 0
        while y == 0:
            proizvod = input('Unesite naziv ili sifru namestaja: ')
            for i in range(len(namestaj)):
                if namestaj[i]['sifra'] == proizvod or namestaj[i]['naziv'] == proizvod:
                    namestaj_copy = copy.deepcopy(namestaj)             
                    namestaj_copy[i]['kolicina'] = 1
                    if korpa == []:
                        korpa.append(namestaj_copy[i])
                    else:
                        n = 0
                        for i in korpa:
                            if proizvod  == i['sifra'] or proizvod == i['naziv']:
                                i['kolicina'] += 1
                                n += 1
                        if n == 0:
                            korpa.append(namestaj_copy[i])
                    namestaj[i]['kolicina'] = int(namestaj[i]['kolicina']) - 1
                    updateCsv('Podaci/namestaj.csv', namestaj)
                    print("Vasa korpa: ")
                    pregled(korpa)
                    y = 1
            if y != 1:
                print("Pokusajte ponovo")
    if x == 'pregled':
        pregled(namestaj)

    

def pregled(csv_fajl):
    print("Sifra | Naziv | Boja | Kolicina | Cena | Kategorija")
    for i in range(len(csv_fajl)):
        line = " | "
        text = csv_fajl[i]['sifra'] + line + csv_fajl[i]['naziv'] + line + csv_fajl[i]['boja'] + line + str(csv_fajl[i]['kolicina']) + line + csv_fajl[i]['cena'] + line + csv_fajl[i]['kategorija']
        print(text)
def searching():
    if uloga == 'kupac':
        print("Dobrodosli!")
        kupovina()
        y = input("Da li zelite da nastavite kupovinu?(Napisite da ili ne) ")
        while y == 'da':
            if y == 'da':
                n = input("Da li zelite da kupite jos neki proizvod ili zelite da izbriste neki prozivod iz korpe?(Unesite: kupovina ili brisanje, za izlaz pritisnite enter) ")
                while n != "kupovina" and n != 'brisanje' and  n != '':
                    print("Pogresili ste. Molim vas pokusajte ponovo")
                    n = input("Da li zelite da kupite jos neki proizvod ili zelite da izbriste neki prozivod iz korpe?(Unesite: kupovina ili brisanje, za izlaz pritisnite enter) ")
                if n == 'kupovina':
                    kupovina()
                    y = input("Da li zelite da nastavite kupovinu?(Napisite da ili ne) ")
                elif n == 'brisanje':
                    for i in range(len(korpa)):
                        print(korpa[i])
                    while True:
                        m = input("Koji proizvod zelite da izbrisete? (Unesite sifru ili stisnite enter ako zelite da nastavite kupovinu: ")
                        for i in range(len(korpa)):
                            if m == korpa[i]['sifra']:
                                for n in range(len(namestaj)):
                                    if namestaj[n]['sifra'] == korpa[i]['sifra']:
                                        namestaj[n]['kolicina'] = int(namestaj[n]['kolicina']) + 1
                                        updateCsv('Podaci/namestaj.csv', namestaj)
                                del korpa[i]
                                print("Vasa korpa: ")
                                pregled(korpa)
                        if m == '':
                            break
                else:
                    break                          

    if uloga == 'menadzer':
        print("Dobrodosli!")
        x = input("Sta zelis da uradis? Sta zelis da pregledas? (Unesi: namestaj, korisnici ili usluge)")
        while x != 'namestaj' and x != 'korisnici' and x!= 'usluge':
            print("Pogresio si. Molim te ukucaj ponovo")
            x = input("Sta zelis da uradis? Sta zelis da pregledas? (Unesi: namestaj, korisnici ili usluge)")
        
searching()

