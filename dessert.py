from abc import ABC, abstractmethod
from payment import PayType
from combine import Combinable


customer_db = {} #Dict[str, Customer()]

class Customer:
  def __init__(self, name):
    self.name = name
    self.order_history = []
    self.customer_id = 1000 

  def add2history(self, order: "Order") -> list:
    self.order_history.append(order)
    return self.order_history
    
  def __str__(self):
    return f'Customer Name: {self.name}         Customer ID: {self.customer_id}         Total Orders: {len(self.order_history)}'

  def set_id(self, id_number):
    self.customer_id += id_number
    

    

class DessertItem(ABC):
  def __init__(self, name = '', tax_percent = 7.25):
    self.name = name
    self.tax_percent = tax_percent
    self.packaging = None
    

  def calculate_cost(self):
    pass
  
  def calculate_tax(self):
    return self.calculate_cost() * (self.tax_percent / 100)

  def get_name(self):
    return self.name

  def __eq__(self, other):
    return self.calculate_cost() == other
    
  def __ne__(self, other):
    return self.calculate_cost() != other

  def __lt__(self, other):
    return self.calculate_cost() < other
  
  def __gt__(self, other):
    return self.calculate_cost() > other
  
  def __ge__(self, other):
    return self.calculate_cost() >= other

  def __le__(self, other):
    return self.calculate_cost() <= other
    
  

class Candy(DessertItem):
  def __init__(self, name, quantity, unit_price):
    super().__init__(name)
    self.quantity = quantity
    self.unit_price = unit_price
    self.packaging = 'Bag'


  def calculate_cost(self):
    return self.quantity * self.unit_price


  def __str__(self):
    return f'{self.name}, {self.quantity}lbs, ${round(self.unit_price, 2)}/lb, ${round(self.calculate_cost(), 2)}, {round(self.calculate_tax(),2)}, ({self.packaging})'

  def can_combine(self, other: "Candy") -> bool:
    if isinstance(other, Candy) and self.name == other.name and self.unit_price == other.unit_price:
      return True
    else:
      return False
    
  def combine(self, other: "Candy") -> "Candy":
    combined_candy = Candy(self.name, (self.quantity + other.quantity), self.unit_price)
    return combined_candy
        

class Cookie(DessertItem):
  def __init__(self, name, quantity, unit_price):
    super().__init__(name)
    self.quantity = quantity #int
    self.unit_price = unit_price  #float
    self.packaging = 'Box'

  def calculate_cost(self):
    return self.quantity/12 * self.unit_price

  def chill(self):
    return 'chilling'

  def thaw(self):
    return 'thawing'

  def __str__(self):
    return f'{self.name} Cookies, {self.quantity} cookies, ${round(self.unit_price, 2)}/dozen, ${round(self.calculate_cost(), 2)}, {round(self.calculate_tax(), 2)}, ({self.packaging})'

  def can_combine(self, other: "Cookie") -> bool:
    if isinstance(other, Cookie) and self.name == other.name and self.unit_price == other.unit_price:
      return True
    else:
      return False
    
  def combine(self, other: "Cookie") -> "Cookie":
    combined_cookie = Cookie(self.name, (self.quantity + other.quantity), self.unit_price)
    return combined_cookie


class IceCream(DessertItem):
  def __init__(self, name, quantity, unit_price):
    super().__init__(name)
    self.quantity = quantity #int 
    self.unit_price = unit_price #float
    self.packaging = 'Bowl'

  def calculate_cost(self):
    return self.quantity * self.unit_price

  def chill(self):
    return 'chilling'

  def thaw(self):
    return 'thawing'

  def __str__(self):
    return f'{self.name} Ice Cream, {self.quantity} scoops, ${round(self.unit_price, 2)}/scoop, ${round(self.calculate_cost(), 2)}, {round(self.calculate_tax(), 2)}, ({self.packaging})'

  def can_combine(self, other: "IceCream") -> bool:
    return False


class Sundae(IceCream):
  def __init__(self, name, quantity, unit_price, topping_name, topping_price):
    super().__init__(name, quantity, unit_price)
    self.topping_name = topping_name #string 
    self.topping_price = topping_price #float
    self.packaging = 'Boat'
    

  def calculate_cost(self):
    return (self.quantity * self.unit_price) + self.topping_price

  def chill(self):
    return 'chilling'

  def thaw(self):
    return 'thawing'

  def __str__(self):
    return f'{self.name} Sundae, {self.quantity} scoops, ${round(self.unit_price, 2)}/scoop, ${round(self.calculate_cost(), 2)}, {round(self.calculate_tax(), 2)}, ({self.packaging})\n{self.topping_name} topping, ${self.topping_price}'

  def can_combine(self, other: "IceCream") -> bool:
    return False
      


class Order(DessertItem, Customer):
  def __init__(self):
    self.order = []
    self.pay_type = PayType.CASH


  def calculate_cost(self):
    pass

  def get_order_list(self):
    return self.order
    
  def add(self, DessertItem):
    if len(self.order) == 0:
      self.order.append(DessertItem)
    else:
      count = 0
      order_length = len(self.order)
      for item in self.order:
        can_combine = item.can_combine(DessertItem)
        if can_combine == False:
          count += 1
          if count == order_length:
            self.order.append(DessertItem)
            break
        if can_combine == True:
          combined_item = item.combine(DessertItem)
          self.order.remove(item)
          self.order.append(combined_item)
          break

  def item_count(self):
    return len(self.order)
  
  def order_cost(self):
    '''calculates and returns the total cost for all items in the order
    '''
    self.cost_list = []
    for item in self.order:
      self.cost_list.append(item.calculate_cost())
    total_cost = 0
    for price in self.cost_list:
      total_cost += price
    return round(total_cost, 2)


  def order_tax(self):
    '''calculates and returns the total tax for all items in the order
    '''
    self.tax_list = []
    for element in self.order:
      self.tax_list.append(element.calculate_tax())
    total_tax = 0
    for price in self.tax_list:
      total_tax += price
    return round(total_tax, 2)

  def update_paytype(self, new_payment):
    self.new_payment = new_payment
    self.pay_type = self.new_payment

  def sort_items(self):
    self.order.sort(key = lambda x: x.calculate_cost())


  def __str__(self):
    total_cost = 0
    total_tax = 0
    print('-------------------RECEIPT--------------------')
    for item in self.order:
      print(item)
      total_cost += round(item.calculate_cost(), 2)
      total_tax += round(item.calculate_tax(), 2)
    print('Total Number of items in order:   ', len(self.order))
    print('----------------------------------------------')
    print(f'Order Subtotals:  ${round(total_cost, 2)} cost    ${round(total_tax, 2)} tax')
    print(f'Total Cost:   ${round(total_cost + total_tax, 2)}')
    print('----------------------------------------------')
    print(f'Paid with {self.pay_type}')
    print('----------------------------------------------')
    return ''
    

  
    
    



