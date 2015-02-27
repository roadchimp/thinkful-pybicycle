class Bicycle(object):
  def __init__(self, model, weight, cost, quantity):
    self.model = model
    self.weight = weight
    self.cost = cost
    self.quantity = quantity
  
class BikeShop(object):
  def __init__(self, name, inventory, margin):
    self.name = name
    self.inventory = inventory
    self.margin = margin
    
class Customer(object):
  def __init__(self, name, budget, bike):
    self.name = name
    self.budget = budget
    self.bike = bike

#Create a Bicycle Shop
def initialize_shop(shopname):
  shopname = BikeShop(shopname, None, 20)
  print "Welcome to %s" %shopname.name
  return shopname
  
#Add 6 Bikes to Inventory 
def add_inventory(shopname):
  shopname.Inventory = []
  shopname.Inventory.append(Bicycle("PureFix Papa", 40, 337, 10))
  shopname.Inventory.append(Bicycle("PureFix Coolidge", 40, 299, 10))
  shopname.Inventory.append(Bicycle("Diamondback Century 5", 30, 999, 10))
  shopname.Inventory.append(Bicycle("Diamondback Interval Carbon", 45, 500, 10))
  shopname.Inventory.append(Bicycle("Schwinn Huntington", 50, 105, 10))
  shopname.Inventory.append(Bicycle("Schwinn Starlet", 35, 220, 10))
  #print Store101.Inventory[0].model
  #print Store101.Inventory[0].cost
  #print Store101.Inventory[0].quantity
  return shopname.Inventory
    
#Create three customers.
def initialize_customers():
  Customer_list = []
  Customer_list.append(Customer("Larry", "200", None))
  Customer_list.append(Customer("Moe", "500", None))
  Customer_list.append(Customer("Curly", "1000", None))
  #print Customer_list[0].name
  return Customer_list


#Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 
def evaluate_budget(Customer_list, storename):
  for customer in Customer_list:
    i = 0 
    item_price = 0
    print "The budget of %s is %d" %(customer.name, int(customer.budget))
    while i < len(storename.Inventory):
      item_price = float(storename.Inventory[i].cost) * float(1+(storename.margin/100.0))
      if int(customer.budget) > item_price:
        print customer.name, "You can afford the %s which sells for %d " %(storename.Inventory[i].model, item_price)
      else:
        #print customer.name, "You cannot afford the %s which costs %d" %(storename.Inventory[i].model, item_price)
        pass
      i += 1
  
#Print the initial inventory of the bike shop for each bike it carries.
def remaining_inventory():
  i = 0 
  while i < len(Store101.Inventory):
    print "We have %d remaining in inventory for %s" %(Store101.Inventory[i].quantity, Store101.Inventory[i].model)
  i +=1
      
def main():
  Store101 = initialize_shop("Mike's Bikes")
  Store101.inventory = add_inventory(Store101)
  #print Store101.Inventory[1].model
  Customer_list = initialize_customers()
  #print Customer_list[1].name
  evaluate_budget(Customer_list, Store101)
  
#Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.
  for customer in Customer_list:
    customer.bike = (Store101.inventory[0].model)
    print customer.bike

    
if __name__ == "__main__":
  main()


    