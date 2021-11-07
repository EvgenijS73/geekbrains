class Road:
    def __init__(self, _length, _width, _depth):
        self._length = _length
        self._width = _width
        self._depth = _depth

    def mass_of_asphalt(self):
        mass_per_cm = 25
        total_mass = ((self._length * self._width * mass_per_cm * self._depth) / 1000)
        print(f'For covering all the road will require {round(total_mass, 3)} ton(s) of asphalt')


r = Road(3667, 17.95, 7.5)
r.mass_of_asphalt()
