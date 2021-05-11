
def parse_str_with_space(var: str) -> str:
    """ return string without multiply whitespaces
    Example: var = "My name  is   John    "
    Return var = "My name is John"
    """
    str_list = list(filter(None, var.split(' ')))
    return ' '.join(x for x in str_list)


def find_by_key(data: dict, target):
    """Find a key value in a nested dict"""
    for k, v in data.items():
        if k == target:
            return v
        elif isinstance(v, dict):
            return find_by_key(v, target)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    return find_by_key(i, target)
