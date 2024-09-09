class Customer:
    # Initializes a customer with a name
    def __init__(self, name):
        self.name = name
        self._orders = []

    # Property to get the customer's name
    @property
    def name(self):
        return self._name

    # Setter for the customer's name with validation
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    # Returns all orders for this customer
    def orders(self):
        return self._orders

    # Returns all unique coffees this customer has ordered
    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    # Creates a new order for the customer
    def create_order(self, coffee, price):
        from order import Order  # Import here to avoid circular dependency
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee.orders().append(new_order)
        return new_order
