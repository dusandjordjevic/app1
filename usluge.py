from readupdateCSV import *

usluge = []
usluge = readCsv('Podaci/usluge.csv', usluge)

changeValue('naziv', 'prevoz', 'cena', '1200', usluge, 'usluge')

    