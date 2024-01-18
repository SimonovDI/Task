from logic.beverage_choice import ChoiceDrink


class AcceptingMoney:
    """Приём денег"""

    def __init__(self):
        self.wallet = []  # кошелек
        self.money = None  # внесенные деньги
        self.sum_money = 0  # общая сумма внесенных денег
        self.products = {"Чай": 50,
                         "Кофе": 100,
                         "Сок": 120}
        self.lst_coin = [0, 5, 10, 20, 50]  # список разрешенных денег

    def get_money(self, money=0):

        """Получение денег"""

        self.money = money
        self.wallet.append(self.money)
        print('Чай: 50\nКофе: 100\nСок: 120')
        self.money = int(input('Вставьте купюру: '))
        valid_coin = AcceptingMoney()
        self.money = valid_coin.check_valid_coin(self.money)    # проверяем деньги на валидность по монетам

        while self.money != 0:

            # добавляем в кошелек пока покупатель не остановится и не введет 0

            self.wallet.append(self.money)
            self.money = int(input('Вставьте купюру: '))
            self.money = valid_coin.check_valid_coin(self.money)
        accepting_money = AcceptingMoney()
        accepting_money.check_for_fake(self.wallet)     # "проверяем на фальшивку" + суммируем сумму внесенных денег
        return 'Напиток готов!'

    def check_for_fake(self, wallet):

        """Детектор банкнот + считает количество внесенных денег """

        for item_money in wallet:       # считаем общею внесенную сумму денег
            self.sum_money += item_money
        money = AcceptingMoney()
        money.check_minimum_amount(self.sum_money)  # проверка на минимальную сумму покупки.

    def check_minimum_amount(self, sum_money):

        """Проверка на минимальную сумму покупки"""

        min_sum = min(list(self.products.values()))     # в словаре ищем минимальное значение товара

        # проверяем на минимальную суммы покупки, если сумма внесенных денег меньше, то
        # очищаем кошелек от общей суммы внесенных денег, создаем экземпляр + передаем в новый экземпляр
        # общую сумму денег.

        if sum_money < min_sum:
            print('\nНедостаточная сумма для покупки\n')
            self.wallet.clear()
            new_wallet = AcceptingMoney()
            new_wallet.get_money(sum_money)
        choice_drink = ChoiceDrink()
        choice_drink.product(sum_money)

    def check_valid_coin(self, coin):

        """Проверка на валидность внесенных денег"""

        while coin not in self.lst_coin:
            print(f'Мы не принимаем {coin}, Вставьте купюру только 5,10,20,50')
            coin = int(input('Вставьте купюру: '))
        return coin
