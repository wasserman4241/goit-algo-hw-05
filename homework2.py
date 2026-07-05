import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Аналізує текст, ідентифікує всі дійсні числа, відокремлені пробілами з обох боків,
    та повертає їх як генератор.
    """
    pattern = r'(?<!\S)\d+(?:\.\d+)?(?!\S)'
    
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму чисел у вхідному рядку, використовуючи генератор.
    """
    return sum(func(text))

# Приклад використання:
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")