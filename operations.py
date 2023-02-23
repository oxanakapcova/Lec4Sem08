def print_all():
    pb = open('phone_book.txt', 'r')
    print(pb.read())
    pb.close()


def find_entry(name):
    pb = open('phone_book.txt', 'r')
    print(pb)
    list_of_found_entries = list()
    for l in pb:
        print(l)
        if name in l.split():
            list_of_found_entries.append(l)
    pb.close()
    return list_of_found_entries


def add_an_entry(data):
    pb = open('phone_book.txt', 'a')
    pb.write(' '.join(data) + '\n')
    pb.close()

def prompt():
    print("""
    Нажмите '1', чтобы вывести весь справочник на экран
    Нажмите '2', чтобы записать новый контакт
    Нажмите '3', чтобы найти контакт 
    Нажмите '0', чтобы завершить работу
    """)

