# Проект "Виджет банковских операций клиента"
## Описание:
### Проект - это виджет для удобного мониторинга банковских операций клиента

## Установка:
### 1. Клонируйте репозиторий
```
git clone https://github.com/T1lteZ/homework.git
```
### 2. Установите зависимости
```
pip install -r requirements.txt
```
## Использование:
### Виджет может маскировать данные карт и аккаунта, сортировать словари и выводить дату в удобном формате

## Пример:
```
def get_date(date_: str) -> str | None:
    """Функция вывода времени"""
    result_date = f"{date_[8:10]}.{date_[5:7]}.{date_[0:4]}"
    return result_date

print(get_date("2024-03-11T02:26:18.671407"))

"11.03.2024"
```
## Тестирование
### Тестирование проекта проходит в директории tests. Покрытие проекта тестами выполняется на 90%

## Добавление модуля "generators"
### В данном модуле добавленны функции:
```
def card_number_generator(start, end):
    """Генератор номера карт"""
    for i in range(start, end + 1):
        card_num_gen = "0000000000000000"
        str_sum = card_num_gen + str(i)
        card_number = f"{str_sum[-16:-12]} {str_sum[-12:-8]} {str_sum[-8:-4]} {str_sum[-4:-1]}{str_sum[-1]}"
        yield card_number
```
### Данная функция генерирует номера карт

## Информация о логгерах
### В данном проекте добавленны логгеры для модулей mask и utils. Логгеры записываются в папку logs в корне проекта