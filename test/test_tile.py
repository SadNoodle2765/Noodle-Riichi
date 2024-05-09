import unittest

from src.tile import Tile
from src.suit import Suit, HonorType

class TestTile(unittest.TestCase):
    def test_init_sets_non_honor_correctly(self):
        temp = Tile(Suit.MANZU, 5, red_dora=True)
        self.assertEqual(temp._suit, Suit.MANZU)
        self.assertEqual(temp._number, 5)
        self.assertEqual(temp._honor_type, HonorType.NULL)
        self.assertEqual(temp._red_dora, True)

    def test_init_sets_honor_correctly(self):
        temp = Tile(Suit.HONOR, honor_type=HonorType.HAKU)
        self.assertEqual(temp._suit, Suit.HONOR)
        self.assertEqual(temp._number, 0)
        self.assertEqual(temp._honor_type, HonorType.HAKU)
        self.assertEqual(temp._red_dora, False)

    def test_validate_suit_type_correct(self):
        Tile._validate(Suit.MANZU, 3, HonorType.HAKU, False)

    def test_validate_suit_type_incorrect(self):
        with self.assertRaises(TypeError):
            Tile._validate(5, 3, HonorType.HAKU, False)

    def test_validate_number_type_correct(self):
        Tile._validate(Suit.MANZU, 3, HonorType.HAKU, False)

    def test_validate_number_type_incorrect(self):
        with self.assertRaises(TypeError):
            Tile._validate(Suit.MANZU, 'A', HonorType.HAKU, False)

    def test_validate_honor_type_type_correct(self):
        Tile._validate(Suit.HONOR, 0, HonorType.HAKU, False)

    def test_validate_honor_type_type_incorrect(self):
        with self.assertRaises(TypeError):
            Tile._validate(Suit.HONOR, 0, 5, False)

    def test_validate_red_dora_type_correct(self):
        Tile._validate(Suit.MANZU, 3, HonorType.NULL, False)

    def test_validate_red_dora_type_incorrect(self):
        with self.assertRaises(TypeError):
            Tile._validate(Suit.MANZU, 4, HonorType.NULL, 321)

    def test_validate_number_suit_number_in_range(self):
        Tile._validate(Suit.MANZU, 1, HonorType.NULL, False)
        Tile._validate(Suit.PINZU, 9, HonorType.NULL, False)
        Tile._validate(Suit.SOUZU, 1, HonorType.NULL, False)

    def test_validate_number_suit_number_out_of_range(self):
        with self.assertRaises(ValueError):
            Tile._validate(Suit.MANZU, 0, HonorType.NULL, False)
        with self.assertRaises(ValueError):
            Tile._validate(Suit.PINZU, 10, HonorType.NULL, False)
        with self.assertRaises(ValueError):
            Tile._validate(Suit.PINZU, -5, HonorType.NULL, False)
        with self.assertRaises(ValueError):
            Tile._validate(Suit.SOUZU, 20, HonorType.NULL, False)
    

if __name__ == '__main__':
    unittest.main()