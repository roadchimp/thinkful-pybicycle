from bicycles import BikeShop, Bicycle, Customer, Wheel, Frame, Manufacturer

# Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund.

#After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes.

# Create 2 Manufacturers
# We do not want to capitalize items that cannot be instantiated
# rule: if we can instantiate it, we cpitalize it
manuf1 = Manufacturer("PureFix", 20, None)
manuf2 = Manufacturer("Diamondback", 20, None)
# Create 3 wheels
wheel1 = Wheel("700C", 5, 30)
wheel2 = Wheel("26", 7, 35)
wheel3 = Wheel("20", 5, 20)
# reate 3 frames
frame1 = Frame("aluminum", 3, 150)
frame2 = Frame("carbon", 2, 500)
frame3 = Frame("steel", 5, 75)
#Create 6 models of bike
bike1 = Bicycle("Papa", frame1, wheel1)
bike2 = Bicycle("Coolidge", frame2, wheel1)
bike3 = Bicycle("Romeo", frame3, wheel1)
bike4 = Bicycle("Diamondback Century 5", frame3, wheel1)
bike5 = Bicycle("Diamondback Interval Carbon", frame2, wheel2)
bike6 = Bicycle("Diamondback Starlet", frame3, wheel3)

#print bike1.cost()
#bike1.wheel = wheel2
#print bike1.cost()

#Add bikes to Manufacturers inventory
manuf1.catalog.append(bike1)
manuf1.catalog.append(bike2)
manuf1.catalog.append(bike3)
#return the cost of a bike
#print Manuf1.catalog[0].model

# Create 3 customers
cust1 = Customer("Larry", "200", None)
cust2 = Customer("Moe", "500", None)
cust3 = Customer("Curly", "1000", None)

#Create a Bicycle Shop + buy 6 bicycles
store101 = BikeShop("Mike's Bikes", None, .20)
store101.add_inventory(manuf1.catalog[0], manuf1.catalog[1], manuf1.catalog[2] )
print "wholesale value of invenory:" , store101.inventory_wholesale()
print "retail value of invenory:" , store101.inventory_retail()
print "potential profit", store101.potential_profit()

#Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget. 
def evaluate_budget(customer_list, storename):
  customer_list = []
  customer_list[0].append(Cust1)

  for customer in customer_list:
    i = 0 
    item_price = 0
    print "The budget of %s is %d" %(customer.name, int(customer.budget))
    while i < len(storename.Inventory):
      item_price = float(storename.Inventory[i].cost) * float(1+(storename.margin/100.0))
      if int(customer.budget) > item_price:
        print customer.name, "You can afford the %s which sells for %d " %(storename.inventory[i].model, item_price)
      else:
        #print customer.name, "You cannot afford the %s which costs %d" %(storename.Inventory[i].model, item_price)
        pass
      i += 1 

def main():
  pass

  
  
if __name__ == "__main__":
  main()
