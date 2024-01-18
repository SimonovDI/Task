class HandingMoney:
    """Сдача"""

    def __init__(self):
        self.money = 0
        self.change = 0
        self.exchange = 0
        self.money_bills = [10, 5]
        self.lst_coin = {}

    def give_change(self, money, change):

        """ Выдаем сдачу одной суммой"""

        self.change = change
        self.money = money
        result = self.money - self.change
        return result

    def money_exchange(self, rest_of_money):

        """Разбиваем сумму на номинал 5 и 10 рублей"""

        self.exchange = rest_of_money
        while self.exchange != 0:
            for i in self.money_bills:
                coin = self.exchange // i
                self.lst_coin[f'Монета {i} руб. -> '] = coin
                self.exchange %= 10
            self.exchange //= 10
        return self.lst_coin
