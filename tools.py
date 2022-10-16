import re


def remove_spaces(string,):
    return re.sub(r"[\n\t][  +]*", "", string)


def remove_characters(string):
    return re.sub(r'[!@#$.,\sლ]', '', string)
