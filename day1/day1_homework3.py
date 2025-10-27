# 3. Napisz program, który rysuje prostokąt o zadanych rozmiarach
# (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +---+
#     |   |
#     |   |
#     +---+

rectangle_height = input('Podaj wysokość prostokąta: ')
rectangle_height_int = int(rectangle_height)
rectangle_length = input('Podaj długość prostokąta: ')
rectangle_length_int = int(rectangle_length)
print('+','+',sep='-' * rectangle_length_int)
licznik = 0
while licznik < rectangle_height_int:
    print('|','|',sep=' ' * rectangle_height_int)
    licznik += 1
print('+','+',sep='-' * rectangle_length_int)
