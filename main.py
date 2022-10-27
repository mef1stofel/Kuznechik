
def validate_input(msg: str, sup: int = 10_000_000_000) -> int:
    """Validates input value and converts it into integer"""
    val = 0
    while sup < val <= 0:
        try:
            val = int(input(msg))
        except ValueError:
            continue
    return val


def calculate_leaps(circle_length: int, leap_length: int) -> int:
    """Compute a minimum count of leaps to achieve the same point of the circle """
    short_leaps_count = circle_length // leap_length  # целое число прыжков в круге
    short_reminder = circle_length % leap_length  # остаток недопрыгнутого

    long_leap_length = leap_length + 1
    long_leaps_count = circle_length // long_leap_length  # целое число длинных прыжков в круге
    long_reminder = circle_length % long_leap_length  # остаток недопрыгнутого при длинных прыжках

    # Возможные случаи:
    #
    # 1. leaps_count == 0
    #   Кузнечик прыгает дальше, чем длина круга, тогда reminder - насколько он дальше прыгает
    #
    # 2. leaps_count > 0, reminder == 0: НО!
    #   Длина круга делится нацело на длину прыжка
    #       2.1. long_leaps_count > 0, long_reminder == 0 Если каждый прыжок учвеличить +1
    #           return long_leaps_count
    #       2.2  long_leaps_count > 0, 0 < long_reminder <= long_leaps_count

    #
    # 3. leaps_count > 0, 0 < reminder <= leaps_count:
    #   Можем добрать недостающее, добавляя +1м к некоторым прыжкам
    #
    # 4. leaps_count > 0, reminder > leaps_count:
    #   надо прыгать несколько кругов
    #       4.1 Проверяем для circle_length*2 и leap_length
    # TODO: Выяснить, могут ли  быть другие случаи?

    # if leaps_count > 0 and 0 <= reminder <= leaps_count:  # 2, 3 случай
    #     return leaps_count


if __name__ == '__main__':
    n = validate_input('Введите длину окружности')
    k = validate_input('Введите длину прыжка')
    leaps_count = calculate_leaps(n, k)

    print(leaps_count)


