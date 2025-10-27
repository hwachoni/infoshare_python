# 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym..
year_input = input('Podaj rok: ')
year = int(year_input)
# Rok jest przestępny, jeśli jest podzielny przez 4.
# Wyjątek: jeśli jest podzielny przez 100, ale nie przez 400, to nie jest przestępny.
year_4 = year % 4
year_100 = year % 100
year_400 = year % 400
if year_4 != 0:
    print('Rok ' + year_input + ' nie jest przestępny.')
elif year_4 == 0 and year_100 == 0 and year_400 != 0:
    print('Rok ' + year_input + ' nie jest przestępny.')
else:
    print('Rok ' + year_input + ' jest przestępny.')
