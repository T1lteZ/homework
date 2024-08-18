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