import json


class ATM:

    """Класс имитирующий работу банкомата, данных сохраняются в JSON"""

    def __init__(self):
        self.pin = 0        # пин-код
        self.count = 0      # счетчик количества попыток ввода пин-кода
        self.id_card = ' '  # № карты
        self.data = {}      # dict который хранит данные о карточке
        self.lst_data = []  # список с dict, который будет записываться в файл

    def access(self):

        """Получить доступ"""
        try:
            self.id_card = input('Введите номер карты: ')
            pin = int(input('Введите пин-код: '))

            data_pin, data_block, self.data = self.input_data()     # проверка на валидность данных
            self.count += 1
            if data_block == 'True':
                return 'Карта заблокирована'

            while data_pin != pin:

                pin = int(input('Введите пин-код: '))
                self.count += 1
                if data_pin == pin:
                    continue
                if self.count == 3:
                    self.recording_data('access_' + 'True')     # блокируем карту
                    return 'Карта заблокирована'
            else:
                self.count = 0
                return self.deposit_or_withdraw_money()

        except Exception as ex:
            raise f'{ex} - Ошибка ввода данных в access'

    def deposit_or_withdraw_money(self):

        """Внести, получить, просмотр счета"""
        try:
            number = int(input("Снять деньги - 1, Пополнить счет - 2, Просмотр счета - 3: "))

            if number == 1:
                sum_withdraw = int(input("Введите сумму снятия: "))
                negative_balance = self.recording_data('withdraw_' + str(sum_withdraw))
                if negative_balance == -1:
                    return "Не достаточно денег"
                return "Не забудь карту!"

            if number == 2:
                sum_rec = int(input("Введите сумму пополнения: "))
                self.recording_data('record_' + str(sum_rec))
                return "Баланс пополнен"

            if number == 3:
                load_data = self.load_data()
                for item in load_data:
                    if item['id'] == self.id_card:
                        name = item['name']
                        last_name = item['lastname']
                        sum_money = item['amount']
                        return f"\nИмя: {name}\nФамилия: {last_name}\nСумма: {sum_money}"
            return 'Нет такой цифры'

        except Exception as ex:
            raise f'{ex} - Ошибка ввода данных в deposit_or_withdraw_money'

    def input_data(self):

        """Проверка входных данных на актуальность и корректность"""
        try:

            data = self.load_data()
            for item in data:
                if item['id'] == self.id_card:
                    data_pin = item['pin']
                    data_block = item['block']
                    return data_pin, data_block, item

        except Exception as ex:
            raise f'{ex} - Ошибка в блоке input_data'

    def load_data(self):

        """Чтение данных из файла"""
        try:

            with open('logic/database.json', 'r') as file:
                data = json.load(file)
            return data

        except FileNotFoundError:
            raise 'Нет файла'

    def recording_data(self, methond):

        """Записать данные в файл"""

        data = self.data  # данные из выбранной карты
        load_data_from_file = self.load_data()
        for item in load_data_from_file:
            self.lst_data.append(item)
            if item['id'] == data['id']:
                meth_data = self.method_data(methond, item)
                if meth_data == -1:     # проверка на отрицательную итоговую сумму для выдачи
                    return -1

        with open('logic/database.json', 'w') as file:
            file.write(json.dumps(self.lst_data, indent=4))

        return self.lst_data

    def method_data(self, method, data):

        """Обработка методов доступ, запись, просмотр счета"""
        try:

            method_definition = method.split('_')
            if method_definition[0] == 'access':
                data['block'] = 'True'
            if method_definition[0] == 'record':
                data['amount'] += int(method_definition[1])
            if method_definition[0] == 'withdraw':
                balance_money = data['amount']
                if balance_money - int(method_definition[1]) < 0:
                    return -1
                data['amount'] -= int(method_definition[1])

        except Exception as ex:
            raise f'{ex} Ошибка в блоке method_data'
