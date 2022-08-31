from functions import *

while True:
    print('Выберите направление:')
    print('1. Шифрование')
    print('2. Дешифрование')
    direction = input('1 или 2 пункт? ')
    if direction != '1' and direction != '2':
        error_1()
        continue
    else:
        direction = int(direction)
        clear()
        break
while True:
    print('Выберите язык алфавита:')
    print('1. Русский')
    print('2. Английский')
    alphabet_language = input('1 или 2 пункт? ')
    if alphabet_language != '1' and alphabet_language != '2':
        error_1()
        continue
    else:
        clear()
        break
while True:
    shift_step = input('Введите шаг сдвига: ')
    if shift_step.isdigit():
        shift_step = int(shift_step)
        if direction == 2:
            shift_step = -shift_step
        clear()
        break
    else:
        error_1()
        continue
while True:
    text = input('Введите текст для обработки\n')
    if text.isspace():
        error_3()
    if layout(text, alphabet_language):
        break
    else:
        continue

for i in range(25):
    translate(text, i, alphabet_language)


