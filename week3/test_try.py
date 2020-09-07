class Planet:
    count = 0

    def __init__(self, name, population = None):
        self.name = name
        self.population = population or []
        Planet.count += 1


earth = Planet("Earth")
mars = Planet("Mars")
print(earth.__dict__)
earth.mass = 123124
print(earth.mass)
print(earth.__dict__)
