#! /usr/bin/env python3
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.GoldenEgg import Eggs

class Test_Eggs:
    __count = 3
    @pytest.fixture()
    def eggs(self):
        return Eggs(self.__count)

    def test_random_number(self, eggs):
        generated_numbers = set()
        for x in range(10):
            number = eggs.get_random_number()
            generated_numbers.add(number)
            print()
            print("%d -> Random number: %d" % (x, number), end='')
            assert number > 0 and number <=self.__count

        for x in range(1, self.__count):
            assert (x in generated_numbers) is True

    def test_initialize(self, eggs):
        initialized_eggs = eggs.initialize()
        assert len(initialized_eggs) == self.__count
        # The Egg with value 1 is golden egg and any one egg should be initialized with 1
        assert (1 in initialized_eggs) is True
        assert (0 in initialized_eggs) is True  # Normal eggs are initialized with 0
        assert initialized_eggs.count(0) == self.__count - 1  # Count of Eggs with 0 will be 2
        assert initialized_eggs.count(1) == 1  # Count of Eggs with 1 will be 1

