import unittest

from src.tile import Tile
from src.suit import Suit, HonorType

class TestTile(unittest.TestCase):
    ######### Test __init__ method #########

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
    
    ######### Test _validate method #########

    def test_validate_suit_type_correct(self):
        Tile._validate(Suit.MANZU, 3, HonorType.NULL, False)

    def test_validate_suit_type_incorrect(self):
        with self.assertRaises(TypeError):
            Tile._validate(5, 3, HonorType.NULL, False)

    def test_validate_number_type_correct(self):
        Tile._validate(Suit.MANZU, 3, HonorType.NULL, False)

    def test_validate_number_type_incorrect(self):
        with self.assertRaises(TypeError):
            Tile._validate(Suit.MANZU, 'A', HonorType.NULL, False)

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

    def test_validate_number_suit_honor_type_must_be_null(self):
        with self.assertRaises(ValueError):
            Tile._validate(Suit.MANZU, 1, HonorType.CHUN, False)

    def test_validate_number_suit_five_can_be_red_dora(self):
        Tile._validate(Suit.MANZU, 5, HonorType.NULL, True)

    def test_validate_number_suit_nonfive_cannot_be_red_dora(self):
        with self.assertRaises(ValueError):
            Tile._validate(Suit.MANZU, 3, HonorType.NULL, True)

    def test_validate_honor_suit_number_must_be_zero(self):
        with self.assertRaises(ValueError):
            Tile._validate(Suit.HONOR, 3, HonorType.NULL, False)

    def test_validate_honor_suit_honor_type_cannot_be_null(self):
        with self.assertRaises(ValueError):
            Tile._validate(Suit.HONOR, 0, HonorType.NULL, False)

    def test_validate_honor_suit_cannot_be_red_dora(self):
        with self.assertRaises(ValueError):
            Tile._validate(Suit.HONOR, 0, HonorType.HAKU, True)

    ######### Test getter methods #########

    def test_get_suit(self):
        tileManzu = Tile(Suit.MANZU, 3)
        tilePinzu = Tile(Suit.PINZU, 5)
        tileSouzu = Tile(Suit.SOUZU, 5, red_dora=True)
        tileHonor = Tile(Suit.HONOR, honor_type=HonorType.EAST)

        self.assertEqual(tileManzu.get_suit(), Suit.MANZU)
        self.assertEqual(tilePinzu.get_suit(), Suit.PINZU)
        self.assertEqual(tileSouzu.get_suit(), Suit.SOUZU)
        self.assertEqual(tileHonor.get_suit(), Suit.HONOR)

    def test_get_number(self):
        tileTerminal    = Tile(Suit.MANZU, 1)
        tileSimple      = Tile(Suit.PINZU, 7)
        tileFive        = Tile(Suit.SOUZU, 5)
        tileHonor       = Tile(Suit.HONOR, honor_type=HonorType.HATSU)

        self.assertEqual(tileTerminal.get_number(), 1)
        self.assertEqual(tileSimple.get_number(), 7)
        self.assertEqual(tileFive.get_number(), 5)
        self.assertEqual(tileHonor.get_number(), 0)

    def test_get_honor_type(self):
        tileNumber      = Tile(Suit.MANZU, 2)
        tileWind        = Tile(Suit.HONOR, honor_type=HonorType.SOUTH)
        tileDragon      = Tile(Suit.HONOR, honor_type=HonorType.HATSU)

        self.assertEqual(tileNumber.get_honor_type(), HonorType.NULL)
        self.assertEqual(tileWind.get_honor_type(), HonorType.SOUTH)
        self.assertEqual(tileDragon.get_honor_type(), HonorType.HATSU)

    ######### Test is x methods #########

    def test_is_honor(self):
        tileSimple      = Tile(Suit.SOUZU, 3)
        tileTerminal    = Tile(Suit.MANZU, 9)
        tileWind        = Tile(Suit.HONOR, honor_type=HonorType.NORTH)
        tileDragon      = Tile(Suit.HONOR, honor_type=HonorType.HAKU)

        self.assertFalse(tileSimple.is_honor())
        self.assertFalse(tileTerminal.is_honor())
        self.assertTrue(tileWind.is_honor())
        self.assertTrue(tileDragon.is_honor())
    
    def test_is_terminal(self):
        tileSimple          = Tile(Suit.SOUZU, 2)
        tileTerminalOne     = Tile(Suit.MANZU, 1)
        tileTerminalNine    = Tile(Suit.MANZU, 9)
        tileWind            = Tile(Suit.HONOR, honor_type=HonorType.NORTH)
        tileDragon          = Tile(Suit.HONOR, honor_type=HonorType.HAKU)

        self.assertFalse(tileSimple.is_terminal())
        self.assertTrue(tileTerminalOne.is_terminal())
        self.assertTrue(tileTerminalNine.is_terminal())
        self.assertFalse(tileWind.is_terminal())
        self.assertFalse(tileDragon.is_terminal())

    def test_is_simple(self):
        tileSimple          = Tile(Suit.SOUZU, 2)
        tileTerminalOne     = Tile(Suit.MANZU, 1)
        tileTerminalNine    = Tile(Suit.MANZU, 9)
        tileWind            = Tile(Suit.HONOR, honor_type=HonorType.NORTH)
        tileDragon          = Tile(Suit.HONOR, honor_type=HonorType.HAKU)

        self.assertTrue(tileSimple.is_simple())
        self.assertFalse(tileTerminalOne.is_simple())
        self.assertFalse(tileTerminalNine.is_simple())
        self.assertFalse(tileWind.is_simple())
        self.assertFalse(tileDragon.is_simple())

    def test_is_wind(self):
        tileSimple          = Tile(Suit.SOUZU, 2)
        tileTerminal        = Tile(Suit.MANZU, 1)
        tileEast            = Tile(Suit.HONOR, honor_type=HonorType.EAST)
        tileSouth           = Tile(Suit.HONOR, honor_type=HonorType.SOUTH)
        tileWest            = Tile(Suit.HONOR, honor_type=HonorType.WEST)
        tileNorth           = Tile(Suit.HONOR, honor_type=HonorType.NORTH)
        tileDragon          = Tile(Suit.HONOR, honor_type=HonorType.HAKU)

        self.assertFalse(tileSimple.is_wind())
        self.assertFalse(tileTerminal.is_wind())
        self.assertTrue(tileEast.is_wind())
        self.assertTrue(tileSouth.is_wind())
        self.assertTrue(tileWest.is_wind())
        self.assertTrue(tileNorth.is_wind())
        self.assertFalse(tileDragon.is_wind())

    def test_is_dragon(self):
        tileSimple          = Tile(Suit.SOUZU, 2)
        tileTerminal        = Tile(Suit.MANZU, 1)
        tileEast            = Tile(Suit.HONOR, honor_type=HonorType.EAST)
        tileSouth           = Tile(Suit.HONOR, honor_type=HonorType.SOUTH)
        tileHaku            = Tile(Suit.HONOR, honor_type=HonorType.HAKU)
        tileHatsu           = Tile(Suit.HONOR, honor_type=HonorType.HATSU)
        tileChun            = Tile(Suit.HONOR, honor_type=HonorType.CHUN)

        self.assertFalse(tileSimple.is_dragon())
        self.assertFalse(tileTerminal.is_dragon())
        self.assertFalse(tileEast.is_dragon())
        self.assertFalse(tileSouth.is_dragon())
        self.assertTrue(tileHaku.is_dragon())
        self.assertTrue(tileHatsu.is_dragon())
        self.assertTrue(tileChun.is_dragon())

    def test_is_red_dora(self):
        tileTerminal        = Tile(Suit.MANZU, 1)
        tileFive            = Tile(Suit.SOUZU, 5)
        tileRedDora         = Tile(Suit.PINZU, 5, red_dora=True)
        tileHonor           = Tile(Suit.HONOR, honor_type=HonorType.HAKU)

        self.assertTrue(tileRedDora.is_red_dora())
        self.assertFalse(tileTerminal.is_red_dora())
        self.assertFalse(tileFive.is_red_dora())
        self.assertFalse(tileHonor.is_red_dora())

    def test_is_green(self):
        tilePinzu           = Tile(Suit.PINZU, 3)
        tileManzu           = Tile(Suit.MANZU, 4)
        tileSouzuWrong      = Tile(Suit.SOUZU, 5)
        tileSouzu2          = Tile(Suit.SOUZU, 2)
        tileSouzu3          = Tile(Suit.SOUZU, 3)
        tileSouzu4          = Tile(Suit.SOUZU, 4)
        tileSouzu6          = Tile(Suit.SOUZU, 6)
        tileSouzu8          = Tile(Suit.SOUZU, 8)
        tileWind          = Tile(Suit.HONOR, honor_type=HonorType.EAST)
        tileHatsu          = Tile(Suit.HONOR, honor_type=HonorType.HATSU)
        tileHaku          = Tile(Suit.HONOR, honor_type=HonorType.HAKU)

        self.assertFalse(tilePinzu.is_green())
        self.assertFalse(tileManzu.is_green())
        self.assertFalse(tileSouzuWrong.is_green())
        self.assertTrue(tileSouzu2.is_green())
        self.assertTrue(tileSouzu3.is_green())
        self.assertTrue(tileSouzu4.is_green())
        self.assertTrue(tileSouzu6.is_green())
        self.assertTrue(tileSouzu8.is_green())
        self.assertFalse(tileWind.is_green())
        self.assertTrue(tileHatsu.is_green())
        self.assertFalse(tileHaku.is_green())
        

    
        
    

if __name__ == '__main__':
    unittest.main()