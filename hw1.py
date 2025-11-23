
import json
from pprint import pprint


# 1. Просмотр контакта
# 2. Создание контакта
# 3. Удаление контакта
# 4. Изменение контакта
# 5. Найти контакт

PATH = "phone_book.json"

def get_phonebook():
    '''
    Загружает базу контактов из файла
    '''
    with open(PATH, 'r', encoding='UTF-8') as file:
        return json.load(file)
        
        
        
def save_phonebook(content):
    '''
    Сохраняет базу контактов
    '''
    with open(PATH, 'w', encoding='UTF-8') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)
        
    
    
def show_contact(content):
    '''
    Список всех контактов
    '''
    print('\n')
    print("Список контактов:")
    pprint(content, sort_dicts=False)
    
    
def add_contact (content):   
    '''
    Добавление контактов
    -имя
    -телефон
    -описание
    ''' 
    print('\n')
    name = input('Введите имя:')
    phone = input('Введите номер телефона:')
    comment = input('Описание:')
    print('\n')
    
    # Присваиваем новому контакту id (последний + 1) 
    id_list = list(content.keys())
    if not id_list:
        return 0
    max_id = max(map(int, id_list))
    id_contact = str(max_id + 1)
    
    content [id_contact] = {"name": name, "phone": phone, "comment": comment}
    pprint (content, sort_dicts=False)
    save_phonebook(content)
    print(f'Контакт {name} добавлен')
    return(content)


def del_contact (content):
    '''
    Удаление контакта
    '''
    print('\n')
    pprint(content, sort_dicts=False)
    del_id = "удаляемый контакт"
    del_id = input('Введите номер контакта, который необходимо удалить:')
    if del_id in content:
        del content[del_id]
    print('\n')
    pprint(content, sort_dicts=False)
    
    save_phonebook(content)
    print(f'Контакт {del_id} удален')
    return(content)


def edit_contact(content):
    '''
    Вносит изменение контакта
    '''
    print('\n')
    pprint(content, sort_dicts=False)
    edit_id = "изменяемый контакт"
    edit_id = input('Введите номер контакта, который необходимо изменить: ')
    if edit_id in content :
        content[edit_id]["name"] = input('Введите новое имя: ')
        content[edit_id]["phone"] = input('Введите новый телефон: ')
        content[edit_id]["comment"] = input('Введите новое описание: ')
    else:
        print(f'Контакт {edit_id} не найден')
        
    save_phonebook(content)
    print('\n')
    pprint(content, sort_dicts=False)
    print(f'Контакт {edit_id} изменен')
    return(content)


def find_contact(content):
    """
    Поиск контакта по ключевому слову
    """
    keyword = input('Введите слово для поиска: ').lower()
    results = {}
    for contact_id, info in content.items():
        if (keyword in info["name"].lower() or
            keyword in info["phone"].lower() or
            keyword in info["comment"].lower()):
            results[contact_id] = info
    if results:
        print('\nНайденные контакты:')
        pprint(results, sort_dicts=False)
    else:
        print('Контакты не найдены')



def main():
    '''
    Выводит список возможных действий
    '''
    content = get_phonebook()
    while True:
        print("\nТелефонный справочник")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Редактировать контакт")
        print("5. Найти контакт")
        print("0. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            show_contact(content)
        elif choice == "2":
            content = add_contact(content)
        elif choice == "3":
            content = del_contact(content) 
        elif choice == "4":
            content = edit_contact(content)
        elif choice == "5":
            find_contact(content)
        elif choice == "0":
            print('Завершение программы')
            break
        else:
            print("Некорректное значение")
   
   

if __name__ == "__main__":
    main()