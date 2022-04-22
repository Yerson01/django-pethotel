import re


def clean_word(name: str) -> str:
    name = re.sub(r'[^a-zA-Z]', '', name)
    return name.lower()
