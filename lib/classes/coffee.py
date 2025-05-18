from order import Order
class Coffee:
    def __init__(self, name):
        self.name = name
        

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value) >=3:
            self._name=value
        else:
            raise ValueError("Coffee name should be a string at least 3 characters long")
        

    
    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders=self.orders()
        if orders:
            return sum(order.price for order in orders)/len(orders)
        else:
            return 0
        
if __name__ == "__main__":
    c1 = Coffee("Espresso")
    c2 = Coffee("Latte")
    print(f"Created coffees: {c1.name}, {c2.name}")