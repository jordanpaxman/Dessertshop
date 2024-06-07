from dessertshop import Customer

def test_customer():
  customer1 = Customer('Bill')
  assert customer1.name == 'Bill'
  assert customer1.order_history == []
  assert customer1.customer_id == 1000
  customer1.set_id(1)
  assert customer1.customer_id == 1001
  customer1.set_id(1)
  assert customer1.customer_id == 1002


