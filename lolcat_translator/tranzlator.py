import json
import re
from typing import Dict

from lolcat_translator.config import Settings


def load_dictionary(filepath: str) -> Dict:
    with open(filepath) as file:
        dictionary = json.load(file)

    return dictionary


def is_capital(string: str) -> bool:
    return string[0].upper() and string[1:].islower()


def replace_word(dictionary: Dict, string: str) -> str:
    real_string = string.group(0)

    is_upper = real_string.isupper()
    iscapital = is_capital(real_string)

    result_string = dictionary.get(real_string.lower(), real_string)
    if is_upper:
        result_string = result_string.upper()
    elif iscapital:
        result_string = result_string[0].upper() + result_string[1:]
    else:
        pass

    return result_string


def tranzlate_file(inputfile: str, outputfile: str) -> None:
    dictionary = load_dictionary(filepath=Settings().dictionary_filepath)

    with open(inputfile) as file:
        lines = file.readlines()

    with open(outputfile, "w") as file:
        for line in lines:
            file.write(re.sub(
                r"[a-zA-Z]+", lambda word: replace_word(dictionary, word), line
            ))
