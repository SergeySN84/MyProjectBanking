import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстура для тестовых данных
@pytest.fixture
def tests_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

# Тесты для функции filter_by_state с параметризацией
@pytest.mark.parametrize(
    "state, expected",
    [
        # Тест фильтрации по умолчанию (state='EXECUTED')
        ("EXECUTED", [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]),
        # Тест фильтрации с указанием state='CANCELED'
        ("CANCELED", [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]),
        # Тест фильтрации с несуществующим state
        ("UNKNOWN", [])
    ]
)
def test_filter_by_state(tests_data, state, expected):
    """Параметризованный тест фильтрации по состоянию"""
    result = filter_by_state(tests_data, state=state)
    assert result == expected

# Тесты для функции sort_by_date с параметризацией
@pytest.mark.parametrize(
    "reverse, expected",
    [
        # Тест сортировки по убыванию (reverse=True)
        (True, [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]),
        # Тест сортировки по возрастанию (reverse=False)
        (False, [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ])
    ]
)
def test_sort_by_date(tests_data, reverse, expected):
    """Параметризованный тест сортировки по дате"""
    result = sort_by_date(tests_data, reverse=reverse)
    assert result == expected

# Отдельный тест для пустого списка
def test_sort_by_date_empty():
    """Тест сортировки пустого списка"""
    result = sort_by_date([])
    assert result == []