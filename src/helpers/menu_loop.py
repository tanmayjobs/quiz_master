def menu_loop(menu):
    def looped_menu():
        while True:
            menu()

    return looped_menu()
