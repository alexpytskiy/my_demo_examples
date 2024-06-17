import random

n = random.randint(1, 101)
print('Добро пожаловать в числовую угадайку')
mx = input('для начала давайте определимся с максимальным числом. введите его: ')
mx = int(mx)
def is_valid(num):
    return num in range(1, mx)

cnt = 1
replay = 'y'
while True and replay == 'y':
    num = input(f'Введите число от 1 до {mx}: ')
    num = int(num)
    if is_valid(num) == False:
        print(f'Попробуйте еще раз. Нужно число от 1 до {mx} включительно')
    if num < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        cnt += 1
    elif num > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        cnt += 1
    elif num == n:
        print(f'ЭВРИКА! Вы угадали числов за {cnt} попыток!')
        question = input('Сыграем еще разок? Введите "y" или "n":' )
        if question == 'n':
            print('до скорых встреч!')
            replay = 'n'
            break


