def until_none(input_func):
    def get_until_not_valid(*args):
        while not (valid_result := input_func(*args)):
            continue
        return valid_result

    return get_until_not_valid
