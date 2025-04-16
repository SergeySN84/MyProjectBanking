"""Переменная со словаоем для проверки функций"""

users_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(date_list: list, state: str = "EXECUTED") -> list:

    """Функция для фильтрации словарей в списке по заданному ключу"""

    filtered_list = [i for i in date_list if i["state"] == state]

    return filtered_list


def sort_by_date(date_list: list, vector: bool = True) -> list:

    """Функция сортировки списка словарей по дате"""

    return sorted(date_list, key=lambda i: i["date"], reverse=vector)


a = filter_by_state(users_data)
print(a)
