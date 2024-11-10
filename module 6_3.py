class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed : int | float) -> None:
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx : int | float, dy : int | float, dz : int | float) -> None:
        if self.speed * dz + self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += self.speed * dx
            self._cords[1] += self.speed * dy
            self._cords[2] += self.speed * dz

    def get_cords(self) -> None:
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self) -> None:
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self) -> None:
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self) -> None:
        from random import randint
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz : int | float) -> None:
        self._cords[2] -= abs(dz) / 2 * self.speed


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):

    def __init__(self, speed : int | float) -> None:
        super().__init__(speed)
        self.sound = 'Click-click-click'


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
