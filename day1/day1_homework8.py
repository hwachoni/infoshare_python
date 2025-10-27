# 8. Program rysujący piramidę o określonej wysokości, np dla 3
#         #
#       ###
#     #####
pyramid_height_input = input('Podaj wysokość piramidy: ')
pyramid_height = int(pyramid_height_input)
count = -1
while count < pyramid_height + 2:
    print(f'{"#" * (count + 2):^{(pyramid_height * 2)}}')
    count += 2
