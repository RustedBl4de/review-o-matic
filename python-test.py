def get_lego():
    return "21103", "Back to the Future Time Machine", "401", "2013"

my_lego = get_lego()
print(my_lego[0], my_lego[1], my_lego[2], my_lego[3])


# Better
from collections import namedtuple

def get_lego():
    lego = namedtuple("lego", ["serial_number", "name", "num_of_pieces", "release_year"])
    return lego("21103", "Back to the Future Time Machine", "401", "2013")

my_lego = get_lego()
print(my_lego.serial_number, my_lego.name, my_lego.num_of_pieces, my_lego.release_year)