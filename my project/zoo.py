class Cage:
    def __init__(self, spece):
        self.animal_in_cage = []
        self.space = spece

    def add(self, animal) -> bool:
        if self.space < animal.space:
            return False
        self.space -= animal.space
        self.animal_in_cage.append(animal.name)
        return True

    def free_space(self) -> int:
        return self.space

    def get_animal(self) -> list:
        return self.animal_in_cage


class Animal:
    def __init__(self, name, space):
        self.name = name
        self.space = space


cage = Cage(200)
lion = Animal("Alex", 100)
pingvin1 = Animal("Gunter", 15)
pingvin2 = Animal("Ganter", 25)
begimot = Animal("Gloria", 300)
giraffe = Animal("Melman", 70)

(cage.add(pingvin1))                        # True
(cage.add(begimot))                         # False
(cage.free_space())                         # 185
(cage.add(lion))                            # True
(cage.free_space())                         # 85
(cage.add(pingvin2))                        # True
(cage.add(giraffe))                         # False
(cage.get_animal())                         # ['Gunter', 'Alex', 'Melman']
