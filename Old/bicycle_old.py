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
  
class Bicycle(Manufacturer):
  def __init__(self, model, frame, wheel):
    self.model = model
    self.frame = frame
    self.wheel = wheel
    self.weight = self.wheel.weight * 2 + self.frame.weight
    self.cost = self.wheel.cost * 2 + self.frame.cost
  
#   def Bicycle_weight(self):
#     return self.wheel.weight * 2 + self.frame.weight
#     self.weight = weight
#     self.cost = cost
    
#   def manuf_cost(self):
#     return self.wheel.cost * 2 + self.frame.cost

class BikeShop(object):
  def __init__(self, name, inventory, margin):
    self.name = name
    self.inventory = []
    self.margin = margin

  def Purchase_Bike(self, *Bicycle):
    for unit in Bicycle:
      self.inventory.append(unit)
      print unit.model
      #unit.wholesale_price = unit.cost * ( 1 + unit.Manufacturer.margin)
	  #unit.retail_price = unit.wholesale_price * (1 + self.margin)
	  #self.profit -= unit.wholesale_price   
    
  def salesprice(self, bicycle):
    return bicycle.Bicycle_cost * (self.margin + 1)/ 100.0 
    
class Customer(object):
  def __init__(self, name, budget, bike):
    self.name = name
    self.budget = budget
    self.bike = bike

