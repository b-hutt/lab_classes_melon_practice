############
# Part 1   #
############

import re

class MelonType(object):
    """A species of melon at a melon farm."""



    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', 
                           True , True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', True, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', 
                          True, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', 
                                   True, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name.title()} pairs well with ')
        for pairing in melon.pairings:
            print(f'- {pairing}.')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_code_dict= {}

    for melon in melon_types:
        for code in melon.code:
            if code not in melon_code_dict:
                melon_code_dict[melon.code] = melon
  
    return melon_code_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__ (self, code, shape_rating, color_rating, field, farmer):
        """Initialize a melon"""

        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.farmer = farmer


    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False
         
def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_code_dict = melon_types
    melon_objects = []

    melon_1 = Melon(melon_code_dict['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_code_dict['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_code_dict['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_code_dict['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_code_dict['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_code_dict['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_code_dict['cren'],2, 3, 4, 'Michael')
    melon_8 = Melon(melon_code_dict['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_code_dict['yw'], 7, 10, 3, 'Sheila')
    
    melon_objects.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, 
                          melon_7, melon_8, melon_9])

    print(f'melon objects are {melon_objects}')
    return melon_objects 


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    melon_objects = melons

    for melon in melon_objects:
        if melon.is_sellable():
            print (f'Harvested by {melon.farmer} from field {melon.field}. (CAN BE SOLD)')

        else: 
            print(f'Harvested by {melon.farmer} from field {melon.field}. (NOT SELLABLE)')



