def dict_to_str(dct: dict) -> str:
    return '\n'.join(f'{k}: {v}' for k, v in dct.items())

def list_to_str(lst: list) -> str:
    return '\n'.join(f'{i}' for i in lst)
