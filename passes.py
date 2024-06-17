import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_lettets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
missed = 'il1Lo0O'
chars = ''

cnt = int(input('введите количество паролей для генерации: '))
l = int(input('введите длину одного пароля: '))

numbers = input('включать цифры 0123456789? ("да"/"нет"): ')
up = input('включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ("да"/"нет"): ')
down = input('включать строчные буквы abcdefghijklmnopqrstuvwxyz? ("да"/"нет"): ')
punct = input('включать символы !#$%&*+-=?@^_? ("да"/"нет"): ')
miss = input('исключать ли неоднозначные сиволы il1Lo0O? ("да"/"нет"): ')

if numbers.lower() == 'да':
    chars += digits
if up.lower() == 'да':
    chars += uppercase_lettets
if down.lower() == 'да':
    chars += lowercase_letters
if punct.lower() == 'да':
    chars += punctuation
if miss == 'да':
    for i in chars:
        if i in missed:
            chars = chars.replace(i, '')


def generate_password(l, cnt):
    for i in range(1, cnt + 1):
        print(*random.sample(chars, l), sep='')
    return print('пароли сгенерированы')

generate_password(l, cnt)