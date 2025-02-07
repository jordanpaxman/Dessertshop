from dessert import DessertItem, Candy, Sundae, Cookie, IceCream, Order, Customer, customer_db
from receipt import make_receipt
from freeze import Freezer
import sys
from dessertshop_gui import DessertApp


def main_menu():
    my_order = Order()
    while True:
        print("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae\n5: Admin Module\nWhat would you like to add to the order? (1-5, Enter for done):")
        choice = input().strip()
        if not choice:
            break
        if choice == "1":
            item = user_prompt_candy()
            if item:
                my_order.add(item)
        elif choice == "2":
            item = user_prompt_cookie()
            if item:
                my_order.add(item)
        elif choice == "3":
            item = user_prompt_icecream()
            if item:
                my_order.add(item)
        elif choice == "4":
            item = user_prompt_sundae()
            if item:
                my_order.add(item)
        elif choice == "5":
            print('hello')
            while True:
              print('ADMIN MODULE\n1: Shop Customer List\n2: Customer Order History\n3: Best Customer\n4: Exit Admin Module\nWhat would you like to do? (1-4):')
              admin_choice = input().strip()
              if admin_choice == '1':
                for customer in customer_db.values():
                  print(customer)
              elif admin_choice == '2':
                print('Enter the name of the customer:')
                customer_choice = input().strip()
                if customer_choice in customer_db.keys():
                  receipt_num = 1
                  print(customer_db[customer_choice])
                  for order in customer_db[customer_choice].order_history:
                    print(f'Order #: {receipt_num}')
                    print(f'{order}\n')
                    receipt_num += 1
                else:
                  print('Customer name not found\n')
              elif admin_choice == '3':
                num_orders = 0
                best_customer = ''
                for customer in customer_db.values():
                  if len(customer.order_history) > num_orders:
                    num_orders = len(customer.order_history)
                    best_customer = customer.name
                  else:
                    pass
                print(f'The Dessert Shop\'s most valued customer is: {best_customer}!\n')
              elif admin_choice == '4':
                break
        else:
            print("Invalid option, please try again.\n")


    print("What is the customer's name?")
    name = input().strip().capitalize()
    if name in customer_db.keys():
      customer_db[name].add2history(my_order)
    else:
      customer_db[name] = Customer(name)
      customer_db[name].add2history(my_order)
      customer_db[name].set_id(len(customer_db))
    

    while True:
      print('1: Cash\n2: Card\n3: Phone\nEnter payment method: ')
      choice = input().strip()
      if choice == '1':
        my_order.update_paytype('CASH')
        break
      elif choice == '2':
        my_order.update_paytype('CARD')
        break
      elif choice == '3':
        my_order.update_paytype('PHONE')
        break
      else:
        print('Invalid payment option, please try again.\n')
    return my_order, name


def user_prompt_candy():
    print("Enter the type of candy:")
    name = input().strip()
    print("Enter the weight (in pounds):")
    weight = float(input().strip())
    print("Enter the price per pound:")
    price_per_pound = float(input().strip())
    return Candy(name, weight, price_per_pound)

def user_prompt_cookie():
    print("Enter the type of cookie:")
    name = input().strip()
    print("Enter the number of cookies:")
    number = int(input().strip())
    print("Enter the price per dozen:")
    price_per_dozen = float(input().strip())
    return Cookie(name, number, price_per_dozen)


def user_prompt_icecream():
    print("Enter the type of ice cream:")
    name = input().strip()
    print("Enter the number of scoops:")
    scoops = int(input().strip())
    print("Enter the price per scoop:")
    price_per_scoop = float(input())
    return IceCream(name, scoops, price_per_scoop)

def user_prompt_sundae():
    print("Enter the type of sundae:")
    name = input().strip()
    print("Enter the number of scoops:")
    scoops = int(input().strip())
    print("Enter the price per scoop:")
    price_per_scoop = float(input().strip())
    print("Enter the topping name:")
    topping_name = input().strip()
    print("Enter the cost of toppings:")
    topping_cost = float(input().strip())
    return Sundae(name, scoops, price_per_scoop, topping_name, topping_cost)

def ring_up(order, name):
  subtotal = order.order_cost()
  total_tax = order.order_tax()
  total_cost = round(subtotal + total_tax, 2)
  num_of_items = len(order.get_order_list())

  items = []
  order.sort_items()
  items.append(['Name', 'Packaging', 'Quantity', 'Unit Price', 'Item Cost', 'Tax'])
  for item in order.get_order_list():
    items.append([item.get_name(), item.packaging, item.quantity, item.unit_price, round(item.calculate_cost(), 2), round(item.calculate_tax(), 2)])
  items.append(['--------------------------'])
  items.append(['Order Subtotals', '', '', '', subtotal, total_tax])
  items.append(['Order Total', '', '', '', '', total_cost])
  items.append(['Number of Items', '', '', '', '', num_of_items])
  items.append(['--------------------------', '', '', '', '', '']) 
  items.append([f'Paid with {order.pay_type}', '', '', '', '', ''])
  items.append(['--------------------------', '', '', '', '', '']) 
  items.append([f'{customer_db[name]}', '', '', '', '', ''])
  make_receipt(items, 'receipt.pdf')
  print(order)
  print(customer_db[name], '\n')


def prompt_new_order():
  while True:
    print("Would you like to place another order?\n\nPress 'y' for yes.\nPress anything else for no.")
    choice = input().strip().lower()
    if choice == 'y':
      print('What else would you like?\n')
      my_order, customer_name = main_menu()
      ring_up(my_order, customer_name)

    else:
      print('Thank you and come again!')
      break

def runs_gui():
  try:
    if sys.argv[1] == "-g":
       DessertApp().run()
  except:
     main()

def main():

  freezer = Freezer()
  chocolate_chip = Cookie('Chocolate Chip', 6, 3.99)
  pistachio_icecream = IceCream('Pistachio', 2, .79)
  vanilla_sundae = Sundae('Vanilla', 3, .69, 'Hot Fudge', 1.29)
  oatmeal_raisin = Cookie('Oatmeal Raisin', 4, 3.45)
  freezer.put(chocolate_chip)
  freezer.put(pistachio_icecream)
  freezer.put(vanilla_sundae)
  freezer.put(oatmeal_raisin)
  
  my_order, customer_name = main_menu()

  freezer.get(chocolate_chip)
  my_order.add(chocolate_chip)
  freezer.get(pistachio_icecream)
  my_order.add(pistachio_icecream)
  freezer.get(vanilla_sundae)
  my_order.add(vanilla_sundae)
  freezer.get(oatmeal_raisin)
  my_order.add(oatmeal_raisin)

  
  ring_up(my_order, customer_name)
  prompt_new_order()


if __name__ == "__main__":
  #main()
  runs_gui()
