
# 1. функция возращает фио и номер телефона введенные с консоли
def get_data():
    last_name = input('Surname:  ').strip()
    first_name = input('Name: ').strip()
    middle_name = input('Middle name: ').strip()
    phone_number = input('Phone number: ').strip()
    return (last_name, first_name, middle_name, phone_number)


# 2. функция предлагает выбрать необходимое действие
def get_operation_number():
    operation = input().strip()
    while operation not in ('1', '2', '3', '4', '5', '6', '7', '0'):
        print('Not correct, try again:')
        operation = input().strip()
    return operation


# 3. функция по номеру числа делает нужную операцию
def do_operation(operation_number):
    if operation_number == '1':
        print_all()
    elif operation_number == '2':
        add_data(get_data())
    elif operation_number == '3':
        print('\n'.join(find_entry(input('Type surname, name, middle name or phone number: ').strip())))
    elif operation_number == '4':
        change_data()
    elif operation_number == '5':
        delete_full_file()
    elif operation_number == '6':
        delete_selected_data()
    elif operation_number == '7':
        change_selected_data()
    else:
        print('Завершение работы')


# 4. функция выводит на печать весь техт из файла (кнопка 1)
def print_all():
    with open('phonebook.txt', 'r') as phonebook:
        for line in phonebook:
            print(line.replace('\n', ''))
    print('====end====')


# 5. функция ищет по заданному параметру (кнопка 3)
def find_entry(your_parametr):
    with open('phonebook.txt', 'r') as phonebook:
        list_of_found = list()  # empthy tupple
        for line in phonebook:
            if your_parametr in line.split():
                list_of_found.append(line)
                print('====found====')
        return list_of_found


# 6. функция добавляет текст в файл (кнопка 2)
def add_data(data):
    with open('phonebook.txt', 'a') as phonebook:
        phonebook.write(' '.join(data) + '\n')
    print('====added====')


# 7. функция печатает подсказку пользователю
def print_prompt():
    print("""
    Нажмите '1', чтобы вывести весь справочник на экран
    Нажмите '2', чтобы записать новый контакт
    Нажмите '3', чтобы найти контакт 
    Нажмите '4', чтобы изменить данные в файле(останутся только те что вы запишите)
    Нажмите '5', чтобы удалить все данные в файле
    Нажмите '6', чтобы удалить выбранные данные
    Нажмите '7', чтобы заменить выбранные данные
    Нажмите '0', чтобы завершить работу
    """)


# 8. функция удалит все данные из файла (кнопка 5)
def delete_full_file():
    with open('phonebook.txt', 'w'):
        print('====deleted====')

# 10. функция изменит выбранные данные (кнопка 4)
# удалится все что было, останется то что записано
def change_data():
    with open('phonebook.txt', 'r+') as phonebook: # r+ mode opens the file in read and write mode
        s = input("Enter text to replace the existing contents:")
        phonebook.truncate(0) # усекает размер файла
        phonebook.write(s)
        print("Text successfully replaced")


# 9. функция удалит только выбранные данные из файла(кнопка 6)
def delete_selected_data():
    with open('phonebook.txt', 'r') as phonebook:
        data = phonebook.readlines()
    with open('phonebook.txt', 'w') as phonebook:
        a = input('type what you want to delete: ')
        for line in data:
            # condition for data to be deleted
            if line.strip("\n") != a:
                phonebook.write(line)
        print('====deleted====')

# функция предложит что нужно заменить и на что, остальное не изменится (кнопка 7)
def change_selected_data():
    search_text = input('what be replaced: ')
    replace_text = input('type new text: ')
    with open(r'phonebook.txt', 'r') as phonebook:
        # открыт только для чтения
        data = phonebook.read()
        data = data.replace(search_text, replace_text)
    # теперь открыт для записи
    with open(r'phonebook.txt', 'w') as phonebook:
        phonebook.write(data)
    print('====replaced====')


if __name__ == '__main__':
    change_selected_data()



