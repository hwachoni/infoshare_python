# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita
# i odwrotnie (niech program zapyta o kierunek konwersji)

which_degree = (input('Podaj jedostkę stopni C lub F: '))
which_degree_upper = which_degree.upper()
degree_value = input('Podaj liczbę stopni: ')
degree_value_float = float(degree_value)
if which_degree_upper == 'C':
    degree_converted = degree_value_float * 9/5 + 32
    print(str(degree_value_float) + ' ' + which_degree_upper +
          ' to w przeliczeniu ' + str(degree_converted) + ' F')
elif which_degree_upper == 'F':
    degree_converted = (degree_value_float - 32) / 2
    print(str(degree_value_float) + ' ' + which_degree_upper +
          ' to w przeliczeniu ' + str(degree_converted) + ' C')
else:
    print('Podałeś niewłaściwą jednostkę stopni.')
    exit()
