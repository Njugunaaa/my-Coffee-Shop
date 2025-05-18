class Order:
    all_orders=[]               
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and 1 <= value <= 10:
            self._price = float(value)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self,value):
        from customer import Customer
        if isinstance(value,Customer):
            self._customer=value

        else:
            raise TypeError("Customer should be an instance of a customer. ")

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self,value):
        from coffee import Coffee
        if isinstance(value,Coffee):
            self._coffee=value

        else:
            raise TypeError("Coffee should be an instance of a coffee. ")        

    

if __name__ == "__main__":
    from customer import Customer
    from coffee import Coffee

    cust1 = Customer("Kimani")
    coffee1 = Coffee("Espresso")

    order1 = Order(cust1, coffee1, 5)
    print(f"{order1.customer.name} ordered {order1.coffee.name} at {order1.price}")