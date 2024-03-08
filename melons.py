"""Classes for melon orders."""
class AbstractMelonOrder:   
       
    def __init__(self, species, qty,):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        # print(self.order_type)
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        if self.species == ("Christmas Melons"):
            base_price = base_price * 1.5     #check
        if self.order_type == "international" and self.qty < 10:
            # print(total)
            total += 3

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
    tax = 0.17
    order_type = "international"
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        

        # if qty < 10:
        # self.base_price = self.base_price + 3

class GovernmentMelonOrder(AbstractMelonOrder):
    order_type = "government"
    tax = 0.0
    # mark_inspection = False
    def __init__(self, species, qty, inspection):
        super.__init__(species, qty)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed
            
        



    def get_country_code(self):
        """Return the country code."""

        return self.country_code
