"""This file should have our melon-type classes in it."""


class AbstractMelonOrder(object):
    def get_base_price(self):
        return 5.0
    def __init__(self):
        raise NotImplementedError('Do not call this class--use concrete class of melon type')

class WatermelonOrder(AbstractMelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        if qty >= 3:
            self.base_price = self.base_price * .75
        total = self.base_price * qty    # TODO, calculate the real amount!

        return total

class CantaloupeOrder(AbstractMelonOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        if qty >= 5:
            self.base_price = self.base_price * .5
        total = self.base_price * qty    # TODO, calculate the real amount!

        return total

class CasabaOrder(AbstractMelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Winter', 'Fall']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        total = self.base_price * qty    # TODO, calculate the real amount!

        return total

class SharlynOrder(AbstractMelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        total = self.base_price * qty    # TODO, calculate the real amount!

        return total

class SantaClausOrder(AbstractMelonOrder):
    species = "Santa claus"
    color = "green "
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        total = self.base_price * qty    # TODO, calculate the real amount!

        return total

class ChristmasOrder(AbstractMelonOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        total = self.base_price * qty    # TODO, calculate the real amount!

        return total

class HornedAbstractMelonOrder(AbstractMelonOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        total = self.base_price * qty 
        return total

class XiguaOrder(AbstractMelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2
        total = self.base_price * qty   # TODO, calculate the real amount!

        return total

class OgenOrder(AbstractMelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        self.base_price = self.get_base_price()
        if self.species == 'Ogen' or self.species == 'Casaba':
            self.base_price = self.base_price + 1
        if self.imported:
            self.base_price = self.base_price*1.5
        if self.shape == 'square':
            self.base_price = self.base_price * 2

        total = self.base_price * qty   # TODO, calculate the real amount!

        return total