import os
os.environ["KIVY_NO_ARGS"] = "1"
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from dessert import *
from receipt import make_receipt

my_order = Order()
class ItemSelection(Screen):
    pass

class CandyWindow(Screen):
    dessert = ObjectProperty(None)
    quantity = ObjectProperty(None)
    price = ObjectProperty(None)

    def add_item(self):
        dessert = self.dessert.text
        quantity = self.quantity.text
        price = self.price.text
        
    
        my_candy = Candy(dessert, float(quantity), float(price))
        print(my_candy)
        my_order.add(my_candy)
        self.clear_text()
           

    def error_widget(self):
        self.add_widget(Label(text = "Make sure Dessert contains only letters and your quantity/ contains only numbers"))
        self.clear_text()


    def clear_text(self):
        self.dessert.text = ""
        self.quantity.text = ""
        self.price.text = ""
        

class CookieWindow(Screen):
    dessert = ObjectProperty(None)
    quantity = ObjectProperty(None)
    price = ObjectProperty(None)
    
    
    def add_item(self):
        dessert = self.dessert.text
        quantity = self.quantity.text
        price = self.price.text

        my_cookie = Cookie(dessert, float(quantity), float(price))
        print(my_cookie)
        my_order.add(my_cookie)
        self.clear_text()


    def clear_text(self):
        self.dessert.text = ""
        self.quantity.text = ""
        self.price.text = ""


class IceCreamWindow(Screen):
    dessert = ObjectProperty(None)
    quantity = ObjectProperty(None)
    price = ObjectProperty(None)
    
    def add_item(self):
        dessert = self.dessert.text
        quantity = self.quantity.text
        price = self.price.text

        my_icecream = IceCream(dessert, float(quantity), float(price))
        print(my_icecream)
        my_order.add(my_icecream)
        self.clear_text()

    
    def clear_text(self):
        self.dessert.text = ""
        self.quantity.text = ""
        self.price.text = ""

class SundaeWindow(Screen):
    dessert = ObjectProperty(None)
    quantity = ObjectProperty(None)
    price = ObjectProperty(None)
    topping = ObjectProperty(None)
    topping_price = ObjectProperty(None)
    
    def add_item(self):
        dessert = self.dessert.text
        quantity = self.quantity.text
        price = self.price.text
        topping = self.topping.text
        topping_price = self.topping_price.text

        my_sundae = Sundae(dessert, float(quantity), float(price), topping, float(topping_price))
        print(my_sundae)
        my_order.add(my_sundae)
        self.clear_text()


    def clear_text(self):
        self.dessert.text = ""
        self.quantity.text = ""
        self.price.text = ""
        self.topping.text = ""
        self.topping_price.text = ""


class CustomerWindow(Screen):
    customer_name = ObjectProperty(None)


    def check_customer(self):
        customer_name = self.customer_name.text
        if customer_name in customer_db.keys():
            customer_db[customer_name].add2history(my_order)
        else:
            customer_db[customer_name] = Customer(customer_name)
            customer_db[customer_name].add2history(my_order)
            customer_db[customer_name].set_id(len(customer_db))

    def update_pay(self, id):
        phone = self.phone
        card = self.card 
        cash = self.cash
        

        if id == phone:
            my_order.update_paytype('PHONE')
        elif id == card:
            my_order.update_paytype('CARD')
        elif id == cash:
            my_order.update_paytype('CASH')


    def clear_text(self):
        self.customer_name.text = ""


class OrderAgainWindow(Screen):
    def new_order(self):
        pass 
    def print_receipts(self):
        subtotal = my_order.order_cost()
        total_tax = my_order.order_tax()
        total_cost = round(subtotal + total_tax, 2)
        num_of_items = len(my_order.get_order_list())

        items = []
        my_order.sort_items()
        items.append(['Name', 'Packaging', 'Quantity', 'Unit Price', 'Item Cost', 'Tax'])
        for item in my_order.get_order_list():
            items.append([item.get_name(), item.packaging, item.quantity, item.unit_price, round(item.calculate_cost(), 2), round(item.calculate_tax(), 2)])
        items.append(['--------------------------'])
        items.append(['Order Subtotals', '', '', '', subtotal, total_tax])
        items.append(['Order Total', '', '', '', '', total_cost])
        items.append(['Number of Items', '', '', '', '', num_of_items])
        items.append(['--------------------------', '', '', '', '', '']) 
        items.append([f'Paid with {my_order.pay_type}', '', '', '', '', ''])
        items.append(['--------------------------', '', '', '', '', '']) 
        #items.append([f'{customer_db[name]}', '', '', '', '', ''])
        make_receipt(items, 'receipt.pdf')
        print(my_order)
        #print(customer_db[name], '\n')


class ThankYouWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('dessert_stylesheet.kv')

class DessertApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    DessertApp().run()