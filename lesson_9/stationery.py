class Stationary:
    title = 'Start rendering'

    def draw(self):
        print(f'{self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'{Stationary.title} with Pen')


class Pencil(Stationary):
    def draw(self):
        print(f'{Stationary.title} with Pencil')


class Handle(Stationary):
    def draw(self):
        print(f'{Stationary.title} with Handle')


s = Stationary()
print(s.title)
s.draw()
p = Pen()
p.draw()
pc = Pencil()
pc.draw()
h = Handle()
h.draw()
