# 8. Program rysujący piramidę o określonej wysokości, np dla 3
#         #
#       ###
#     #####
import math
pyramid_height_input = input('Podaj wysokość piramidy: ')
pyramid_height = int(pyramid_height_input)
rounded = math.ceil(pyramid_height / 2)
count = -1
while count <= (pyramid_height + rounded):
    print(f'{"#" * (count + 2):^{(pyramid_height * 2)}}')
    count += 2
