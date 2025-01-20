import unittest
import numpy as np
from Field import Field

class TestField(unittest.TestCase):
    def test_create_mega_matrix(self):
        level_matrix = [[1, 0], [0, 1]]
        field = Field(level_matrix)
        field.create_mega_matrix()

        # Ожидаемая структура, основанная на выводе
        expected_mega_matrix = np.array([
            [0, 1, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0]
        ])
        np.testing.assert_array_equal(field.mega_matrix, expected_mega_matrix)

    def test_check_win_state(self):
        level_matrix = [[1, 0], [0, 1]]
        solve_matrix = np.array([
            [0, 1, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 0]
        ])
        field = Field(level_matrix)
        field.create_mega_matrix()

        self.assertTrue(field.check_win_state(solve_matrix))  # Ожидаем выигрыш

if __name__ == "__main__":
    unittest.main()