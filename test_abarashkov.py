from math import pi
import random


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """

    # Переменные
    name = "Анна"
    age = 25

    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """

    # Переменные
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = 2 * (a + b)

    # Проверяем результат
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b

    # Проверяем результат
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """

    # Переменная
    r = 23

    # TODO сосчитайте площадь
    area = pi * r ** 2

    # Проверяем результат
    assert area == 1661.9025137490005
    print(area)

    # TODO сосчитайте длину окружности
    length = 2 * pi * r

    # Проверяем результат
    assert length == 144.51326206513048
    print(length)


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    num_list = random.sample(range(1, 101), 10)

    # Num list sort
    num_list.sort()

    # Проверяем результаты
    assert len(num_list) == 10
    assert num_list[0] < num_list[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """

    # Переменная
    massive_list = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    # TODO удалите повторяющиеся элементы
    massive_list = list(set(massive_list))

    # Проверяем результаты
    assert isinstance(massive_list, list)
    assert len(massive_list) == 10
    assert massive_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.

    Подсказка: используй встроенную функцию zip.
    """

    # Переменные
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    # TODO создайте словарь
    d = dict(zip(first, second))

    # Показать значение словаря
    print(d.values())

    # Проверяем результаты
    assert isinstance(d, dict)
    assert len(d) == 5
