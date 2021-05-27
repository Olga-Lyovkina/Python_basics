# task_1
class TrafficLight:

    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        from time import sleep
        for num, i in enumerate(self.__color):
            print(f'Светофор переключается {i}')
            if num == 0:
                sleep(7)
            elif num == 1:
                sleep(2)
            elif num == 2:
                sleep(5)


traffic = TrafficLight()
traffic.running()


# task_2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width


    def calcul_mass(self):
        return (self._length * self._width * 25 * 5) / 1000


my_road = Road(4456.5, 2.5)
print(f'Необходимая масса асфальта: {my_road.calcul_mass():.2f} т.')

# task_3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name_worker(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Полный доход сотрудника: {sum(self._income.values())}'

worker = Position('Kate', 'Brawns', 'qa tester', 1400, 145)
print(worker.get_full_name_worker())
print(worker.get_total_income())

# task_4
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def direction(self):
        print(f'{self.name} развернулась')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} : {self.speed}')
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость 60 км/ч')
        else:
            Car.show_speed(self)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость 40 км/ч')
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police


class SportCar(Car):
    """Класс спортиный автомобиль"""


town_car = TownCar(59, 'blue', 'towncar_1')
town_car.show_speed()

work_car = WorkCar(40, 'red', 'workcar_1')
work_car.show_speed()

# task_5
class Stationery:

    def __init__(self, title):
        self.name = title

    def draw(self):
        print(f'Запуск отрисовки: {self.name}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой: {self.name}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом: {self.name}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером: {self.name}')


stat = Stationery('ластик')
stat.draw()

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()