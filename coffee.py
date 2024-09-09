class Coffee:
    # Initializes a coffee with a name
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            self._orders = []
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
 
    # Property to get the coffee's name
    @property
    def name(self):
        return self._name

    # Returns all orders for this coffee
    def orders(self):
        return self._orders

    # Returns all unique customers who have ordered this coffee
    def customers(self):
        return list(set(order.customer for order in self._orders))

    # Returns the number of orders for this coffee
    def num_orders(self):
        return len(self._orders)

    # Returns the average price of this coffee
    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
