def menu_loop(menu):
    """
    menu_loop can be used on screen function
    which basically shows a screen till the user want to go back or quit the application.
    IMPORTANT: The function which uses the menu_loop must have return type as bool

    IMPORTANT: The returned bool tells whether to go back or not,
    True means go back and False means continue the same screen.

    :param menu: The function for the menu screen.
    :return: Returns the decorated looped menu screen.
    """

    def looped_menu(*args, **kwargs):
        while True:
            go_back = menu(*args, **kwargs)
            if go_back:
                break

    return looped_menu
