def signleton(cls):
    obj = cls()
    generate = yield
    while generate:
        yield obj
        generate = yield

def get(signleton_obj, close):
    if close:
        ...
    else:
        # signleton_obj.send(!close)
        ...