def menu_loop(menu):
    def looped_menu(*args, **kwargs):
        while True:
            go_back = menu(*args, **kwargs)
            if go_back:
                break
    return looped_menu
