class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
      return self._name
    
    @name.setter
    def name(self,value):
       if isinstance (value,str)and 1<=len(value)<=15:
            self._name=value
       else:
          raise ValueError("Customer must be of input string and must be between 1 and 15 characters")
       

    def orders(self):
        from .order import Order
        return [order for order in Order.all_orders if order.coffee == self]
        
    def coffees(self):
        from .order import Order
        return list({order.coffee for order in Order.all_orders if order.customer == self})

    
    def create_order(self, coffee, price):
        from .order import Order
        return Order(self, coffee, price)
    
    def most_aficionado(cls, coffee):
        from .order import Order
        customers = set(order.customer for order in Order.all_orders if order.coffee == coffee)
        if not customers:
            return None
        return max(customers, key=lambda customer: sum(
            order.price for order in Order.all_orders
            if order.customer == customer and order.coffee == coffee
        ))
if __name__ == "__main__":
    customera = Customer("Kimani")
    customerb = Customer("Wanja")
    customerc = Customer("Kamau")
    print("*****Created customers: *****")
    print(f"Customer name is: {customera.name}")
    print(f"Customer name is: {customerb.name}")
    print(f"Customer name is: {customerc.name}")