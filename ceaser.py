
# здороваемся
print('Добро пожаловать! Я умею шифровать и дешифровать текст согласо шифру Цезаря!')
print('Давай определимся, что нужно сделать, я помогу!')
print()

# задаем нужные вопросы, поверхностная "защита от дурака"
encryption = input('шифруем или дешифруем?')
encryption_yes = 'шифруем'
encryption_no = 'дешифруем'
while encryption != encryption_yes and encryption != encryption_no:
    encryption = input('немного ты не то ввел. введи или "шифруем", или "дешифруем"')
if encryption == encryption_yes:
    print('отлично! мы зашифруем твой текст!')
else:
    print('отлично! мы расшифруем твой текст!')

lang = input('выбери язык (русский или английский)')
lang_ru = 'русский'
lang_en = 'английский'
while lang != lang_en and lang != lang_ru:
    lang = input('немного ты не то ввел. введи или "русский", или "английский"')
if lang == lang_en:
    print(f'отлично! {encryption} на английском языке!')
else:
    print(f'отлично! {encryption} на русском языке!')

step = input('теперь давай определимся с количеством символов, на которое сдвигается текст. введи число')
while step.isdigit() != True:
    step = input('что-то ты не то ввел. нужно просто число')
if int(step) == 1:
    print(f'отлично! {encryption} на {step} букву! наш язык - {lang}!')
elif 1 < int(step) < 5:
    print(f'отлично! {encryption} на {step} буквы! наш язык - {lang}!')
else:
    print(f'отлично! {encryption} на {step} букв! наш язык - {lang}!')
print()
print('теперь самое важное. введи свой текст, фразу или слово. будь внимателен. что введешь, то и будет обработано')
print('программа правильность введенного текста не проверяет')
text = input('введи или вставь свой текст, фразу или слово')


# вспоминаем русский и английский алфавит
alphabet_rus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_rus_up = alphabet_rus.upper()
alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_en_up = alphabet_en.upper()

# в цикле два условия в зависимости от того, шифруем или дешифруем, попутно учитываем остальные параметры
new_text = ''
while True:
    for i in text:
        if encryption == 'шифруем':
            if lang == 'русский':
                if i in alphabet_rus:
                    ind = alphabet_rus.index(i)
                    new_text += alphabet_rus[ind + int(step) % len(alphabet_rus)]
                elif i in alphabet_rus_up:
                    ind = alphabet_rus_up.index(i)
                    new_text += alphabet_rus_up[ind + int(step) % len(alphabet_rus_up)]
                else:
                    new_text += i
            if lang == 'английский':
                if i in alphabet_en:
                    ind = alphabet_en.index(i)
                    new_text += alphabet_en[ind + step % len(alphabet_en)]
                elif i in alphabet_en_up:
                    ind = alphabet_en_up.index(i)
                    new_text += alphabet_en_up[ind + step % len(alphabet_en_up)]
                else:
                    new_text += i
        if encryption == 'дешифруем':
            if lang == 'русский':
                if i in alphabet_rus:
                    ind = alphabet_rus.index(i)
                    new_text += alphabet_rus[ind - int(step) % len(alphabet_rus)]
                elif i in alphabet_rus_up:
                    ind = alphabet_rus_up.index(i)
                    new_text += alphabet_rus_up[ind - int(step) % len(alphabet_rus_up)]
                else:
                    new_text += i
            if lang == 'английский':
                if i in alphabet_en:
                    ind = alphabet_en.index(i)
                    new_text += alphabet_en[ind - int(step) % len(alphabet_en)]
                elif i in alphabet_en_up:
                    ind = alphabet_en_up.index(i)
                    new_text += alphabet_en_up[ind - int(step) % len(alphabet_en_up)]
                else:
                    new_text += i
    print(new_text)
    replay = input('если нужно зашифровать что-то еще? напиши "да" или "нет"') # заходим на следующий круг, если это нужно пользователю
    if replay == 'да':
        continue
    elif replay == 'нет':
        print('до новых шифров, мой друг!')
        break

