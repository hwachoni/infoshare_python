# 2. Napisz program do obliczania pola powierzchni koła
# o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)

pi_value = 3.14
print('Wzór na pole koła: π * r^2')
circle_radius = input('Podaj promień koła r: ')
circle_radius_float = float(circle_radius)
print('Obliczenie pola koła: ' + str(pi_value) + ' * ' + circle_radius + '^2')
circle_area = pi_value * circle_radius_float ** 2
print('Pole koła o promieniu ' + circle_radius + ' wynosi: ' + str(circle_area))
