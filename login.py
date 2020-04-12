from getpass import getpass
from korisnici import korisnici, addUser
from namestaj import namestaj
from usluge import usluge

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
def kupovina():
    x = input("Da li zelite da odmah kupite proizvod ili zelite da pogledate katalog?(Napisite: kupovina ili pregled): ")
    while x != 'kupovina' and x != 'pregled':
        print("Molim vas da unesete kupovina ili pregled.")
        x = input("Da li zelite da odmah kupite proizvod ili zelite da pogledate katalog?(Napisite: kupovina ili pregled): ")
    if x == 'kupovina':
        korpa = []
        y = 0
        while y == 0:
            proizvod = input('Unesite naziv ili sifru namestaja: ')
            for i in range(len(namestaj)):
                if namestaj[i]['sifra'] == proizvod or namestaj[i]['naziv'] == proizvod:
                    korpa.append(namestaj[i])
                    y = 1
            if y != 1:
                print("Pokusajte ponovo")
    if x == 'pregled':
        pregled(namestaj)

def pregled(csv_fajl):
    print("Sifra | Naziv | Boja | Kolicina | Cena | Kategorija")
    for i in range(len(csv_fajl)):
        line = " | "
        print(csv_fajl[i]['sifra'] + line + csv_fajl[i]['naziv'] + line + csv_fajl[i]['boja'] + line + csv_fajl[i]['kolicina'] + line + csv_fajl[i]['cena'] + line + csv_fajl[i]['kategorija'])
def searching():
    if uloga == 'kupac':
        print("Dobrodosli!")
        kupovina()
        y = input("Da li zelite da nastavite kupovinu?(Napisite da ili ne) ")
        while y == 'da':
            kupovina()
            y = input("Da li zelite da nastavite kupovinu?(Napisite da ili ne) ")
    if uloga == 'menadzer':
        print("Dobrodosli!")
        x = input("Sta zelis da uradis? Sta zelis da pregledas? (Unesi: namestaj, korisnici ili usluge)")
        while x != 'namestaj' and x != 'korisnici' and x!= 'usluge':
            print("Pogresio si. Molim te ukucaj ponovo")
            x = input("Sta zelis da uradis? Sta zelis da pregledas? (Unesi: namestaj, korisnici ili usluge)")
        
searching()

