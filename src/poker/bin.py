from typing import Union

import numpy as np


class Bit(int):
    def __init__(self, value: int | str):
        if (value == "b"):
            self.value = value
        if (value not in [0, 1, "b"]):
            raise ValueError(f" Bit with nonzero value: {value}")
        self.value = int(value)


def op_int(value: str) -> int | str:
    """ Optional conversion to int"""
    if ("b" == value):
        return 0
    return int(value)


class Binary:
    def __init__(self, values: list[int] | int, length: int | None = None):
        self.values = []
        self.length = length
        if isinstance(values, int):
            self.values = [0] * (length - len(bin(values))+2) + \
                list(map(op_int, list(bin(values))))[2:]
        elif length is not None:
            # print(len(self.values))
            self.values = list(map(op_int, values))
            self.values = self.values
        else:
            # self.values = [0]*(len(values))
            self.values = list(map(op_int, values))

    @property
    def np_array(self):
        return np.array(self.values, dtype=bool)

    @property
    def to_list(self) -> list:
        return self.__tuple__()

    @property
    def to_name(self):
        return card_name_factory(self)

    @property
    def bin_str(self) -> str:
        return self.__str__()

    @property
    def to_int(self) -> int:
        return np.dot(list(self.values),
                      list([2**val for val in range(len(self.values))]))

    def __tuple__(self) -> tuple:
        return tuple(self.values)

    def __list__(self) -> list:
        return list(self.values)

    def __str__(self):
        b_s = bin(
            np.dot(list(self.values),
                   list([2**val for val in range(len(self.values))])))
        if list(b_s) == self.values:
            raise ValueError(
                f"Binary Conversion failed witrh {self.values}, {b_s}")
        return b_s


class Card:
    """ The Class for representing Cards"""

    def __init__(self, number):
        # store binary with last two digets being the color value and the rest the value
        self.binary = Binary(number)
        self.name = card_name_factory(self.binary)

    def is_greater_than(self, card: "Card") -> bool:
        return card.binary.bin_str >= card.binary.bin_str

    def __str__(self) -> str:
        return str(self.name)


def gen_cv(length):
    length = length
    return {
        Binary(0, length=length).__tuple__(): "2",
        Binary(1, length=length).__tuple__(): "3",
        Binary(2, length=length).__tuple__(): "4",
        Binary(3, length=length).__tuple__(): "5",
        Binary(4, length=length).__tuple__(): "6",
        Binary(5, length=length).__tuple__(): "7",
        Binary(6, length=length).__tuple__(): "8",
        Binary(7, length=length).__tuple__(): "9",
        Binary(8, length=length).__tuple__(): "10",
        Binary(9, length=length).__tuple__(): "J",
        Binary(10, length=length).__tuple__(): "Q",
        Binary(11, length=length).__tuple__(): "K",
        Binary(12, length=length).__tuple__(): "A",
        # Binary(13, length=length).__tuple__(): "Joker"

    }


CT = {
    "cc-str":  {
        (1, 1): "h",
        (1, 0): "d",
        (0, 1): "s",
        (0, 0): "c",
    },
    "cv-str": gen_cv(4),


}


def invert_conversion_table(conversion) -> dict:
    res = {}
    for table_name, table in conversion.items():
        print(table_name.split)
        inv_table_name = "-".join(reversed(table_name.split("-")))
        res[inv_table_name
            ] = dict([[value, key]for key, value in table.items()])
        res[table_name] = table
    return res


CT = invert_conversion_table(CT)
print(CT)


def card_value(inp: tuple | str) -> str | tuple:
    """ Get Card Value from binary string """

    c_str = "cv-str"
    if isinstance(inp, str):
        c_rev = "-".join(reversed(c_str.split("-")))
        return CT[c_rev][inp]

    key: tuple[int, int] = inp[: -2]
    # print
    # try:
    return CT[c_str][key]
    # except:
    #     # print(cv)
    #     raise Exception("Could not find key", key)


def card_color(inp: tuple | str) -> str | tuple:
    """Get Card Color from binary string"""
    c_str = "cc-str"
    if isinstance(inp, str):
        c_rev = "-".join(reversed(c_str.split("-")))
        return CT[c_rev][inp]

    key: tuple[int, int] = tuple(inp[-2:])
    # print(binary)
    return CT[c_str][key]


def card_name_factory(binary: Binary) -> str:
    """ Construct the name of the card from its binary representation"""
    card_name: str = ""

    card_name += card_color(binary.__tuple__())
    # print(card_name)
    card_name += card_value(binary.__tuple__())
    # print(card_name)
    return card_name


def card_np_map(length) -> np.ndarray:
    result = {}

    bit = [[0, 1]]
    length = length+2
    print(bit*length)
    coords = np.array(np.meshgrid(* bit*length)).ravel("F")
    print(coords.shape, len(bit)*length)
    coords = coords.reshape(-1, len(bit)*length)
    # print([2 ** i for i in range(len(bit)*length)], coords)
    # print(coords)

    # color indicator
    val = Binary(coords[0], length=length)
    res = np.zeros((4, 13, 1), dtype="|S3")
    print(res.shape)
    for t in coords:
        val = Binary(t, length=length)
        try:
            val_name = str(val.to_name)
            print(val_name)
            res[Binary(card_color(val_name[0])).to_int,
                Binary(card_value(val_name[1:])).to_int] = val_name

        except Exception as e:
            pass

    # print(result.items())
    print("\n", res, "Arr res")
    print(np.where(np.any(res == 1, axis=2)))
    return res
    # print(gen_cv(length-2))


class Game:
    def __init__(self, possible_cards: list[Card] | None):
        self.card_deck = possible_cards


if __name__ == '__main__':
    bit_length = 4

    # print(card_name_factory(bin(2)))
    (print(Binary(64, length=bit_length).np_array))
    card_np_map(bit_length)

    # for i in range()
