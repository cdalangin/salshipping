premium = 125 #premium shipping cost

def ground(weight): #ground shipping per weight
  if weight <= 2:
    cost = (weight * 1.50) + 20 
    return (cost)
  elif weight <= 6:
    cost = (weight * 3.00) + 20
    return (cost)
  elif weight <= 10:
    cost = (weight * 4.00) + 20
    return (cost)
  else:
    cost = (weight * 4.75) + 20
    return (cost)

def drone(weight): #drone shipping per weight
  if weight <= 2:
    cost = (weight * 4.50)
    return (cost)
  elif weight <= 6:
    cost = (weight * 9.00)
    return (cost)
  elif weight <= 10:
    cost = (weight * 12.00)
    return cost
  else:
    cost = (weight * 14.25)
    return cost

def cheapest(weight): #find the cheapest shipping option
  if premium < ground(weight) and drone(weight):
    return premium
  elif drone(weight) < ground(weight) and premium:
    return drone(weight)
  elif ground(weight) < (drone(weight) and premium):
    return ground(weight)

print(cheapest(41.5))
