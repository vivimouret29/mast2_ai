
import pytest
from unittest import TestCase

from game_of_life import *

class TestGameOfLife(TestCase):
    
    def test_setUp(self):
        self.game = GameOfLife(5, 5)
        self.evolve = self.game.evolve

    def test_a_cell_is_inside_the_grid(self):
        self.game = GameOfLife(5, 5)
        assert self.game._inside_grid((2, 2)) is (True)

    def test_a_cell_up_the_grid_is_not_inside(self):
        self.game = GameOfLife(5, 5)
        assert self.game._inside_grid((-1, 0)) is (False)

    def test_a_cell_down_the_grid_is_not_inside(self):
        self.game = GameOfLife(5, 5)
        assert self.game._inside_grid((5, 0)) is (False)

    def test_a_cell_left_to_the_grid_is_not_inside(self):
        self.game = GameOfLife(5, 5)
        assert self.game._inside_grid((0, -1)) is (False)

    def test_a_cell_right_to_the_grid_is_not_inside(self):
        self.game = GameOfLife(5, 5)
        assert self.game._inside_grid((0, 5)) is (False)

    def test_a_cell_without_neighbours_dies_of_underpopulation(self):
        self.game = GameOfLife(5, 5)
        evolution = self.game.evolve([
            (0, 0)
        ])

        assert (0, 0) not in evolution

    def test_a_cell_with_more_than_3_neighbours_dies_of_overpopulation(self):
        self.game = GameOfLife(5, 5)
        evolution = self.game.evolve([
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1)
        ])

        assert (1, 1) not in evolution

    def test_a_cell_does_not_spawn_outside_the_grid_limit(self):
        self.game = GameOfLife(3, 3)
        evolution = self.game.evolve([
            (0, 0), (0, 1), (0, 2)
        ])

        assert (-1, 1) not in evolution
    
    # def test_a_cell_spawns_when_it_has_3_neighbours(self):
    #     self.game = GameOfLife(5, 5)
    #     evolution = self.game.evolve([
    #         (0, 0), (0, 1),
    #         (1, 0),
    #     ])

    #     assert (1, 1) in evolution

    # def test_a_cell_stays_alive_when_it_has_2_neighbours(self):
    #     self.game = GameOfLife(5, 5)
    #     evolution = self.game.evolve([
    #         (0, 0), (0, 1), (0, 2)
    #     ])

    #     assert (0, 1) in evolution

    # def test_a_cell_stays_alive_when_it_has_3_neighbours(self):
    #     self.game = GameOfLife(5, 5)
    #     evolution = self.game.evolve([
    #         (0, 0), (0, 1), (0, 2),
    #                 (1, 1)
    #     ])

    #     assert (1, 1) in evolution