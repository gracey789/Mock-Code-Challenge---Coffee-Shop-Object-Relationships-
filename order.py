class Order:
    # Initializes an order with a customer, coffee, and price
    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer) and isinstance(coffee, Coffee) and isinstance(price, (int, float)) and 1.0 <= price <= 10.0:
            self._customer = customer
            self._coffee = coffee
            self._price = price
        else:
            raise ValueError("Invalid data for Order.")

    # Property to get the order's customer
    @property
    def customer(self):
        return self._customer

    # Property to get the order's coffee
    @property
    def coffee(self):
        return self._coffee

    # Property to get the order's price
    @property
    def price(self):
        return self._price
