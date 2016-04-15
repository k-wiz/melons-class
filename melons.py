"""This file should have our order classes in it."""


class AbstractMelonOrder(object):

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax


    def get_total(self):
        """ Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to True."""

        self.shipped = True





class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, 
                                                "domestic", 0.08)




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        self.country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty, 'international', 0.17)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


# class ChristmasMelonOrder(AbstractMelonOrder):

#     def get_total(self):

#         base_price = 1.5 * 5


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0)



    def mark_inspection(self):
        self.passed_inspection = True