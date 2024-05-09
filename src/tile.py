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
            raise TypeError(f"suit type {type(suit)} incorrect (should be type enum Suit).")
        if type(number) is not int:
            raise TypeError(f"number type {type(number)}  incorrect (should be type int).")
        if type(honor_type) is not HonorType:
            raise TypeError(f"honor_type {type(honor_type)}  type incorrect (should be type HonorType).")
        if type(red_dora) is not bool:
            raise TypeError(f"red_dora {type(red_dora)}  type incorrect (should be type bool).")    
        
        if suit != Suit.HONOR:
            if number < 1 or number > 9:
                raise ValueError(f"number {number} out of range. Must be between 1 and 9.")
            if red_dora and number != 5:
                raise ValueError(f"number {number} cannot be red dora. Must be number 5.")
            if honor_type != HonorType.NULL:
                raise ValueError(f"honor_type {honor_type} invalid. Must be HonorType.NULL for non-honor suits.")
        else:
            if number != 0:
                raise ValueError(f"number {number} invalid. Must be 0 for honor suit.")
            if honor_type == HonorType.NULL:
                raise ValueError(f"honor_type {honor_type} invalid. Cannot be HonorType.NULL for honor suit.")
            if red_dora:
                raise ValueError(f"Honor suit cannot be red dora.")



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

    