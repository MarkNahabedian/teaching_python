
import random


class World (object):
    def __init__(self, size):
        self.size = size
        self.critters = []

    def check_position(self, position):
        """check_position checks to see that position is within the World and
        returns a corrected position."""
        if position < 0:
            return 0
        if position > self.size:
            return self.size
        return position

    def show(self):
        where = {}
        for critter in self.critters:
            if critter.position in where:
                print("CRASH! %s %s" % (critter, where[critter.position]))
                return
            where[critter.position] = critter
        view = ""
        for position in range(0, self.size + 1):
            if position in where:
                view += where[position].show_as
            else:
                view += "."
        print view

    def step(self):
        for critter in self.critters:
            critter.peek(self)
        for critter in self.critters:
            critter.move(self)
        self.show()
        

class Mouse (object):
    def __init__(self, world):
        self.show_as = "m"
        world.critters.append(self)
        # The mouse starts in the middle of the world:
        self.position = world.size / 2

    def __str__(self):
        return "mouse"

    def peek(self, world):
        # The mouse doesn't think about where he's going
        pass

    def move(self, world):
        # The mouse can move up to three spaces in either direction, randomly
        self.position = world.check_position(
            random.randint(self.position - 3,
                           self.position + 3))


class Cat (object):
    def __init__(self, world):
        self.show_as = "C"
        world.critters.append(self)
        self.position = 0

    def __str__(self):
        return "cat"

    def peek(self, world):
        # The cat pounces to where the mouse was last.
        for critter in world.critters:
            if isinstance(critter, Mouse):
                self.mouse_last = critter.position
                break

    def move(self, world):
        self.position = world.check_position(self.mouse_last)


world = World(30)
Mouse(world)
Cat(world)
world.show()
