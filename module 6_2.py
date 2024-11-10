class Vehicle:
    __COLOR_VARIANTS = ['default', 'blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner : str, model : str, color : str, engine : int) -> None:
        self.owner = owner
        self.__model = model
        self.__engine_power = engine
        self.__color = 'default'
        self.set_color(color)

    def get_model(self) -> str:
        return f'Модель: {self.__model}'

    def get_horsepower(self) -> str:
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self) -> str:
        return f'Цвет: {self.__color}'

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color : str) -> None:
        color = new_color.lower()
        if color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print()
vehicle1.print_info()
