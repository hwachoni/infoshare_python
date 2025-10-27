# 6. Napisz program do wyliczania silni dla zadanej liczby
number_input = input('Podaj liczbę: ')
number = int(number_input)
i = 1
sum_factorial = 1
while i < number + 1:
    sum_factorial = sum_factorial * i
    i += 1
print('Silnia z liczby ' + number_input + ' wynosi ' + str(sum_factorial) + '.')
