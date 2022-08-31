import time


def clear():
    for _ in range(100):
        print()


def error_1():
    clear()
    print('Некорректный ответ')
    time.sleep(3)
    clear()


def error_2():
    clear()
    print('Поменяйте раскладку')
    time.sleep(3)
    clear()


def error_3():
    clear()
    print('Текст не введен')
    time.sleep(3)
    clear()


def layout(text, language):
    if language == '1':
        for c in text:
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
                error_2()
                return False
    else:
        for c in text:
            if 1040 <= ord(c) <= 1103:
                error_2()
                return False
    return True


def translate(text, shift_step, language):
    if language == '1':
        for i in range(len(text)):
            if 1072 <= ord(text[i]) <= 1103:
                text = text[:i] + chr(((ord(text[i]) + shift_step - 1072) % 32) + 1072) + text[i + 1:]
            elif 1040 <= ord(text[i]) <= 1071:
                text = text[:i] + chr(((ord(text[i]) + shift_step - 1040) % 32) + 1040) + text[i + 1:]
    if language == '2':
        for i in range(len(text)):
            if 97 <= ord(text[i]) <= 122:
                text = text[:i] + chr(((ord(text[i]) + shift_step - 97) % 26) + 97) + text[i + 1:]
            elif 65 <= ord(text[i]) <= 90:
                text = text[:i] + chr(((ord(text[i]) + shift_step - 65) % 26) + 65) + text[i + 1:]
    print(text)
