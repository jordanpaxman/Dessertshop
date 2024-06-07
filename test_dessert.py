''' To run the pytest for test_dessert.py, make sure pytest is installed by entering "python3 -m pip install pytest"
into the terminal. After that, enter "pytest" in the terminal to run the pytest.
'''

from dessert import DessertItem, Candy, Sundae, Cookie, IceCream, Order
from freeze import Freezer
from payment import PayType

def test_can_name_dessert():
  my_dessert = DessertItem('Chocolate Chip Cookie')
  my_candy =  Candy('Sour Patch Kids', .5, 1.99)
  my_sundae = Sundae('Chocolate with Sprinkles', 3, .99, 'sprinkles', .50)
  assert my_dessert.name == 'Chocolate Chip Cookie'
  assert my_candy.name == 'Sour Patch Kids'
  assert my_sundae.name == 'Chocolate with Sprinkles'

def test_candy():
    my_candy = Candy('air heads', 2.5, 1.00)
    assert my_candy.quantity == 2.5
    assert my_candy.unit_price == 1.00
    assert my_candy.packaging == 'Bag'
    
def test_cookie():
    my_cookie = Cookie('Snickerdoodle', 5, 10.00)
    assert my_cookie.quantity == 5
    assert my_cookie.unit_price == 10.00
    assert my_cookie.packaging == 'Box'

def test_ice_cream():
    my_ice_cream = IceCream('Vanilla', 3, 1.00)
    assert my_ice_cream.quantity == 3
    assert my_ice_cream.unit_price == 1.00
    assert my_ice_cream.packaging == 'Bowl'
    
def test_sundae():
    sundae = Sundae('The Beast', 2, 1.00, 'sprinkles', .50)
    assert sundae.quantity == 2
    assert sundae.unit_price == 1.00
    assert sundae.topping_name == 'sprinkles'
    assert sundae.topping_price == .50
    assert sundae.packaging == 'Boat'
    
def test_dessert_item():
    candy = Candy('Rips', .5, 3.0)
    assert candy.name == 'Rips'
    assert candy.quantity == .5
    assert candy.unit_price == 3.0
    assert candy.calculate_cost() == 1.5
    assert candy.tax_percent == 7.25
    assert round(candy.calculate_tax(), 2) == .11
    assert candy.packaging == 'Bag'

def test_freezer_protocol():
    freezer = Freezer()
    ice_cream = IceCream('Vanilla', 3, 1.00)
    cookie = Cookie('Snickerdoodle', 5, 10.00)
    sundae = Sundae('The Beast', 2, 1.00, 'sprinkles', .50)
    cold_ic = freezer.put(ice_cream)
    cold_cookie = freezer.put(cookie)
    cold_sundae = freezer.put(sundae)
    #assert isinstance(cold_ic, freezer) == True

def test_pay_type():
  my_order = Order()
  assert my_order.pay_type == PayType.CASH
  my_order.update_paytype('CARD')
  assert my_order.pay_type == 'CARD'
  my_order.update_paytype('PHONE')
  assert my_order.pay_type == 'PHONE'
  my_order.update_paytype('CASH')
  assert my_order.pay_type == 'CASH'
    
def test_relational():
    candy = Candy('Rips', .5, 3.0)
    candy2 = Candy('Licorice', .5, 3.0)
    sundae = Sundae('The Beast', 2, 1.00, 'sprinkles', .50)
    assert candy != sundae
    assert candy < sundae
    assert candy <= sundae
    assert sundae > candy
    assert sundae >= candy
    assert candy == candy2


def test_can_combine():
  candy1 = Candy('Gummy Bears', 2, 2.2)
  candy2 = Candy('Licorice', 2, 2.2)
  candy3 = Candy('Gummy Bears', 3, 2.2)
  cookie1 = Cookie('Chocolate Chip', 2, 12)
  cookie2 = Cookie('Chocolate Chip', 4, 12)
  cookie3 = Cookie('Oatmeal Raisin', 4, 12)

  assert candy1.can_combine(candy2) == False
  assert candy2.can_combine(candy1) == False
  assert candy3.can_combine(candy1) == True
  assert cookie1.can_combine(cookie2) == True
  assert cookie3.can_combine(cookie2) == False


