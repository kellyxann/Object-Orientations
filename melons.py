"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """An order of melons"""
 
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5
        if species == 'Christmas melon':
            total = (1 + self.tax) * self.qty * base_price * 1.5
        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True
    

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.08)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
