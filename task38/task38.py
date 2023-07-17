#Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных


def print_records(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(*line.split(';'), end='')

def find_char():
    print('Выберите характеристику:')
    print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
    char = input()
    while char not in ('0', '1', '2', '3', '4', 'q'):
        print('Введены неверные данные')
        print('Выберите характеристику:')
        print('0 - id, 1 - фамилия, 2 - имя, 3 - отчество, 4 - номер, q - выйти')
        char = input()
    if char != 'q':
        inp = input('Введите значение\n')
        return char, inp
    else:
        return 'q', 'q'


def find_records(file_name: str, char, condition):
    if condition != 'q':
        printed = False
        with open(file_name, 'r', encoding='utf-8') as data:
            for line in data:
                if condition == line.split(';')[int(char)]:
                    print(*line.split(';'))
                    printed = True
        if not printed:
            print("Не найдено")
        return printed


def check_id_record(file_name: str, text: str):
    decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    while decision not in ('1', 'q'):
        if decision != '2':
            print('Введены неверные данные')
        else:
            find_records(path, *find_char())
        decision = input(f'Вы знаете id записи которую хотите {text}? 1 - да, 2 - нет, q - выйти\n')
    if decision == '1':
        record_id = input('Введите id, q - выйти\n')
        while not find_records(file_name, '0', record_id) and record_id != 'q':
            record_id = input('Введите id, q - выйти\n')
        return record_id
    return decision


def confirmation(text: str):
    confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    while confirm not in ('y', 'n'):
        print('Введены неверные данные')
        confirm = input(f"Подтвердите {text} записи: y - да, n - нет\n")
    return confirm


def replace_record_line(file_name: str, record_id, replaced_line: str):
    replaced = ''
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            replaced += line
            if record_id == line.split(';', 1)[0]:
                replaced = replaced.replace(line, replaced_line)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write(replaced)


def change_records(file_name: str):
    record_id = check_id_record(file_name, 'Изменить контакт')
    if record_id != 'q':
        replaced_line = f'{int(record_id)};' + ';'.join(
            input('Введите фамилию, имя, отчество, номер телефона через пробел, описание\n').split()[:4]) + ';\n'
        confirm = confirmation('изменение')
        if confirm == 'y':
            replace_record_line(file_name, record_id, replaced_line)


def add_records(file_name: str):
    add_id = input(f'Вы хотите добавить новую запись? 1 - да, 2 - нет, q - выйти\n')
    while add_id not in ('2', 'q'):
        if add_id != '1':
            print('Введены неверные данные')
        else:
            with open(file_name, "r", encoding="utf-8") as data:
                tel_file = data.read()
                num = len(tel_file.split("\n"))
                replaced_line = f'{int(num)};' + ';'.join(
                input('Введите фамилию, имя, отчество, номер телефона через пробел, описание\n').split()[:4]) + ';\n'
                confirm = confirmation('добавление')
                if confirm == 'y':
                    with open(file_name, "a", encoding="utf-8") as data:
                        data.write(replaced_line)
            exit = input('Хотите выйти? 1 - нет, q - выйти\n')
            if exit == 'q':
                return add_id
            else:
                return add_records(file_name)

def delete_records(file_name: str):
    record_id = check_id_record(file_name, 'Удалить контакт')
    if record_id != 'q':
        confirm = confirmation('удаление')
        if confirm == 'y':
            replace_record_line(file_name, record_id, '')


path = 'phon.txt'

try:                        # исключения try/except/finally
    file = open(path, 'r')  # открыть файл
except IOError:             # если нет файла он создается
    print('Создан новый справочник -> phon.txt ')
    file = open(path, 'w')
finally:                    
    file.close()

actions = {'1': 'Показать контакты',
           '2': 'Найти контакт',
           '3': 'Добавить контакт',
           '4': 'Изменить контакт',
           '5': 'Удалить контакт',
           'q': 'Выход'}

action = None
while action != 'q':
    print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
    action = input()
    while action not in actions:
        print('Какое действие хотите совершить?', *[f'{i} - {actions[i]}' for i in actions])
        action = input()
        if action not in actions:
            print('Введены неверные данные')
    if action != 'q':
        if action == '1':
            print_records(path)
        elif action == '2':
            find_records(path, *find_char())
        elif action == '3':
            add_records(path)
        elif action == '4':
            change_records(path)
        elif action == '5':
            delete_records(path)