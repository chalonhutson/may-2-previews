class Superhero:

    POWER_FACTOR = 10

    num_of_superheros = 0

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power * Superhero.POWER_FACTOR
        Superhero.num_of_superheros += 1

    def punch(self, superhero):
        print(f"{self.name} is attempting to punch {superhero.name}!")
        superhero.health = superhero.health - self.power
        if superhero.health <= 0:
            superhero.die()
        else:
            print(f"{superhero.name} survived the attacked and has {superhero.health} left!")

    def die(self):
        print(f"{self.name} has died. F in the chat......")

    def return_num_of_superheros(cls):
        return cls.num_of_superheros