import re


def remove_spaces(string,):
    clean_string = re.sub(r"[\n\t][  +]*", "", string)
    return clean_string
