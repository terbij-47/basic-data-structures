class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start : float | int, stop : float | int, step : float | int = 1) -> None:
        self.pointer = start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self) -> 'Iterator':
        self.pointer = self.start - self.step
        return self

    def __next__(self) -> float | int:
        self.pointer += self.step
        if not self.step:
            raise StepValueError()
        elif self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        elif self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
        return self.pointer


try:
    for i in Iterator(100, 200, 0):
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

for i in Iterator(-5, 1):
    print(i, end=' ')
print()
for i in Iterator(6, 15, 2):
    print(i, end=' ')
print()
for i in Iterator(5, 1, -1):
    print(i, end=' ')
print()
for i in Iterator(10, 1):
    print(i, end=' ')
print()
for i in Iterator(1.1, 10.4, 2.3):
    print(i, end=' ')
