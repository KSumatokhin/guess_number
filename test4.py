from math import sqrt
from typing import Optional, Union


def add_numbers(
        num_1: Union[int, float],
        num_2: Union[int, float]) -> Union[int, float]:
    return num_1 + num_2


def calculate_square_root(number: Union[int, float]) -> float:
    if number >= 0:
        return float(sqrt(number))
    else:
        raise ValueError('not defined for Negative numbers')


def calc(your_number: Union[int, float]) -> Optional[str]:
    if not your_number <= 0:
        square = calculate_square_root(your_number)
        return (
            'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {square}'
        )
    else:
        raise ValueError('not defined for Negative numbers')


num_1 = 10
num_2 = 5

print('Сумма чисел: ', add_numbers(num_1, num_2))

print(calc(25.5))
