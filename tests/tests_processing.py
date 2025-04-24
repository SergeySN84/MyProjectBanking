import pytest

from src.processing import filter_by_state, sort_by_date

# Тестовые данные
users_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Тесты для функции filter_by_state
def test_filter_by_state_default():
    """Тест фильтрации по умолчанию (state='EXECUTED')"""
    expected_result = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    result = filter_by_state(users_data)
    assert result == expected_result

def test_filter_by_state_custom():
    """Тест фильтрации с указанием state='CANCELED'"""
    expected_result = [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    result = filter_by_state(users_data, state="CANCELED")
    assert result == expected_result

def test_filter_by_state_empty():
    """Тест фильтрации с несуществующим state"""
    result = filter_by_state(users_data, state="UNKNOWN")
    assert result == []

# Тесты для функции sort_by_date
def test_sort_by_date_descending():
    """Тест сортировки по убыванию (reverse=True)"""
    expected_result = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    result = sort_by_date(users_data, reverse=True)
    assert result == expected_result

def test_sort_by_date_ascending():
    """Тест сортировки по возрастанию (reverse=False)"""
    expected_result = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]
    result = sort_by_date(users_data, reverse=False)
    assert result == expected_result

def test_sort_by_date_empty():
    """Тест сортировки пустого списка"""
    result = sort_by_date([])
    assert result == []