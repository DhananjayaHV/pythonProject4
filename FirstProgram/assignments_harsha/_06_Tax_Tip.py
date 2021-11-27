tax_rate = 0.14
tip_rate = 0.18

cost = float (input ("Enter the cost of the meal: "))

tax = cost * tax_rate
tip = cost * tip_rate
total = cost + tax + tip

print ("Total tax amount: "'{0:0.2f}'.format(tax) +'\n'+"Total tip amount" '{0:0.2f}'.format(tip)+'\n'+'{0:0.2f}'.format(total))


