"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.Car import Car


def main():
    # """Demo test code to show how to use car class."""
    # my_car = Car(180)
    # my_car.drive(30)
    # print("fuel =", my_car.fuel)
    # print("odo =", my_car.odometer)
    # print(my_car)
    #
    # print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # 1
    limo = Car("Limo", 100)

    # 2
    limo.add_fuel(20)

    # 3
    print(limo.fuel)

    # 4 and 5
    limo.drive(115)

    # 5
    print(limo.drive(115))

    # 6
    print(limo.__str__())

    # 7
    mini = Car("Mini", 200)
    mini.drive(100)
    print(mini.__str__())

    monster_mash_machine = Car("Monster Mash Machine", 50)
    monster_mash_machine.drive(40)
    print(monster_mash_machine.__str__())


main()
