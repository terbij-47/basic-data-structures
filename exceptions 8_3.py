class Car:

    @staticmethod
    def __is_valid_vin(vin : int) -> bool:
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin < 1000000 or vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    @staticmethod
    def __is_valid_number(number : str) -> bool:
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

    def __init__(self, model : str, vin : int, numbers : str) -> None:
        self.model = model
        self.__is_valid_vin(vin)
        self.__vin = vin
        self.__is_valid_number(numbers)
        self.__numbers = numbers


class IncorrectVinNumber(Exception):
    def __init__(self, message : str) -> None:
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message : str) -> None:
        self.message = message


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
