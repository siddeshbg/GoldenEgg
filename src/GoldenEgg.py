import random


class Eggs:

    def __init__(self, count):
        self.count = count

    def get_random_number(self):
        return random.randint(1, self.count)

    def initialize(self):
        eggs = []
        num = self.get_random_number()
        for x in range(1, self.count + 1):
            if x == num:
                eggs.insert(x, 1)  # The Egg with value 1 is golden egg
            else:
                eggs.insert(x, 0)  # The Egg with value 0 is normal egg
        return eggs

    def play(self):
        unlocked_eggs = []
        eggs = self.initialize()
        print("Welcome to Egg blasting game")
        print("One Egg contains Gold coin and you blast other eggs to win it")

        while len(unlocked_eggs) < self.count:
            print("Which Egg you want to blast?")
            if len(unlocked_eggs) == 0:
                print("*" * 30)
                for x in range(1, self.count + 1):
                    print("EGG-%s|" % x, end='')
                print()
                print("*" * 30)
            else:
                print("*" * 30)
                for x in range(1, self.count + 1):
                    if x not in unlocked_eggs:
                        print("EGG-%s|" % x, end='')
                print()
                print("*" * 40)

            while True:
                your_choice = input("\nEGG? ")
                if int(your_choice) not in unlocked_eggs:
                    break
                else:
                    print("You have already blasted this egg. Choose another Egg..")

            if eggs[int(your_choice) - 1] == 1:
                print("Oh no..... you blasted the Golden Egg and you lost!!")
                exit(0)
            else:
                print("Good job !! you knocked out one normal egg")

            unlocked_eggs.append(int(your_choice))

            if len(unlocked_eggs) == 2:
                print("***** You won *********")
                break
        return eggs


