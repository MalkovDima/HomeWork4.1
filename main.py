cook_book = {}
h = ['Омлет', 'Запеченный картофель']


def print_cook(menu):
    dish = menu.readline().strip()
    n = int(menu.readline().strip())
    ingredient_list = []
    ingredient_dict = {}
    i = 0
    for i in range(n):
        str_ind = menu.readline().strip()
        ingredient_dict['ingredient_name'] = str_ind[0:str_ind.find(' | ')]
        str_ind = str_ind[str_ind.find(' | ')+3:]
        ingredient_dict['quantity'] = int(str_ind[0:str_ind.find(' | ')])
        str_ind = str_ind[str_ind.find(' | ') + 3:]
        ingredient_dict['measure'] = str_ind
        ingredient_list.append(ingredient_dict)
        ingredient_dict = {}
    cook_book[dish] = ingredient_list
    menu.readline()


def empty_str(file_name):
    with open('cook.txt') as file:
        lst = [i for i in file.readlines() if '\n' == i]
    return len(lst)


def all_menu():
    with open('cook.txt') as file_cook:
        for g in range(empty_str(file_cook)+1):
            print_cook(file_cook)
    return cook_book


def print_menu(list_menu):
    with open('cook.txt') as file_cook:
        list_dish = []
        print("Меню нашего заведения:")
        for key in list_menu:
            list_dish.append(key)
        print(list_dish)


def get_shop_list_by_dishes(dishes: list, person_count: int):
    all_product = {}
    for i in dishes:
        for n in cook_book[i]:
            name = n['ingredient_name']
            n.pop('ingredient_name')
            if name in all_product.keys():
                all_product[name]['quantity'] += n['quantity']
            else:
                all_product[name] = n
    if person_count >1:
        for k in all_product.values():
            k['quantity'] *= person_count
    for key, value in all_product.items():
        print(key, ':', value)
    return all_product


all_menu()
print(cook_book)
print('+++++++++')
print_menu(cook_book)
print('+++++++++')
get_shop_list_by_dishes(h, 9)

