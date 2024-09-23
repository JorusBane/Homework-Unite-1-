class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car(Exception):
    def __init__(self, model, vin, numbers):
        Car.__is_valid_vin(vin)
        Car.__is_valid_numbers(numbers)
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    @staticmethod
    def __is_valid_vin(vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номер ")
        elif not (1000000 <= vin <= 9999999):
            raise IncorrectVinNumber("Некорректный тип vin номер ")
        else:
            return  True

    @staticmethod
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип для номеров ")
        elif int(len(numbers)) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        else:
            return  True



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
