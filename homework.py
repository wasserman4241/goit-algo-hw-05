def caching_fibonacci():
    
    cache = {}

    def fibonacci(n: int) -> int:
        # Якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        if n == 1:
            return 1
        # Якщо значення вже є в кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Обчислюємо рекурсивно, зберігаємо у кеш та повертаємо результат
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Приклад використання:
if __name__ == "__main__":
    # Отримуємо функцію fibonacci з кешуванням
    fib = caching_fibonacci()

    # Обчислюємо числа Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610