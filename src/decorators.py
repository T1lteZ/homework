from functools import wraps


def log(filename):
    """ декоратор для записи вызова функции в консоль или в mylog"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("my_function ok\n")
                else:
                    print("my_function ok\n")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}. Inputs {args}, {kwargs}\n")
                else:
                    print(f"my_function error: {e}. Inputs {args}, {kwargs}")
            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция складывания двух чисел"""
    return x + y


my_function(1, 0)
