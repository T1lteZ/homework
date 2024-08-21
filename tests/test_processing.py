from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(state_list):
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]) == state_list


def test_sort_by_date(date_list):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33'}]) == date_list
