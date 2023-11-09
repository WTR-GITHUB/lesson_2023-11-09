import logging
from typing import List

logging.basicConfig(level=logging.DEBUG, filename='error.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def test_input_lenght(text_line: str) -> bool:
    try:
        if len(text_line) >= 25:
            return True
        else:
            return False
    except Exception as error:
        logging.error(error)   


def sepacate_letters(text_line: str) -> List[str]:
    try:
        only_letters = [letter for letter in text_line if letter.isalpha()]
        return only_letters
    except Exception as error:
        logging.error(error)


def sepacate_numbers(text_line: str) -> List[str]:
    try:
        only_numbers = [number for number in text_line if number.isnumeric()]
        return only_numbers
    except Exception as error:
        logging.error(error)


def sepacate_spec_simbolss(text_line: str) -> List[str]:
    try:
        only_simb = [simb for simb in text_line if not simb.isalpha() and not simb.isnumeric()]
        return only_simb
    except Exception as error:
        logging.error(error)


def sort_unique_chars(text_list: List[str]) -> List[str]:
    unique_char_list = [] 
    try:
        for char in text_list:
            if char not in unique_char_list:
                unique_char_list.append(char)
        return unique_char_list
    except Exception as error:
        logging.error(error)                   


def put_in_order(text_list: List[str])-> List[str]:
    try:
        return sorted(text_list)
    except Exception as error:
        logging.error(error)


def revers_order(text_list: List[str])-> List[str]:
    try:
        text_list.reverse()
        return text_list
    except Exception as error:
        logging.error(error)


def sum_of_chars(text_list: List[str])-> int:
    try:
        return len(text_list)
    except Exception as error:
        logging.error(error)


