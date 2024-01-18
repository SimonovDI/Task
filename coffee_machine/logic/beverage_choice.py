from logic.preparing_drink import PreparingDrink
from logic.handing_money import HandingMoney


class ChoiceDrink:
    """Выбор напитка"""

    def __init__(self):
        self.pay = 0    # минимальная сумма в списке товара
        self.price = 0  # цена для проверки, что сумма покупки > 0
        self.change = 0  # сдача
        self.money = 0  # сумма внесенных денег
        self.coin = {}  # итоговая сумма сдачи разбитая по монетам
        self.choice = None  # Товар, который выбрал покупатель
        self.list_product = {"Чай": 50, "Кофе": 100, "Сок": 120}  # Дублирование

    def product(self, money):

        """Выбор товара"""

        self.money = money
        self.choice = input('Выберите товар из списка: ')
        while self.choice not in self.list_product:     # проверка на валидность запрашиваемого товара
            print('\nВыберите другой товар...')
            self.choice = input('Выберите товар из списка: ')

        check_pay = ChoiceDrink()
        self.pay = self.list_product.get(self.choice)
        pay = check_pay.check_pay(self.money, self.pay)     # проверяем что оплата > 0
        if pay == -1:
            self.choice = input('Не хватает денег, Выберите другой товар из списка: ')

        if self.choice in self.list_product:
            drink = PreparingDrink.preparing_drink()        # приготовление продукта
            if drink != 'готов':
                print('\n\nЧто-то пошло не так!')

        handing_over_money = HandingMoney()
        self.change = self.list_product.get(self.choice)    # По ключу получаем цену на запрашиваемый товар

        change = handing_over_money.give_change(self.money, self.change)    # сдача
        print('\nВаша сдача - ', change, 'руб.')

        money_exchange = HandingMoney()     # разбиваем сдачу на монеты по 5 рублей и 10
        self.coin = money_exchange.money_exchange(change)
        for item in self.coin.items():
            print(*item)

    def check_pay(self, money, price):

        """Проверка суммы"""

        self.money = money
        self.price = price
        total = self.money - self.price     # итоговая сумма покупки.
        if total >= 0:
            return self.money
        return -1
