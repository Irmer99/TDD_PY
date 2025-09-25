def tax_calculator(earn):

  if(earn < 12000):
    return 0
  elif(earn > 12000 or earn < 36000):
    return 0.2 * earn
  else: return 0.4 * earn
    
