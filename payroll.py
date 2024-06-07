from abc import ABC, abstractmethod
import os


employees = []
PAY_LOGFILE = 'paylog.txt'

def find_employee_by_id(id:str) -> object:
  for employee in employees:
    if employee.emp_id == id:
      return employee
    

def load_employees():
  #reads employees.csv 
  with open('employees.csv', 'r') as input_file:
    lines = input_file.readlines()[1:]
    for line in lines:
      split_line = line.strip().split(',')
      id = split_line[0]
      first_name = split_line[1]
      last_name = split_line[2]
      address = split_line[3]
      city = split_line[4]
      state = split_line[5]
      zipcode = split_line[6]
      classification = split_line[7]
      salary = float(split_line[8])
      commission_rate = float(split_line[9])
      hourly_rate = float(split_line[10])
      emp = Employee(id, first_name, last_name, address, city, state, zipcode, classification)
      employees.append(emp)
      for employee in employees:
        if employee.classification == '3':
          employee.make_hourly(hourly_rate)
        if employee.classification == '1':
          employee.make_salaried(salary)
        if employee.classification == '2':
          employee.make_commissioned(salary, commission_rate)
      # print(employee.classification)
  
    
def process_timecards():
  #reads timecards.csv
  with open('timecards.csv', 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
      split_line = line.strip().split(',')
      id = split_line[0]
      hourly_emp = find_employee_by_id(id).classification
      for clock_in in split_line[1:]:
        hourly_emp.add_timecard(clock_in)
     
           

def process_receipts():
  #reads receipts.csv and interacts with commissioned employees
  with open('receipts.csv', 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
      split_line = line.strip().split(',')
      id = split_line[0]
      commissioned_emp = find_employee_by_id(id).classification
      for sale in split_line[1:]:
        commissioned_emp.add_receipt(sale)
      # print(commissioned_emp.receipts)


def run_payroll():
  if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘paylog.txt’
    os.remove(PAY_LOGFILE)
  for emp in employees: # employees is the global list of Employee objects
    emp.issue_payment() # issue_payment calls a method in the classification
    # object to compute the pay


class Employee():
  def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
    self.emp_id = emp_id
    self.first_name = first_name
    self.last_name = last_name
    self.address = address
    self.city = city
    self.state = state
    self.zipcode = zipcode
    self.classification = classification

  def make_hourly(self, hourly_rate: float):
    self.classification = Hourly(hourly_rate)
    #creates an hourly object and sets self.classification = to hourly object with hourly_rate as parameter
  
  def make_salaried(self, salary: float):
    self.classification = Salary(salary)

  def make_commissioned(self, salary: float, commission_rate: float):
    self.classification = Commission(salary, commission_rate)

  def issue_payment(self):
    with open(PAY_LOGFILE, 'a') as input_file:
      payment = self.classification.compute_pay()
      if payment != 0:
        print(f'Mailing {payment:.2f} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}', file = input_file)
    

    # print('PAYMENT FOR EMPLOYEE', payment)


class Classification(ABC):

  @abstractmethod
  def compute_pay():
    pass


class Hourly(Classification):
  def __init__(self, hourly_rate):
    self.hourly_rate = hourly_rate
    self.hours = []

  def add_timecard(self, time_card):
    self.hours.append(time_card)
  
  def compute_pay(self):
    total_hours = 0
    float_hours = [float(i) for i in self.hours]
    for time_card in float_hours:
      total_hours += time_card
    total_pay = total_hours * self.hourly_rate
    return round(total_pay, 2)


class Salary(Classification):
  def __init__(self, salary):
    self.salary = salary
  
  def compute_pay(self):
    total_pay = round(self.salary * 1/24, 2)
    return total_pay


class Commission(Salary):
  def __init__(self, salary, commission_rate):
    super().__init__(salary)
    self.commission_rate = commission_rate * .01
    self.receipts = []
  
  def add_receipt(self, receipt):
    self.receipts.append(receipt)

  def compute_pay(self):
    total_sales = 0
    float_receipts = [float(i) for i in self.receipts]
    salary_pay = self.salary * 1/24
    for receipt in float_receipts:
      total_sales += receipt
    commissioned_pay = total_sales * self.commission_rate
    total_pay = salary_pay + commissioned_pay
    return round(total_pay, 2)
     
      