#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    dictio_rom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    number = 0
    for i in range(len(roman_string)):
        if dictio_rom.get(roman_string[i], 0) == 0:
            return 0
        if (i != (len(roman_string) - 1) and
                dictio_rom[roman_string[i]] < dictio_rom[roman_string[i + 1]]):
                number += dictio_rom[roman_string[i]] * -1
        else:
            number += dictio_rom[roman_string[i]]
    return number
