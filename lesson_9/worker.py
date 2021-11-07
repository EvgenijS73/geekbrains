class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    # def __init__(self, name, surname, position, wage, bonus):
    def __init__(self, name=input('enter the name: '), surname=input('enter the surname: '),
                 position=input('enter the position: '), wage=int(input('enter the wage: ')),
                 bonus=int(input('enter the bonus: '))):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_income = Position.get_total_income(self)
        print(f'Fullname: {self.name} {self.surname}, position: {self.position}, income: {full_income}')

    def get_total_income(self):
        t_inc = self.income['wage'] + self.income['bonus']
        return t_inc


# w = Position('John', 'Silver', 'manager', 147, 56)
w = Position()
w.get_full_name()
