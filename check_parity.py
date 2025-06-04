def check_parity(n: int) -> str:
    """Перевіряє парність числа.

    Параметри:
        n (int): число для перевірки

    Повертає:
        str: "Парне" якщо n парне, і "Непарне" інакше
    """
    return "Even" if n % 2 == 0 else "Odd"


if __name__ == "__main__":
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Error: it is not number")
    else:
        print(check_parity(number))

