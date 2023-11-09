import sys
from src.helpers.constants import Output

invalid_choice = lambda: print(Output.INVALID_CHOICE)
exit = lambda: sys.exit(0)
show_message = lambda x: print(x)
