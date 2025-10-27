# 4. Napisz program do przeliczania liczby zapisanej w formacie binarnym na
# system dziesiętny i odwrotnie (niech program zapyta o kierunek konwersji)
which_number = (input('Podaj jedostkę liczbową b lub d: '))
number_value = input('Podaj liczbę: ')
number_value_int = int(number_value)
if which_number == 'd':
    number_converted = number_value_int
    i = 0
    binary_list = []
    print('Liczba binarna: ',end='')
    while i < 8:
        number_binary = number_converted % 2
        binary_list.insert(-i, number_binary)
        number_converted = number_converted // 2
        if number_converted == 0:
            break
        i += 1
    for b in binary_list:
        print(b,end='')
elif which_number == 'b':
    number_converted = number_value_int
    i = 0
    sum_integer = 0
    number_reverted = number_value[::-1]
    print('Liczba dziesiętna: ', end='')
    while i < len(number_value):
        j = int(number_reverted[i])
        number_integer = j * 2 ** i
        sum_integer = number_integer + sum_integer
        i += 1
    print(str(sum_integer), end='')
else:
    print('Podałeś niewłaściwą jednostkę.')
    exit()
