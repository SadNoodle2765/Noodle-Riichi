from src.suit import Suit, HonorType

class Tile:
    def __init__(self, suit: Suit, number: int = 0, honor_type: HonorType = HonorType.NULL, red_dora: bool = False):
        self._suit = suit
        self._number = number
        self._honor_type = honor_type
        self._red_dora = red_dora

        if (suit == Suit.HONOR): self._number = 0
        else: self._honor_type = HonorType.NULL

        self._validate(suit, number, honor_type, red_dora)

    @staticmethod
    def _validate(suit: Suit, number: int, honor_type: HonorType, red_dora: bool):
        if type(suit) is not Suit:
            raise TypeError("suit type incorrect (should be type enum Suit)")
        if type(number) is not int:
            raise TypeError("number type incorrect (should be type int)")
        if type(honor_type) is not HonorType:
            raise TypeError("honor_type type incorrect (should be type HonorType)")
        if type(red_dora) is not bool:
            raise TypeError("red_dora type incorrect (should be type bool)")    


    def get_suit(self):
        return self._suit
    
    def get_number(self):
        return self._number
    
    def is_honor(self):
        pass

    def is_terminal(self):
        pass

    def is_simple(self):
        pass

    def is_wind(self):
        pass

    def is_dragon(self):
        pass

    def is_red_dora(self):
        pass

    