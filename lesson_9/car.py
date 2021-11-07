class Car:
    def __init__(self, name, second_name, colour, speed, is_police=True):
        self.name = name
        self.second_name = second_name
        self.colour = colour
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} drove!')

    def stop(self):
        print(f'{self.name} stopped!')

    def turn(self):
        direction = input('Input the direction: ')
        if direction == 'left':
            print(f'{self.name} turn to the left!')
        else:
            print(f'{self.name} turn to the right!')

    def show_speed(self):
        print(f'{self.name} speed: {self.speed} km/h')


class TownCar(Car):
    def __init__(self, name='Toyota', second_name='Corolla', colour='Wind Chill Pearl',
                 speed=int(input('Enter the speed: '))):
        super().__init__(name, second_name, colour, speed)

    def info(self):
        print(f'{self.name} {self.second_name}, colour: {self.colour}, speed: {TownCar.show_speed(self)}')

    def show_speed(self):
        speed = self.speed
        if speed > 60:
            self.speed = f"You're driving about {speed - 60} kilometres an hour over the speed limit."
        else:
            self.speed = f'{self.name} speed: {speed} km/h'

        return self.speed


class WorkCar(Car):
    def __init__(self, name='UAZ', second_name='Patriot', colour='Dirty green', speed=int(input('Enter the speed: '))):
        super().__init__(name, second_name, colour, speed)

    def info(self):
        print(f'{self.name} {self.second_name}, colour: {self.colour}, speed: {WorkCar.show_speed(self)}')

    def show_speed(self):
        speed = self.speed
        if speed > 40:
            self.speed = f"Amazing! You're driving about {speed - 40} kilometres an hour over the speed limit."
        else:
            self.speed = f'{self.name} speed: {speed} km/h'

        return self.speed


class SportCar(Car):
    def __init__(self, name='Porsche', second_name='718 "Cayman"', colour='Midnight black', speed=120):
        super().__init__(name, second_name, colour, speed)

    def info(self):
        print(f'{self.name} {self.second_name}, colour: {self.colour}, speed: {self.speed}')


class PoliceCar(Car):
    def __init__(self, name='Chevrolet', second_name='Tahoe', colour='Black', speed=120):
        super().__init__(name, second_name, colour, speed)

    def info(self):
        print(f'{self.name} {self.second_name}, colour: {self.colour}, speed: {self.speed}')


c = Car('ford', 'focus', 'gray', 100)
c.turn()
c.show_speed()
c.name = 'nissan'
c.go()
t = TownCar()
t.info()
t = TownCar(colour='Blue')
t.info()
w = WorkCar()
w.info()
p = PoliceCar()
p.info()
p = PoliceCar(name='Ford', second_name='Escalade')
p.info()
s = SportCar()
s.info()
