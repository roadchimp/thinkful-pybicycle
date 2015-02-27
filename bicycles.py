#Create a file named bicycles.py that contains each of your classes.
#Create a file named main.py that imports those classes, and uses them.

class Wheel(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
    
class Frame(object):
  def __init__(self, material, weight, cost):
    self.material = material
    self.weight = weight
    self.cost = cost

class Manufacturer(object):
  def __init__(self, name, margin, catalog):
    self.name = name
    self.margin = margin
    self.catalog = []
  
class Bicycle(object):
  def __init__(self, model, frame, wheel):
    self.model = model
    self.frame = frame
    self.wheel = wheel
  
  # we want to use a function, because it is not dependent on the initialiazation of the object (computed property)
  def weight(self):
    return (self.wheel.weight * 2) + self.frame.weight
  
  def cost(self):
    return (self.wheel.cost * 2) + self.frame.cost
    

class BikeShop(object):
  def __init__(self, name, inventory, margin):
    self.name = name
    self.inventory = []
    self.margin = margin

  def add_inventory(self, *bicycle):
    for unit in bicycle:
      self.inventory.append(unit)

  def print_inventory(self):
    inventory_string = "Inventory \n" 
    for bike in self.inventory:
      inventory_string += bike.model + "\n"
    return inventory_string


  def inventory_wholesale(self):
    w = 0
    for bike in self.inventory:
      w+= bike.cost()
    return w
  
  def inventory_retail(self):
    r = 0
    for bike in self.inventory:
      r+= bike.cost() * (1+ self.margin)
    return r
  
  def potential_profit(self):
    return self.inventory_retail() - self.inventory_wholesale()
    
    
  def salesprice(self, bicycle):
    return bicycle.Bicycle_cost * (self.margin + 1)/ 100.0 
    
class Customer(object):
  def __init__(self, name, budget, bike):
    self.name = name
    self.budget = budget
    self.bike = bike

