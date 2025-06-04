def check_parity(n: int) -> str:
    """Перевіряє парність числа.

    Параметри:
        n (int): число для перевірки

    Повертає:
        str: "Парне" якщо n парне, і "Непарне" інакше
    """
    return "Парне" if n % 2 == 0 else "Непарне"


if __name__ == "__main__":
    try:
        number = int(input("Введіть число: "))
    except ValueError:
        print("Помилка: введено не число")
    else:
        print(check_parity(number))

