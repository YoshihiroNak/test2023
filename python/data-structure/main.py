from my_module import foo as bar, person
import my_module
from colort import colorize, ForegroundColor as fc, Style, BackgroundColor as bc
# print(dir(my_module))


foo(person)
bar({'name': 'Matt', 'age':51})



colored_text = colorize('Hello World', fc.GREEN, Style.BOLD, bc.YELLOW)
print('colored text: ' , colored_text)