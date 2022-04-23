import re


def clean_word(name: str) -> str:
    name = re.sub(r'[^a-zA-Z]', '', name)
    return name.lower()


def instance_attr_is_value(obj, field_lookup, value):
    if '__' not in field_lookup:
        return getattr(obj, field_lookup) is value
    filter_kwargs = {field_lookup: value}
    return obj.__class__.objects.filter(**filter_kwargs).exists()