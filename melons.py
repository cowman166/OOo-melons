"""Classes for melon orders."""
class AbstractMelonOrder:   
       
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.order_type = ("international", "domestic")
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        if self.species == ("Christmas Melons"):
            base_price = base_price * 1.5     #check
        if self.order_type == "international" and self.qty < 10:
            return total + 3

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
        
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.order_type = "international"    # check 
        self.tax = 0.17
        



    def get_country_code(self):
        """Return the country code."""

        return self.country_code
