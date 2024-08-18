def filter_by_state(dictionary_list: list[dict[str]], state="EXECUTED") -> list[dict[str]]:
    """Функция сортировки словарей по ключу state"""
    sort_dictionary = []
    for dictionary_executed in dictionary_list:
        if dictionary_executed["state"] == state:
            sort_dictionary.append(dictionary_executed)
        elif dictionary_executed["state"] != state:
            continue
    return sort_dictionary


def sort_by_date(dictionary_list_sort: list[dict[str, int]], revers_list: bool = True) -> list[dict[str, int]]:
    """ Функция сортировки словарей по дате """
    sorted_list = sorted(dictionary_list_sort, key=lambda x: x["date"], reverse=revers_list)
    return sorted_list
