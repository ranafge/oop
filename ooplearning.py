
class Crop:
    """ A generic food crop """ # docstring

    # construction
    def __init__(self, growth_rate,light_need, water_need):
       self._growth = 0
       self._days_growing = 0
       self._growth_rate = growth_rate
       self._light_need = light_need
       self._water_need = water_need
       self._status = "seed"
       self._type = 'Generic'

    def needs(self):
        # return a dictionary
        return {'light need': self._light_need, 'water need': self._water_need}

    def report(self):
        return {'Type': self._type, 'Status': self._status, 'growth': self._growth, 'days': self._days_growing}

    def update_status(self):
        if self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Seeding'
        elif self._growth ==0:
            self._status = 'seed'

    def grow(self, light , water):
        if light >=self._light_need and water > self._water_need:
            self._growth += self._growth_rate

        self._days_growing = 1

        self.update_status()


def main():
    # instantiate a class
    new_crop = Crop(50,50,50)
    print(new_crop.report())
    print(new_crop.grow(100,100))
    print(new_crop.report())



if __name__ == "__main__":
    main()
