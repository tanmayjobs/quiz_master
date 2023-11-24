def until_not_valid(validator_func):
    def get_until_not_valid(*args, **kwargs):
        while (valid_result := validator_func(*args, **kwargs)) == '':
            continue
        return valid_result

    return get_until_not_valid
