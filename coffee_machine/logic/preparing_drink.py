import time


class PreparingDrink:
    """Приготовление напитка"""

    @staticmethod
    def preparing_drink():
        for _ in range(10):
            print(end='*' * 1)
            time.sleep(0.5)
        return f'готов'


