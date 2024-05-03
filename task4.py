# reestr(['key'], "маша")
list_players = ["маша", "петя", "саша", "оля", "киилл"]
last_player = list_players[-1]
reestr = {'первый игрок': list_players[0]}
print('первый участник', reestr["первый игрок"])
print('последний участник', last_player)


list_partipants = ["орлов", "петров", "иванов", "сидоров", "васильев", "черепахин"]
last_partipant = list_partipants[-1]
winnner = {'первый лыжник': list_partipants[0]}
print('первый лыжник', winnner["первый лыжник"])
print('последний лыжник', last_partipant)


sps_book = ["Дубровский", "Горе от ума", "Кавказский пленник", "Хамелеон", "Ревизор", "Гранатовый браслет"]
last_book = sps_book[-1]
book = {'первая книга': sps_book[0]}
print('последняя книга',last_book)
print('первая книга',book['первая книга'])

shopping_list = ["Палатка", "Спальник", "Котелок", "Тренога", "Рюкзак", "Спальник", "Рюкзак", "Термос", "Миска", "Ветровка", "Коврик"]
unique_items = set(shopping_list)
len(unique_items)
print("Количество уникальных товаров:", len(unique_items))
